def affine_encrypt(text, a, b):
    result = ""
    for char in text:
        if char.isalpha():
            x = ord(char.lower()) - ord('a')
            enc = (a * x + b) % 26
            enc_char = chr(enc + ord('a'))
            result += enc_char.upper() if char.isupper() else enc_char
        else:
            result += char
    return result

# Taking input from user
plaintext = input("Enter plaintext: ")
a = int(input("Enter key a (must be coprime with 26): "))
b = int(input("Enter key b: "))

# Validating 'a' is coprime with 26
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

if gcd(a, 26) != 1:
    print("Invalid key 'a'. It must be coprime with 26.")
else:
    encrypted = affine_encrypt(plaintext, a, b)
    print("Encrypted text:", encrypted)