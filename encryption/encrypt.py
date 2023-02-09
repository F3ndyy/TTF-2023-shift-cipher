import os
from dotenv import load_dotenv


def encrypt(text: str, key: int) -> str:
    """Applies a shift cipher (also known as Caesar cipher) to the input text,
    by rotating it LEFT of key number of positions.
    Returns the rotated text.
    """
    pass


def _main():
    # read your secret encryption key from the .env file
    load_dotenv()
    # read from encrypt_input.txt
    key = os.getenv("Secret_Key")
    print(type(key))
    # call encrypt on each line with your key
    with open("./encryption/encrypt_input.txt") as input:
        text = input.readlines()
        print(text)
    # write the encrypted lines to encrypt_output.txt
    with open("./encryption/encrypt_input.txt") as output:
        output.write("TEST")


if __name__ == "__main__":
    _main()
