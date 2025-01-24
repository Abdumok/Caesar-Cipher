import os
# Create function to clear the screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Create encryption function:
def encryption(string, encryption_key):
    string = input("Enter the sentence you want to encrypt: ")
    encryption_key = ""
    while not encryption_key.isdigit():
        encryption_key = input("Enter the encryption key: ")
