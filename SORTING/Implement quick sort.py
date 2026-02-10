arr=[3,68,22,54,33,76,45]
def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[-1]
    left=[]
    right=[]
    for i in range (len(arr)-1):
        if arr[i]<=pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quick_sort(left) + [pivot] + quick_sort(right)
print(quick_sort(arr))
