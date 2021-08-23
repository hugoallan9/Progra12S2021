
def func_a():
    print('dentro de la función a')

def func_b(y):
    print('dentro de la función b')
    return y

def func_c(z):
    print('dentro de la función c')
    return z()

print(func_a())
print( 5 + func_b(2))
print(func_c(func_a))
