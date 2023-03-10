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

a = input('Enter plaintext: ')
n = int(input('Enter shift key: '))
t = encrypt(a,n)
print('Cipher Text is: ', t)
print('Original Text is: ', decrypt(t,n))
