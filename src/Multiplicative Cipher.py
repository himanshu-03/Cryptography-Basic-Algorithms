from sympy import mod_inverse
import math

def multiplicative_encrypt(text, key):
    char_dict = {}
    encrypt_message = ''

    for i in range(26):
         char_dict[chr(ord('a') + i)] = i

    key_list = list(char_dict.keys())
    inv_char_dict = dict(zip(char_dict.values(), char_dict.keys()))

    if math.gcd(26, key) == 1:
        for char in text:
            if char in key_list:
                new_index = (char_dict[char] * key) % 26
                encrypt_message = encrypt_message + inv_char_dict[new_index]
            else:
                encrypt_message = encrypt_message + char
    else:
        print('Invalid Key Selected')
            
    return encrypt_message         
        
def multiplicative_decrypt(text, key):
    char_dict = {}
    decrypt_message = ''

    for i in range(26):
         char_dict[chr(ord('a') + i)] = i
    
    key_list = list(char_dict.keys())
    inv_char_dict = dict(zip(char_dict.values(), char_dict.keys()))

    mult_inv = mod_inverse(key, 26)

    for char in text:
        if char in key_list:
            new_index = (char_dict[char] * mult_inv) % 26
            decrypt_message = decrypt_message + inv_char_dict[new_index]
        else:
            decrypt_message = decrypt_message + char
    
    return decrypt_message


print("\n------------------------------------------\n")
message = input('Enter the message              : ')
print("\n------------------------------------------\n")
key = int(input('Enter the multiplicative key   : '))

encrypt_message=multiplicative_encrypt(message, key)
print("\n------------------------------------------\n")
print('Encrypted Message              :',encrypt_message)

print("\n------------------------------------------\n")
decrypt_message=multiplicative_decrypt(encrypt_message, key)
print('Decrypted Message              :',decrypt_message)


print("\n------------------------------------------\n")