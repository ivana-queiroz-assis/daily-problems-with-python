#Implement the function fib(n), which returns the nth number in the Fibonacci sequence, using only O(1) space

def fib(n: int):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

def fib_better_perfomance(n: int):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b
print(fib_better_perfomance(7))