def MonoalphabeticEncrypt(plaintext, key_map):
    ciphertext = ""
    for ch in plaintext:
        if ch.isupper():
            ciphertext += key_map[ch]
        elif ch.islower():
            ciphertext += key_map[ch.upper()].lower()
        else:
            ciphertext += ch  
    return ciphertext

key_map = {
    'A': 'Q', 'B': 'W', 'C': 'E', 'D': 'R', 'E': 'T', 'F': 'Y', 'G': 'U',
    'H': 'I', 'I': 'O', 'J': 'P', 'K': 'A', 'L': 'S', 'M': 'D', 'N': 'F',
    'O': 'G', 'P': 'H', 'Q': 'J', 'R': 'K', 'S': 'L', 'T': 'Z', 'U': 'X',
    'V': 'C', 'W': 'V', 'X': 'B', 'Y': 'N', 'Z': 'M'
}


plaintext = input("Enter plaintext: ")
ciphertext = MonoalphabeticEncrypt(plaintext, key_map)
print("Ciphertext:", ciphertext)
