arr=[1,2,3,4,7,5,6]

def bubble_sort(arr):
    n=len(arr)
    for i in range (n):
        swapped=False
        for j in range (0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
            swapped=True
            if not swapped:
                    break
    return arr
print(bubble_sort(arr))

    
            
