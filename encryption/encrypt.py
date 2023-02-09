from dotenv import load_dotenv
import os


def encrypt(text: str, key: int) -> str:

    pass


def _main():
    load_dotenv()
    # read your secret encryption key from the .env file
    k = os.getenv("CIPHER_KEY")
    print(type(k))
    # read from encrypt_input.txt
    with open("./encrypt_input.txt") as input:
        print(input.readlines())
    # call encrypt on each line with your key
    # write the encrypted lines to encrypt_output.txtc
    with open("./encrypt_output.txt", "w") as output:
        output.write("TEST")
   


if __name__ == "__main__":
    _main()
