
l=[]
l.append(int(input("enter number")))

prime=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197,199]
semiprime=[]
for i in range(0,len(prime)):
    for j in range(0,len(prime)):
        temp=prime[i]*prime[j]
        if temp<200:
            semiprime.append(temp)
        else:
            break

semiprime.sort()

s=[]
for each in semiprime:
    if each not in s:
        s.append(each)


for i in range(0,len(s)):
    temp=s[i]
    if temp==l[0]:
        print("YES")
    for j in range(0,len(s)):
        
        temp=temp+s[j]
        if l[0]<temp or temp>200:
            print()
        elif l[0]==temp:
            print("YES")
        else:
            print("NO")    
        
        