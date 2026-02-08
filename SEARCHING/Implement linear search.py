arr=[10,30,50,60,44]
print(arr)
target=int(input("target:")) # here we take the target as an input.
def linera_search(arr,target):# this function is for linear search.
    for i in range(len(arr)): # cheak int from 0 index to n 
        if arr[i]==target:# if target and index of the number in array are equal then , 
            return i #return to index immediately,and stop.
    return None # target does not exist in array.
    
print(linera_search(arr,target))


