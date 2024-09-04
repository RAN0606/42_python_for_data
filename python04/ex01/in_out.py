def square(x: int | float) -> int | float:
    """Calculate the square of the given number"""
    return (x**2)


def pow(x: int | float) -> int | float:
    """Power the given number by itself"""
    return (x**x)


def outer(x: int | float, function) -> object:
    """
    Create a counter function that performs calculations
    """
    count = 0

    def inner() -> float:
        """
        Execute the provided function, update the value, and return the result.
        """
        nonlocal count
        if count == 0:
            count = x
        count = function(count)
        return count
    return inner
