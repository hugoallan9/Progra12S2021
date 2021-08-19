# f_n = f_{n-1} + f_{n-2} para n >= 2 f_1 = f_0 = 1

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
#21
print(fibonacci(8))

def fibonacci2(n):
    acumuladora1 = 0
    acumuladora2 = 1
    for x in range(1,n+1):
        acumuladora2, acumuladora1 = acumuladora1 + acumuladora2, acumuladora2
    return acumuladora2

print(fibonacci2(8))