# if is the function to find the duplicate number in the array.
def find_duplicate(nums):  # function is created for find duplicate values.
    seen=set() # creates an empty set named seen.
    duplicate=set()# create an emty set named duplicate .
    for x in nums:
        if x in seen:
            duplicate.add(x)# if the number is duplicate then it will be added in duplicate set.
        else:
            seen.add(x)# otherwise the number will be added in seen set .
    return list(duplicate)

arr=[1,2,3,4,5,2]
print(find_duplicate(arr))#output=[2]