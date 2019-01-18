
n=int(input("enter number of elements"))
m=int(input("enter total bag capacity"))

w=[]
p=[]

for i in range(0,n):
    w.append(int(input("enter weight")))
    p.append(int(input("enter its value")))

#print(w)
#print(v)

d={}




pwr=[]

for i in range(0,n):
    pwr.append(p[i]/w[i])

for i in range(0,n):
    d1={w[i]:pwr[i]}
    d.update(d1)

pwr.sort()
print(d)
print(pwr)
winclu=[]

for key,value in d.items():
    if value==pwr[-1]:
        print(key)









