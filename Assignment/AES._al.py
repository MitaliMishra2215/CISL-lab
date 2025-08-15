from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

# Take key from user
key_input = input("Enter encryption key (16/24/32 characters): ")
key = key_input.encode()

# Validate key length
if len(key) not in [16, 24, 32]:
    raise ValueError("Key must be 16, 24, or 32 characters long!")

# Take message from user
plaintext = input("Enter text to encrypt: ").encode()

# Generate random IV
iv = get_random_bytes(16)

# Create cipher and encrypt
cipher = AES.new(key, AES.MODE_CBC, iv)
ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

# Encode ciphertext + IV to base64 so it's easy to store/send
encrypted_data = base64.b64encode(iv + ciphertext).decode()
print("Encrypted (Base64):", encrypted_data)

# ----- Decryption -----
# Decode from base64
encrypted_bytes = base64.b64decode(encrypted_data)

# Extract IV and ciphertext
iv_dec = encrypted_bytes[:16]
ciphertext_dec = encrypted_bytes[16:]

# Create cipher for decryption
cipher_dec = AES.new(key, AES.MODE_CBC, iv_dec)
decrypted = unpad(cipher_dec.decrypt(ciphertext_dec), AES.block_size)

print("Decrypted text:", decrypted.decode())

