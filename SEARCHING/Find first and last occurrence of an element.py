arr=[1,2,3,4,5,5,5,6,7]
print(arr)
target=int(input("enter your target:"))
def first_occurrence(arr,target):
    low, high=0,len(arr)-1 
    #low → start of array,  
    #high → end of array,
    result=-1 
    #result → stores answer (−1 means “not found yet”)
    while low<=high: #Keep searching as long as there is a valid search range.
        mid=(low+high)//2
        # Target found.
        if arr[mid]==target:
        # Store index in result
            result=mid
        # Move left to check if target appears earlier.
            high=mid-1 # move left.
        elif arr[mid]<target: # target is greater.
            low=mid+1 # Target is on the right side. 
        else: #Target is smaller
            high=mid-1 # Target is on the left side.
        return result

def last_occurrence(arr,target):
    # Same meaning as before.
    low , high=0,len(arr)-1
    result=-1
    while low<=high: #
        mid=(low+high)//2
        if arr[mid]==target:
            result=mid
            low=mid+1 # Move right to find later occurrence.
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1 # left side.
    return result

print("First index:", first_occurrence(arr, target))
print("Last index:", last_occurrence(arr, target))
