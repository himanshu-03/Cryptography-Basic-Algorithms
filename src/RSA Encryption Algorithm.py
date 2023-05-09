import math

def gcd(a, h):              # Function to calculate GCD between e and phi(n)
	temp = 0
	while(1):
		temp = a % h
		if (temp == 0):
			return h
		a = h
		h = temp
		
print('\n----------------------------------------------------\n')
p = int(input('Enter the value of p       : '))
print('\n----------------------------------------------------\n')
q = int(input('Enter the value of q       : '))
print('\n----------------------------------------------------\n')
msg = int(input('Enter the value of message : '))

n = p * q
e = 2                                   # 1 < e < phi(n)
phi = (p - 1) * (q - 1)                 # phi(n)
while (e < phi):
	if(gcd(e, phi) == 1):
		break
	else:
		e = e + 1

k = 2
d = (1 + (k*phi))/e               # To get the value of private key (decryption key), we are assuming the value of k 

c = pow(msg, e)
c = math.fmod(c, n)
print('\n----------------------------------------------------\n')
print("Encrypted data             :", c)

m = pow(c, d)
m = math.fmod(m, n)
print('\n----------------------------------------------------\n')
print("Original Message Sent      :", m)
print('\n----------------------------------------------------\n')