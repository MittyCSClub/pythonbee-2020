# factorial: write a function `f(n: int) -> int` that returns n!
# (cannot use imports)

def f(n):
    return 1 if (n == 1 or n == 0) else n*f(n-1)
