"""Deeper understanding on Context Managers"""

# One of the two approaches of creating context managers is referred to as the class-based approach
# This class-based approach requires explicitly defining and implementing the following two methods

# __enter__() everything under the with statement
# __exit__() ensures the breakdown of the context manager

# For example:


class ContextManager:
    """Context Manager class"""

    def __init__(self) -> None:
        print("Initializing class...")

    def __enter__(self) -> None:
        print("Entering context...")

    def __exit__(self, *exc):
        print("Exiting context")


# By implementing enter and exit methods, we are implementing the context management protocol.
# Putting this class in action we would see something like this:
with ContextManager() as cm:
    print("Code inside the with statement...")
