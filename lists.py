
spam=['apples','bananas','tofu','cats']

def makestring(l):
    str1=''
    for item in range(0,len(l)):
        str1=str1+str(l[item])+" , "
    return str1

temp=makestring(spam)
print(temp)