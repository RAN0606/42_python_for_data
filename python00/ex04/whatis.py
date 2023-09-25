import sys

argList = sys.argv
if len(argList) > 2:
    print("AssertionError: more than one argument is provided")
elif len(argList) == 2:
    try:
        num = int(argList[1])
        if num % 2 == 0:
            print("I'm Even.")
        elif num % 2 == 1:
            print("I'm Odd.")
    except ValueError:
        print("AssertionError: argument is not an integer")
