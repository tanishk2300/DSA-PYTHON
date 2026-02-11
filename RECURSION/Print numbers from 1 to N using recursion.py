def recursion(n):

    if n==0 :# Base case
        return
    recursion(n-1) # Recursive call
    print(n)
n=5
print(recursion(10))