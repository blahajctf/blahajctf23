# Prototype to create an eml file using python

import os
from email import generator
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from cryptography.fernet import Fernet

# where to write the output file
directory = "..\\dist"

body = r"""Greetings Shahmat,

    Our hacking of Blahaj Corp. has proven successful! Our plans have been set in motion, and select pieces of 
    GPT-B-lahaj's knowledge has been successfully replaced with our own code words. 
    
    Two pieces of knowledge have been successfully implanted into GPT-B-lahaj, randomly selected from a list of elements 
    and a list of renaissance artists from simple english wikipedia. The randomly selected element has had it's atomic
    number changed, while the randomly selected renaissance artist has had their country of birth changed. 
    
    It's so absurdly random that they will never be able to figure it out!
    
    The bomb has been planted in their data centers and should go off momentarily. Without their backups, they will be
    unable to isolate our changes to GPT-B-lahaj, and our victory is assured.

We shall rule the day!
Muhlik
"""

subject = "Successful Operation on GPT-B-lahaj"

toAddress = "Shahmat@1337.krew"

fromAddress = "Muhlik@1337.krew"

key = b'S1jFc6YZTyasHwgZFfdQOWzLaTwmQPsh8xqmvx8cLqA='

def create_message():
    msg = MIMEMultipart()
    msg["To"] = toAddress
    msg["From"] = fromAddress
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    return msg


def write_eml_file(msg):
    os.chdir(directory)
    filename = "email.eml"

    with open(filename, 'w') as file:
        emlGenerator = generator.Generator(file)
        emlGenerator.flatten(msg)


def main():
    msg = create_message()
    write_eml_file(msg)

    f = Fernet(key)

    print(f"Encrypting with key {key}")

    with open("email.eml", "rb") as file:
        # read all file data
        file_data = file.read()
    # encrypt data
    encrypted_data = f.encrypt(file_data)
    # write the encrypted file
    with open("email.eml", "wb") as file:
        file.write(encrypted_data)


def decrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)


if __name__ == "__main__":
    main()
    # decrypt('email.eml', key)