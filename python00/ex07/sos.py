import sys


NESTED_MORSE = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ' ': '/'}


def ft_morse_encrypt(text: str):
    morsecode = ""
    try:
        for i in range(len(text)):
            c = text[i].upper()
            morsecode += NESTED_MORSE[c]
            if i != len(text) - 1:
                morsecode += ' '
        print(morsecode)
    except KeyError:
        print("AssertionError: the arguments are bad")


def main():
    argList = sys.argv
    if len(argList) != 2:
        print("AssertionError: the arguments are bad")
    else:
        ft_morse_encrypt(argList[1])


if __name__ == "__main__":
    main()
