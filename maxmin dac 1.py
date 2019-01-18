l=[]
n=int(input("enter number of elements"))
print("enter those elements")
for i in range(0,n):
    l.append(int(input()))




def maxmin(l):
    
    if len(l)==1:
        #print("min and max is ",l[0])
        min=max=l[0]
    elif len(l)==2:
        if l[0]>l[1]:
            max=l[0]
            min=l[1]
            #print("min is ",l[1]," max is ",l[0])
        elif l[0]<l[1]:
            max=l[1]
            min=l[0]            
            #print("min is " ,l[0]," max is ",l[1])
            
    else:
        mid=int(len(l)/2)
        maxmin(l[:mid])
        maxmin(l[mid:])
        print(max,min)     



a,b=maxmin(l)
print(a,b) 
        
