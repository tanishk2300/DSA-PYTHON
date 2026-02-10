arr=[2,3,44,65,36,77]
def insertion_sort(arr):
    n=len(arr)
    
    for i in range(1,n):
        key=arr[i]#yaha value of i put hogi key unhe sort karega,This is the element to be inserted into correct position .
        j=i-1
        while j >=0 and arr[j]>key :
            arr[j+1]=arr[j]#Makes space for key.
            j-=1#Keep checking left side.
        arr[j+1]=key #Put key in correct position.

    return arr
print(insertion_sort(arr))