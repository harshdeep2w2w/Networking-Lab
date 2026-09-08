'''def caesar_encrypt(text, key):
    result = ""

    for char in text:
        if char.isalpha():

            if char.isupper():
                result += chr((ord(char) - ord('A') + key) % 26 + ord('A'))

            else:
                result += chr((ord(char) - ord('a') + key) % 26 + ord('a'))

        else:
            result += char

    return result


def caesar_decrypt(text, key):
    return caesar_encrypt(text, -key)

plaintext = input("Enter the plaintext: ")
key = int(input("Enter the key: "))

ciphertext = caesar_encrypt(plaintext, key)

decrypted_text = caesar_decrypt(ciphertext, key)

print("\nPlaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted Text:", decrypted_text)'''






def vigenere_encrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0

    for char in text:

        if char.isalpha():

            shift = ord(key[key_index % len(key)]) - ord('A')

            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

            key_index += 1

        else:
            result += char

    return result

def vigenere_decrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0

    for char in text:

        if char.isalpha():

            shift = ord(key[key_index % len(key)]) - ord('A')

            if char.isupper():
                result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))

            else:
                result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))

            key_index += 1

        else:
            result += char

    return result


plaintext = input("Enter the plaintext: ")
key = input("Enter the keyword: ")

ciphertext = vigenere_encrypt(plaintext, key)

decrypted_text = vigenere_decrypt(ciphertext, key)

print("\nPlaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted Text:", decrypted_text)