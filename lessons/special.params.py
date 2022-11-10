"""Examples of optional parameters and Union types."""

def hello(name: str = "World") -> str:
    """A delightful greeting."""
    greeting: str = "Hello, " + name
    return greeting

# Single -argument
print(hello(1))

# No arguments!
print(hello())
