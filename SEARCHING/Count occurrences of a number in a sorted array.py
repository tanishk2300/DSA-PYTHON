arr=[1,2,3,4,5,5,5,6,7]
target=int(input("enter target"))
def occurrences_count(arr,target):
    count=0
    for i in range(len(arr)-1):
        if target==arr[i]:
            count+=1
    return count
print(occurrences_count(arr,target))

            



