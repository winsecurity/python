n=int(input("enter number of elements"))
l=[]
for i in range(0,n):
    l.append(int(input()))

min=max=l[0]
for i in range(0,len(l)):
    if l[i]<min:
        min=l[i]
    elif l[i]>max:
        max=l[i]

print("max is",max)
print("min is ",min)