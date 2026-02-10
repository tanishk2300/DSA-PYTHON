arr=[1,3,4,5,2]
# target=int(input("enter your target"))
def selection_sort(arr):
    n=len(arr)
    for i in range (n):
        # Assume the first element of the unsorted part is the minimum
        min_ind=i

        for j in range (i+1,n):
            if arr[j]<arr[min_ind]:
                min_ind=j
        arr[i],arr[min_ind]=arr[min_ind],arr[i]       
    return arr




print(selection_sort(arr))
                


