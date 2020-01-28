import re


def main() :
    plaintext = input("Enter plane text : ")
    key = input("Enter a Key (26 Char) :")
    while len(key) != 26 or not re.match("^[A-Za-z]*$", key) :
        print("Try again!, Key must be 26 char long and between [A-z,a-z]")
        key = input("Enter a Key (26 Char) :")

    # Convert to Upper case and pass to encrypt function
    ciphertext = encrypt_text(plaintext.upper(), key.upper())
    print("Ciphertext : ", ciphertext)

    print("Decrypt text: ", decrypt_text(ciphertext.upper(), key.upper()))


# Remove white space from text
def trim_space(string) :
    return string.replace(' ', '')


# Remove Special Chars
def trim_special_chars(string) :
    # Add more Special Chars
    special_chars = "!@#$,"'’-.'
    for char in special_chars :
        string = string.replace(char, "")
    return string


def encrypt_text(plaintext, key) :
    # trim_space
    plaintext = trim_space(plaintext)
    # Remove Special Chars and Convert into upper case
    plaintext = trim_special_chars(plaintext)
    key_dictionary=substitute_text(plaintext, key)
    print("Plaintext :",plaintext)
    ciphertext = ""
    for char in plaintext:
        ciphertext = ciphertext+key_dictionary[char]
    return ciphertext

def decrypt_text(ciphertext, key) :
    # trim_space
    ciphertext = trim_space(ciphertext)
    # Remove Special Chars and Convert into upper case
    ciphertext = trim_special_chars(ciphertext)
    key_dictionary = substitute_text(ciphertext, key)
    plaintext = ""
    for char in ciphertext :
        plaintext = plaintext + key_dictionary[char]
    return plaintext


def substitute_text(string, key) :
    key_dictionary = {}
    for char,key_char in zip(range(ord('A'), ord('Z') + 1), key) :
        key_dictionary[chr(char)]=key_char
    return  key_dictionary

if __name__ == "__main__" :
    main()
