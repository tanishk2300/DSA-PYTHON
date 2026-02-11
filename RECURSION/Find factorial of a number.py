target=5
#Recursion is when a function calls itself.
def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)#It multiplies n with factorial of (n - 1) = 5 * 4 * 3 * 2 * 1
print(factorial(target))


