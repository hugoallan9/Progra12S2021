"""
f(x) = f(x-1) + f(x+1).
f(x+1) = f(x) - f(x-1) x>=2
f(x) = f(x-1) - f(x-2) x>=1

Input
The first line of input contains a single integer T denoting number of test cases.
The only line of each test case contains three integers: A, B and N, denoting f(1), f(2) and the query.

Example
Input:
2
10 17 3
23 17 3


Output:
7
1000000001
"""

def recursion(n, d):
    modulo = 10**9+ 7
    if n in d:
        return d[n]
    else:
        respuesta = (recursion(n-1,d) % modulo)  - (recursion(n-2,d) %modulo)
        d[n] = respuesta % modulo
        return respuesta % modulo

T = int(input())
for x in range(T):
    A,B,N = input().split()
    A, B, N = int(A), int(B), int(N)
    d = {1:A,2:B}
    print(recursion(N,d))

