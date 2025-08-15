import numpy as np

# Function to convert text to numbers (A=0, B=1, ..., Z=25)
def text_to_numbers(text):
    return [ord(char) - ord('A') for char in text.upper()]

# Function to convert numbers to text
def numbers_to_text(numbers):
    return ''.join([chr(num % 26 + ord('A')) for num in numbers])

# Encryption function
def hill_cipher_encrypt(message, key_matrix):
    message = message.upper().replace(" ", "")

    # Pad message if its length is not a multiple of 2
    if len(message) % 2 != 0:
        message += 'X'

    encrypted_text = ''
    for i in range(0, len(message), 2):
        pair = message[i:i+2]
        vector = np.array(text_to_numbers(pair)).reshape(2, 1)
        result = np.dot(key_matrix, vector) % 26
        encrypted_text += numbers_to_text(result.flatten())
    
    return encrypted_text

# ---- Main Execution ----
# Get user input
message = input("Enter the message to encrypt (only letters): ")
print("Enter the 2x2 key matrix (4 integers):")

# Key input
key = []
for i in range(4):
    key.append(int(input(f"Element {i+1}: ")))
key_matrix = np.array(key).reshape(2, 2)

# Encrypt the message
encrypted = hill_cipher_encrypt(message, key_matrix)
print("Encrypted message:", encrypted)