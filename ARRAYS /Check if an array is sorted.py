# arr=[2,1,4,6,3,7,9,8,5] #for this arr it musst be false 
arr=[1,2,3] # this is sorted array 
is_sorted=True #We assume the array is sorted.
for i in range (len(arr)-1):
    if arr[i]>arr[i+1]:# here if the array values are 
        is_sorted=False# if the 
        break 
print(is_sorted)


