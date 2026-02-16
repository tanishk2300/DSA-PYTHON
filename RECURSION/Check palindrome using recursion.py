a=121

def palindrom_get(n,rev=0): 
    if n==0:
        return rev 
    return palindrom_get(n//10 ,rev * 10 +n%10)

def show_palindrom(n):
    return n == palindrom_get(n)

print(show_palindrom(a))