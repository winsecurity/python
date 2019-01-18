def collatz(number):
    if number%2==0:
        x=number//2
        print(x)
        return x
    else:
        x=number*3+1
        print(x)
        return x


num=int(input("enter number "))

while True:
    res=collatz(num)
    if res==1:
        break
    else:
        num=int(input("enter number"))