ages=[13,15,16,16,19,20,20,21,22,22,25,25,25,25,30,33,33,35,35,35,36,40,45,52,70]
repeat=[]

mean=0

for item in range(0,len(ages)):
    mean=mean+ages[item]

mean=mean/(len(ages))

print("Mean is ",mean)
    
median=ages[int((len(ages)+1)/2)]

print("Median is ",median)

for each in range(0,len(ages)):
    for item in range(0,len(ages)):
        
