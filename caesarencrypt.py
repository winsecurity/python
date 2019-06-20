'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


pt=input("enter plain text")
key=int(input("enter key to encrypt"))

cipher=""
for i in range(0,len(pt)):
    if pt[i]==' ':
        cipher+=' '
    
    else:
        cipher+=alpha[(alpha.index(pt[i])+key)%26]


print(cipher)

print("**********DECRYPTING***********")

temp=''
counter=0
for i in range(0,26):
    for every in range(0,len(cipher)):
        temp+=alpha[(alpha.index(cipher[every])+i)%26]
    print(temp)
    if temp==pt:
        print("got plain text ",temp)
        break
    counter+=1
    temp=''

#print(counter)

