import math

def encryptMessage(message, key):
	
	encrypt_cipher = ""

	k_indx = 0                      # Tracking Key Indices

	msg_len = float(len(message))
	msg_lst = list(message)             # Converting the characters into list

	key_lst = sorted(list(key))     # Sorting the key with the help of their indices

	col = len(key)                  # Length of the column is determined by length of they key
	
	row = int(math.ceil(msg_len / col))         # Maximum row can be calculates with the help of columns and message length

	fill_null = int((row * col) - msg_len)      # Getting the number of null values in the matrix
	msg_lst.extend('_' * fill_null)             # Filling those cells with '_'


	matrix = [msg_lst[i: i + col]                       # Creating matrix and inserting values in the matrix row wise
			for i in range(0, len(msg_lst), col)]

	for _ in range(col):                                # Reading the matrix column wise
		curr_idx = key.index(key_lst[k_indx])
		encrypt_cipher += ''.join([row[curr_idx]
						for row in matrix])
		k_indx += 1

	return encrypt_cipher


def decryptMessage(encrypt_message, key):
	
	msg = ""

	k_indx = 0                      # Tracking Key Indices

	msg_indx = 0                    # Track Message Indices
	msg_len = float(len(encrypt_message))    # Length of the Message
	msg_lst = list(encrypt_message)

	col = len(key)                  # Length of Columns is determined by the key length
	
	row = int(math.ceil(msg_len / col))     # Maximum row can be calculates with the help of columns and message length

	key_lst = sorted(list(key))         # Sorting the key with the help of their indices

	decrypt_cipher = []                 # Creating an empty matrix to store the decrypted message
	for _ in range(row):
		decrypt_cipher += [[None] * col]

	for _ in range(col):                            # Arranging column in the sorted key order 
		curr_idx = key.index(key_lst[k_indx])

		for j in range(row):                                        # Reading the encrypted message list and assigning the
			decrypt_cipher[j][curr_idx] = msg_lst[msg_indx]         # value to the respective lists
			msg_indx += 1
		k_indx += 1

	try:
		msg = ''.join(sum(decrypt_cipher, []))
	except TypeError:
		raise TypeError("This program cannot handle repeating words.")

	null_count = msg.count('_')

	if null_count > 0:
		return msg[: -null_count]

	return msg


print("\n------------------------------------------\n")
message = input('Enter the message  : ')
print("\n------------------------------------------\n")
key = input('Enter the key      : ')

encrypt_message=encryptMessage(message, key)
print("\n------------------------------------------\n")
print('Encrypted Message  :',encrypt_message)

print("\n------------------------------------------\n")
decrypt_message=decryptMessage(encrypt_message, key)
print('Decrypted Message  :',decrypt_message)


print("\n------------------------------------------\n")
