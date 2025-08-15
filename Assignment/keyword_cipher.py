def encrypt(text, keyword):
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = "".join(dict.fromkeys(keyword.upper()))
    cipher = key + ''.join(c for c in abc if c not in key)
    return ''.join(cipher[abc.index(c)] if c.isalpha() else c for c in text.upper())




text = input("Enter text of keyword cipher to be encrypted: ")
keyword = input("Enter keyword: ")
print("Encrypted:", encrypt(text, keyword))