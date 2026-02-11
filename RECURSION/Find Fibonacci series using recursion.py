target=7
def fibonacchi(n):
    if n==0:#Jab number khatam ho jaye, stop recursion.
        return 0
    if n==1:
        return 1
    return fibonacchi(n-1)+fibonacchi(n-2)

def get_fibo(n):
    for i in range(n):
        print(fibonacchi(i),end=" ")
    return None


print(get_fibo(target))