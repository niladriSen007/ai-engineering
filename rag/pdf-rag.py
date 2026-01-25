from langchain_community.document_loaders import UnstructuredPDFLoader, DirectoryLoader
from langchain_openai import OpenAIEmbeddings
from langchain_groq import ChatGroq
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
from dotenv import load_dotenv
from langchain.tools import tool
from uuid import uuid4
import nltk
import os
from langchain.agents import create_agent

load_dotenv(override=True)

# nltk.download("punkt_tab")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment variables.")
if not PINECONE_API_KEY:
    raise ValueError("PINECONE_API_KEY not found in environment variables.")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in environment variables.")


pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index("rag-udemy")
embeddings = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=512)

# creating the vector store
vector_store = PineconeVectorStore(embedding=embeddings, index=index)

pdf_dir = "./doc"
loader = DirectoryLoader(path=pdf_dir, glob="./*.pdf", loader_cls=UnstructuredPDFLoader)
# loader = UnstructuredPDFLoader("./doc/Evolution.pdf")
docs = loader.load()

# print(docs[0])


# splitting the text
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,  # chunk size (characters)
    chunk_overlap=200,  # chunk overlap (characters)
    add_start_index=True,  # track index in original document
)
text_chunks = text_splitter.split_documents(docs)
# print(f"Length is - {len(text_chunks)}")
uuids = [str(uuid4()) for _ in range(len(text_chunks))]
doc_ids = vector_store.add_documents(documents=text_chunks, ids=uuids)
# print(doc_ids)

llm = ChatGroq(
    model="qwen/qwen3-32b",
    temperature=0,
    # max_tokens=None,
    # reasoning_format="parsed",
    # timeout=None,
    # max_retries=2,
)


@tool(response_format="content_and_artifact")
def retrieve_context(query: str):
    """Retrieve information to help answer a query."""
    retrieved_docs = vector_store.similarity_search(query, k=2)
    serialized = "\n\n".join(
        (f"Source: {doc.metadata}\nContent: {doc.page_content}")
        for doc in retrieved_docs
    )
    return serialized, retrieved_docs


tools = [retrieve_context]
# If desired, specify custom instructions
prompt = (
    "You have access to a tool that retrieves context from PDF. "
    "Use the tool to help answer user queries."
)
agent = create_agent(llm, tools, system_prompt=prompt)

query = "Tell me something about Evolution of life forms within 100 words."

for event in agent.stream(
    {"messages": [{"role": "user", "content": query}]},
    stream_mode="values",
):
    event["messages"][-1].pretty_print()
