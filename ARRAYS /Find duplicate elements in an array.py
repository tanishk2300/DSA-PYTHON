# if is the function to find the duplicate number in the array.
def find_duplicate(nums):
    seen=set()
    duplicate=set()
    for x in nums:
        if x in seen:
            duplicate.add(x)
        else:
            seen.add(x)
    return list(duplicate)

arr=[1,2,3,4,5,2]
print(find_duplicate(arr))#output=[2]