# arr=[2,1,4,6,3,7,9,8,5] #for this arr it musst be false 
arr=[1,2,3] # this is sorted array 
is_sorted=True #We assume the array is sorted.
for i in range (len(arr)-1): # here it mean like length of array is 3 here and -1 = 2 'i' must give value only 1,2 becouse 3 is not included .
    if arr[i]>arr[i+1]:# here if the array values are greater then the next value then it goes to false and it break sudden .  
        is_sorted=False 
        break 
print(is_sorted)# output=True


