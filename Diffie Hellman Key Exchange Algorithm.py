from random import randint
if __name__ == '__main__':
    R = int(input('Enter the value of R: '))
    S = int(input('Enter the value of S: '))

    a = int(input('Enter secret key a: '))
    p = int(pow(S,a,R)) 

    b = int(input('Enter secret key b: '))
    q = int(pow(S,b,R)) 
     
    A = int(pow(q,a,R))
    B = int(pow(p,b,R))
     
    print('\n\n')
    print('Value of R is : %d'%(R))
    print('Value of S is : %d'%(S))
    print('Private Key a is: %d'%(a))
    print('Private Key b is : %d'%(b))
    print('Alice\'s Secret key is : %d'%(A))
    print('Bob\'s Secret key is : %d'%(B))
