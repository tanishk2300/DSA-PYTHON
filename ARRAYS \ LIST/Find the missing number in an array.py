
def find_missing(arr):# here we create a function 
    n=len(arr)+1# we find length here .
    total = n * (n + 1) // 2 # this help to find the total of number from start of a perticular digit . 
    return (total-sum(arr))# we subtract the length and the sum of arr to get the missign number in the arr.
   
arr=[1,2,3,5,6,7]#this is array where a digit is missing .
print(find_missing(arr))#output=4