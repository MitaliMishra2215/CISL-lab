from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# Function to make sure the key is exactly 8 bytes
def get_key():
    key = input("Enter 8-character key: ")
    while len(key) != 8:
        print("Key must be exactly 8 characters!")
        key = input("Enter 8-character key: ")
    return key.encode()

# Get user input
key = get_key()
plaintext = input("Enter message to encrypt: ")

# Create DES cipher in ECB mode
cipher = DES.new(key, DES.MODE_ECB)

padded_text = pad(plaintext.encode(), DES.block_size)
encrypted_bytes = cipher.encrypt(padded_text)
print("\nEncrypted (hex):", encrypted_bytes.hex())

decrypted_bytes = cipher.decrypt(encrypted_bytes)
unpadded_text = unpad(decrypted_bytes, DES.block_size).decode()
print("Decrypted text:", unpadded_text)