# The Fibonacci(N) function in Python generates a list containing a Fibonacci series of length N.
# the 1st and 2nd elements of the Fibonacci series are 0 and 1 respectively.

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 7
for i in range(0, n):
    print(fibonacci(i), end=" ")