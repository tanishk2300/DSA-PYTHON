tar=18

def square(tar):
    low=0
    high=tar
    ans=0
    while low<=high:
        mid=(low+high)//2
        if mid*mid==tar:
            return mid
        elif mid*mid<tar:
            ans=mid
            low=mid+1
        else:
            high=mid-1
    return ans
print(square(tar))
        


# import math
# tar=17
# def square(tar):
#     a=math.sqrt(tar)
#     b=int(a)
#     return b
# print(square(tar))

# here the ans you get is like in integer not in float so the ans must in approximation .