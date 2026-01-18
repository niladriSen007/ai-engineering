# AI Engineering Learning Repository

## Repository Purpose
This is a personal learning workspace for exploring Python, NumPy, and PySpark. The codebase contains educational examples and practice code focused on Python fundamentals and data engineering technologies.

## Project Structure

```
ai-engineering/
├── python-learning/    # Python fundamentals and core concepts
├── numpy/             # NumPy data science examples (in development)
└── pyspark/          # PySpark distributed computing examples (in development)
```

## Code Style & Patterns

### Python Fundamentals Focus
The `python-learning/` directory demonstrates core Python concepts through standalone examples:
- **Tuple unpacking patterns**: Extensive use of unpacking and destructuring ([tuples.py](python-learning/tuples.py))
  ```python
  a, *b = coordinate  # Extended unpacking
  ((x1, y1), (x2, y2), (x3, y3)) = nested_data  # Nested destructuring
  ```
- **List comprehensions over loops**: Performance-aware patterns with timing comparisons ([basics.py](python-learning/basics.py#L93-L113))
- **Type hints**: Dictionary type annotations using modern syntax (`dict[str, int]`)
- **Shallow vs deep copy**: Explicit examples showing mutation behavior with nested structures ([basics.py](python-learning/basics.py#L68-L84))

### Learning-First Approach
- Code includes print statements and timing comparisons to demonstrate behavior and performance
- Each file explores a specific concept area (tuples, basics, etc.)
- Examples are self-contained and runnable

## Development Workflow

### Running Python Files
Execute Python scripts directly from the workspace root:
```powershell
python python-learning/basics.py
python python-learning/tuples.py
```

### Key Dependencies
- Standard library modules: `copy`, `time`
- NumPy and PySpark examples are planned but not yet implemented

## When Writing New Code

1. **Keep examples self-contained**: Each file should be independently runnable
2. **Add print statements**: Make behavior visible for learning purposes
3. **Include timing comparisons**: When demonstrating performance differences (e.g., loops vs comprehensions)
4. **Use type hints**: Especially for complex data structures like dictionaries
5. **Comment sparingly**: Code should be readable; comments for "why" not "what"
6. **Progressive complexity**: Start with simple examples, build to nested/complex patterns

## Areas in Development
- NumPy: Notebook created but no content yet
- PySpark: File structure in place but empty

## Notes
This is a learning environment, not a production codebase. Code prioritizes educational clarity over production patterns like error handling, logging, or modular architecture.
