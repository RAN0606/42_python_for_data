import sys
import string


def count_character(text: str):
    nbAll = len(text)
    nbUpper = 0
    nbLower = 0
    nbPunct = 0
    nbSpace = 0
    nbDigit = 0
    if (nbAll > 0):
        for c in text:
            if c.isdigit():
                nbDigit += 1
            elif c.isupper():
                nbUpper += 1
            elif c.islower():
                nbLower += 1
            elif c in string.punctuation:
                nbPunct += 1
            elif c.isspace():
                nbSpace += 1
    print("The text contains {0} characters:".format(nbAll))
    print("{0} upper letters".format(nbUpper))
    print("{0} lower letters".format(nbLower))
    print("{0} punctuation marks".format(nbPunct))
    print("{0} spaces".format(nbSpace))
    print("{0} digits".format(nbDigit))


def main():
    argList = sys.argv
    text = ""

    if len(argList) > 2:
        print("AssertionError: more than one argument is provided")
    else:
        if len(argList) == 2:
            text = argList[1]
        elif len(argList) == 1:
            print("What is the text to count?")
            try:
                text = sys.stdin.read()
            except KeyboardInterrupt:
                print("\nUser interrupted input.")
        count_character(text)


if __name__ == "__main__":
    main()
