
def f(y):
    global x
    x = 1
    x +=1
    print(x)

global x
x = 5
print(x)
f(x)
print(x)