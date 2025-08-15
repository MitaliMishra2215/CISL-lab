def vigenere_encrypt(plaintext, key):
    encrypted_text = ""
    key = key.upper()
    key_length = len(key)
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % key_length]) - ord('A')
            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            key_index += 1
        else:
            encrypted_char = char
        encrypted_text += encrypted_char

    return encrypted_text

# Input from user
plaintext = input("Enter the plaintext: ")
key = input("Enter the key: ")

# Encryption
ciphertext = vigenere_encrypt(plaintext, key)
print("Encrypted text:", ciphertext)