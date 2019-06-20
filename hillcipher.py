l=[]

temp=[]
res=[]
res2=[]
pt=input("enter plain text")
key=input("enter key")

alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

l.append(key[0:3])
l.append(key[3:6])
l.append(key[6:9])

#print(l)

for i in range(0,len(l)):
    for every in range(0,3):
        temp.append(l[i][every])
    res.append(temp)
    temp=[]
    
    
#print(res)    
x=0

for i in range(0,len(res)):
    for every in range(0,3):
        x=alpha.index(res[i][every])
        temp.append(x)
    res2.append(temp)
    temp=[]

#print(res2)

b=[]
mul=[]
for i in range(0,len(pt)):
    b.append(alpha.index(pt[i]))

#print(b)
temp2=0
for i in range(0,3):
    for every in range(0,3):
        temp2+=res2[i][every]*b[every]
    
    mul.append(temp2)
    temp2=0

#print(mul)

for i in range(0,3):
    temp2=mul[i]%26
    print(alpha[temp2],end="")






        
