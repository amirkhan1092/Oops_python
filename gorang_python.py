def fib(t):
    if t == 0 or t == 1:
        return 1
    else:
        return fib(t-1) + fib(t-2)

print(fib(4))