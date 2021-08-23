# n! = n*(n-1)*(n-2)****1 = n * (n-1)!

def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))

def factorial_ciclo(n):
    producto = 1
    for x in range(1,n+1):
        producto *= x
    return producto

print(factorial_ciclo(5))