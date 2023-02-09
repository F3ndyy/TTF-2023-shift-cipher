from dotenv import load_dotenv
import os

def encrypt(text: str, key: int) -> str:
    Newstr=''
    for char in text:
        if char.isalpha()==True & char.islower()==True:
            ASCII=ord(char)
            Pos=ASCII-97
            posnuova=Pos+key
            End=int(posnuova+97)
            Newstr=Newstr + chr(End)
        else:
            Newstr += char
    return Newstr

def _main():
    load_dotenv()
    # read your secret encryption key from the .env file
    k = os.getenv("CIPHER_KEY")
    # read from encrypt_input.txt
    with open("./encrypt_input.txt") as input:
        lines=input.readlines()
    # call encrypt on each line with your key
    # write the encrypted lines to encrypt_output.txtc
        with open("./encrypt_output.txt", "w") as output:
            for line in lines:
                encrypted=encrypt(line, int(k))
                output.write(encrypted)


if __name__ == "__main__":
    _main()
