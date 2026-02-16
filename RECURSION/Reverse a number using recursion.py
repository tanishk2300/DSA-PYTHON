a=1234

def get_reverse(n,rev=0):
    if n==0:
        return rev 
    
    return get_reverse(n//10,rev*10 + n%10)

'''
-----------------
Step 1
----------------
n = 1234
rev = 0
n % 10 = 4   (last digit)
rev * 10 = 0
rev * 10 + n % 10 = 4
______________
Step 2
--------------
n = 123
rev = 4
n % 10 = 3
rev * 10 = 40
rev * 10 + n % 10 = 43
----- so,on ------

here, 
n//10 =remove to last digit.
rev * 10 + n % 10=This builds the reversed number.

'''

print(get_reverse(a))