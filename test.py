#n=int(input("enter number of elements to enter"))
#l=[]
#for i in range(0,n):
    #print("enter ",i+1," number")
    #l.append(int(input()))
    
#print(l)

#palindrome or not

def palornot(s):
    if s==s[::-1]:
        print("its palindrome")
    else:
        print("its not palidrome")

def act1(x):
    if x%2==0:
        print("its even number")
    else:
        print("its odd number")

def sum(x,y):
    print(x+y)

def even(l=[],*args):
    count=0
    for item in l:
        if item%2==0:
            count=count+1
    print("number of even numbers are ",count)        
    
list=[1,2,3,4,5,6,8,10]
#even(list)

def reverse(s):
    print(s[::-1])

#reverse("hi")



#while True:
    #x=int(input(""" 1.Accept and store a string 
    #2.print the reversely stored string
    #3.compare 2 numbers and say which is larger
    #4.remove selected letter from string
    #5.Q to quit"""))
    #s="default string"
    
    #if x==1:
        #s=str(input("enter string"))
    
    #if x==2:
        #print(s[::-1])
    
    #if x==3:
        #a=int(input("enter first number"))
        #b=int(input("enter second number"))
        #if a>b:
            #print("first number is larger than the second")
        #elif a<b:
            #print("second number is larger than the first")
        #else:
            #print("they are equal")
    #if x==4:
        #a=str(input("enter letter u want to remove"))
        #s=s.replace("a","")
        #print(s)
    #if x==5:
        #break
        
l=[]
t=[]
s=[]
#n=int(input("enter number of students"))
#for i in range(n):
    #l.append(str(input()))
    #t.append(int(input()))

#s[0]=l[0]+t[0]
#print(s[0])
#for i in range(1,6):
    #print("Driving straight for "+str(i)+" mile")
    
    
#a=int(input("enter first number"))
#b=int(input("enter second number"))
#print("operations between ",a," and ",b," are ")

#print(a,"+",b," is ",a+b)
#print(a,"-",b," is ",a-b)
#print(a,"*",b," is ",a*b)
#print(a,"/",b," is ",a/b)
#print(a,"%",b," is ",a%b)

#if a>b:
    #print(a,">",b)
#elif a<b:
    #print(a,"<",b)
#else:
    #print(a,"=",b)
    
def factorial(n):
    res=1
    while n!=1:
        res*=n
        n=n-1
    return res
x=factorial(5)

print(x)