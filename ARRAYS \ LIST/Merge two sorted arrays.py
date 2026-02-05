
def merger(arr1,arr2): # here we create a function .
    arr=[]# it store the value of arr1 and arr2 .
    for i in arr1: 
        arr.append(i)# append the values in arr of arr1 .
    for i in arr2:
        arr.append(i)# append the values in arr of arr2 .
    return arr

arr1=[1,2,3,4,5]
arr2=[6,7,8,9]

result=merger(arr1,arr2)# function call 
print(result)
     




