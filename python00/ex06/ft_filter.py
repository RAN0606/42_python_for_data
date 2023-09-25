def ft_filter(func, iterable):

    """ft_filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    # return (item for item in iterable if (func(item) or func is None))
    return ([item for item in iterable if (func(item) or func is None)])


def ft_iseven(x):
    return x % 2 == 0


def main():
    numbers = [0, 1, 2, 3, 4, 5, 6]

    print("ft_filter Reslult:", list(ft_filter(ft_iseven, numbers)))
    print(ft_filter.__doc__)
    print("\n\nfilter Reslult:", list(filter(ft_iseven, numbers)))
    print(filter.__doc__)


if __name__ == "__main__":
    main()
