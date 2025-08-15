def caesar_encrypt(plaintext, key):
    ciphertext = "" 
    for ch in plaintext:
        if ch.isupper():
            ch = chr((ord(ch) - ord('A') + key) % 26 + ord('A'))
        elif ch.islower():
            ch = chr((ord(ch) - ord('a') + key) % 26 + ord('a'))
    
        ciphertext += ch
    return ciphertext


def caesar_decrypt(ciphertext, key):
    plaintext = ""
    for ch in ciphertext:
        if ch.isupper():
            ch = chr((ord(ch) - ord('A') - key + 26) % 26 + ord('A'))
        elif ch.islower():
            ch = chr((ord(ch) - ord('a') - key + 26) % 26 + ord('a'))
        
        plaintext += ch
    return plaintext


if __name__ == "__main__":
    plaintext = input("Enter plaintext: ")
    key = int(input("Enter key: "))

    encrypted = caesar_encrypt(plaintext, key)
    print("Encrypted Text:", encrypted)

    '''decrypted = caesar_decrypt(encrypted, key)
    print("Decrypted Text:", decrypted)'''














# Else keep the character as it is (punctuation/space)