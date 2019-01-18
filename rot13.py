

alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
string=str(input("enter string for rot13 decode"))

for every in string:
    converted_index=alpha.index(every)
    new=(converted_index+13)%26
    print(alpha[new],end="")
