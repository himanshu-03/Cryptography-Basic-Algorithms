def encrypt(plaintext, n):
    ans = ""

    for i in range(len(plaintext)):
        char = plaintext[i]

        if char == " ":
            ans+=" "
        
        elif (char.isupper()):
            ans += chr((ord(char) + n-65) % 26 + 65)
        
        else:
            ans += chr((ord(char) + n-97) % 26 + 97)
        
    return ans

def decrypt(cipher,n):
    ans1 = ""

    for char in cipher:

        if char == " ":
            ans1 += " "
        
        elif (char.isupper()):
            ans1 += chr((ord(char) - n))

        else:
            ans1 += chr((ord(char) - n))
        
    return ans1

print("\n-----------------------------------------\n")
a = input('Enter plaintext  : ')
n = 3                                   # Caeser Cipher has a fixed shift of key size 3 
t = encrypt(a,n)
print("\n-----------------------------------------\n")
print('Cipher Text is   : ', t)
print("\n-----------------------------------------\n")
print('Original Text is : ', decrypt(t,n))
print("\n-----------------------------------------\n")