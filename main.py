import os
import string
import ascii_art

letters = string.ascii_lowercase


# Create function to clear the screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Create encryption function:
def encryption(sentence, encryption_key):
    encryption_letter = ""
    for char in sentence:
        if char.isalpha():
            char_index = letters.index(char.lower())
            encrypt_char = letters[char_index + int(encryption_key)]
            if char == char.capitalize():
                encryption_letter += encrypt_char.upper()
            else:
                encryption_letter += encrypt_char
        else:
            encryption_letter += char
    print(encryption_letter)

print(ascii_art.logo)
original_sentence = input("Enter the sentence you want to encrypt: ")
shift_key = input("Enter the encryption key: ")

encryption(original_sentence,shift_key)





