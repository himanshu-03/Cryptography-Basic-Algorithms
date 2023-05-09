import numpy as np

def rail_fence_encrypt(message,rows):

    cols = len(message)
    char_arr = np.empty((rows,cols), dtype = 'str')
    char_arr[:] = ''
    col = 0
    row = 0
    direction = 'down'
    
    encrypt_message = ''
    
    for char in message:
            char_arr[row][col] = char
            if (row == rows-1):
                direction = 'down'  
            
            if (row == 0):
                direction = 'up'  

            if direction == 'down':
                row = row - 1
            
            if direction == 'up':
                row = row + 1 
            
            col = col + 1   
    
    for char_list in char_arr:
        for char in char_list:
            encrypt_message = encrypt_message+char
    
    return encrypt_message

        
def rail_fence_decrypt(message, rows):

    cols = len(message)
    char_arr = np.empty((rows,cols), dtype='str')
    char_arr[:] = ''
    col = 0
    row = 0
    direction = 'down'
    
    for char in message:
            char_arr[row][col] = '*'
            if (row == rows - 1):
                direction = 'down'  
            
            if (row == 0):
                direction = 'up'  
            
            if direction == 'down':
                row = row - 1
            
            if direction == 'up':
                row = row + 1
            
            col = col + 1
            
    char_cnt = 0
    
    for j in range(rows):
        for i in range(cols):
            if char_arr[j][i] == '*':
                char_arr[j][i] = message[char_cnt]
                char_cnt = char_cnt + 1
            
    decrypt_message = ''
    
    for i in range(cols):
        for j in range(rows):
            if char_arr[j][i] != '':
                decrypt_message=decrypt_message + char_arr[j][i]
                
    return decrypt_message   


print("\n------------------------------------------\n")
message = input('Enter the message      : ')
print("\n------------------------------------------\n")
rows = int(input('Enter number of rows   : '))

encrypt_message=rail_fence_encrypt(message, rows)
print("\n------------------------------------------\n")
print('Encrypted Message      :',encrypt_message)

print("\n------------------------------------------\n")
decrypt_message=rail_fence_decrypt(encrypt_message, rows)
print('Decrypted Message      :',decrypt_message)


print("\n------------------------------------------\n")