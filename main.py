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
            encrypt_char_index = (char_index + int(encryption_key)) % 26
            encrypt_char = letters[encrypt_char_index]
            if char == char.capitalize():
                encryption_letter += encrypt_char.upper()
            else:
                encryption_letter += encrypt_char
        else:
            encryption_letter += char
    print(encryption_letter)

# Create decryption function:
def decryption(encrypted_sentence, decryption_key):
    decryption_letter = ""
    for char in encrypted_sentence:
        if char.isalpha():
            char_index = letters.index(char.lower())
            decrypt_char_index = (char_index - int(decryption_key)) % 26
            decrypt_char = letters[decrypt_char_index]
            if char == char.capitalize():
                decryption_letter += decrypt_char.upper()
            else:
                decryption_letter += decrypt_char
        else:
            decryption_letter += char
    print(decryption_letter)



print(ascii_art.logo)
print("Welcome to Caesar Cipher")
print("1. Encryption")
print("2. Decryption")

choice = input("Select number for the list:")
if choice == "1":
    original_sentence = input("Enter the sentence you want to encrypt: ")
    shift_key = input("Enter the encryption key: ")
    encryption(original_sentence,shift_key)
elif choice == "2":
    encrypted_letter = input("Enter the encrypted letter: ")
    decryption_key = input("Enter the decryption key: ")
    decryption(encrypted_letter, decryption_key)
else:
    print("Invalid input, Try again.")




