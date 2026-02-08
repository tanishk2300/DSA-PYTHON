arr=[10,20,30,40,50]
print(arr)
target=int(input("enter target:"))
def binary_search(arr,target):
    low=0 # the low index.
    high=len(arr)-1 # high index.
    while low<=high: 
        mid=(low+high)//2 # finding the mid (half the unusual int in array ).
        if arr[mid]==target: # compairing the mid(arr) with target .
            return mid
        elif target<arr[mid]:
            high=mid-1
        else:
            low=mid+1
    return None
print(binary_search(arr,target))
        



