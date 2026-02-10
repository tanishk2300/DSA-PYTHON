arr=[1,4,6,7,45,56,67]

def merge_sort(arr):
    if len(arr)<=1:#here len of arr must less and equal to 1.
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])#Left part ko recursively sort karo.
    right=merge_sort(arr[mid:])#right part ko recursively sort karo.
    return merge(left,right)

def merge(left,right):
    result=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:#Left ka element chhota ya barabar hai?
            result.append(left[i])#result m daldo.
            i+=1
        else:
            result.append(right[j])
            j+=1
        result.extend(left[i:])#Agar left me kuch bach gaya ho.
        result.extend(right[j:])#Agar right me kuch bach gaya ho.
        return result
print(merge_sort(arr))


