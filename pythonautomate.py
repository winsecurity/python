import time

print("answer only with \'yes\' or \'no\'")
weather=str(input("Is it raining ? "))

if weather=="no":
    print("go outside")

else:
    have_umbrella=str(input("Do you have umbrella ? "))
    if have_umbrella=="yes":
        print("go outside")
    else:
        print("wait for some time")
        time.sleep(5)
        weather=input("is it still raining ? ")
        while weather=="yes":
            print("wait for some time ")
            time.sleep(5)
            weather=input("is it still raining")
        print(" go outside")