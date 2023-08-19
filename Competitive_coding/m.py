def decrypt_cipher_message(cipher_string, cipher_message):
    # Create a dictionary to map characters in the cipher string to the original English alphabet
    strDict = { chr(97 + i):cipher_string[i] for i in range(26)}
    res = ""
    # print(strDict)

    for i in range(len(cipher_message)):
       
        if cipher_message[i].isalpha(): 
                
            if cipher_message[i].islower():
                    res += strDict[cipher_message[i]]
            else :
                    res += strDict[cipher_message[i].lower()].upper()
        else:
            if cipher_message[i]=="_":
                res += " "

    return res

# Read the number of cipher messages and the cipher string (Str) from input
n, cipher_string = input().split()
n = int(n)

# Process each cipher message and print the decrypted original message
for _ in range(n):
    cipher_message = input()
    decrypted_message = decrypt_cipher_message(cipher_string, cipher_message)
    print(decrypted_message)


# 1 ohsdugyjpzlknexarmqitcvbfw
# Bnkka!
