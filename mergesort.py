arr=[]
n=int(input("enter number of elements"))
for i in range(0,n):
    arr.append(int(input()))

def mergesort(l):
    
    if len(l)>1:
        mid=len(l)//2
        left=l[:mid]
        right=l[mid:]
        
        mergesort(left)
        mergesort(right)
        
        i=j=k=0
        temp=[]
        
        for i in range(0,len(left)):
            for j in range(0,len(right)):
                if left[i]>right[j]:
                    temp.append(right[j])
                else:
                    temp.append(left[i])
        
        while i < len(left): 
                    temp.append(left[i]) 
                    i+=1
                    k+=1
                  
        while j < len(right): 
                temp.append(right[j]) 
                j+=1
                k+=1        
                    
        print(temp)
        
        
def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 

        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 

        i = j = k = 0

        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1

        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1

        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1        
        
mergeSort(arr)
print(arr)