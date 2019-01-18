import random
counter=0
num=int(input("Think number between 1 and 50"))
counter=counter+1
while num!=25:
    if num<25:
        print("Your guess is low")
    else:
        print("Your guess is high")
    num=int(input("Make another guess"))
    counter+=1

print("Good job ! you guessed in ",counter, " guesses")
