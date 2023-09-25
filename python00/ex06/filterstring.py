import sys


def ft_filter(func, iterable):
    return ([item for item in iterable if (func(item) or func is None)])


def ft_filter_string(word: str, nb: int) -> bool:
    return (len(word) > nb)


def main():
    argList = sys.argv
    if len(argList) != 3:
        print("AssertionError: the arguments are bad")
    else:
        try:
            nb = int(argList[2])
            wordList = argList[1].split(" ")
            print(ft_filter(lambda x: ft_filter_string(x, nb), wordList))
        except ValueError:
            print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
