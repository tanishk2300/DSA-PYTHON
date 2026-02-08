arr=[10,20,30,40,50]
print(arr)
target=int(input("enter target:"))
def binary_search(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif target<arr[mid]:
            high=mid-1
        else:
            low=mid+1
    return None
print(binary_search(arr,target))
        



