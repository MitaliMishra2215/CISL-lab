
def AtbashCipher(text):
    result = ""
    for ch in text:
        if ch.isupper():
            result += chr(ord('A') + (ord('Z') - ord(ch)))
        elif ch.islower():
            result += chr(ord('a') + (ord('z') - ord(ch)))
        else:
            result += ch  
    return result


input_text = input("Enter the text to encrypt using Atbash Cipher: ")
output = AtbashCipher(input_text)
print("Cipher Text:", output)





#direct name means not taking input from user
'''def AtbashCipher(text):
    result = ""
    for ch in text:
        if ch.isupper():
            result += chr(ord('A') + (ord('Z') - ord(ch)))
        elif ch.islower():
            result += chr(ord('a') + (ord('z') - ord(ch)))
        else:
            result += ch  
    return result


input_text = "Mitali Mishra"
output = AtbashCipher(input_text)
print("Cipher Text:", output)'''


