# x (int) : Value to take factorial of
def fact(x):
    total = 1
    for i in range(1, x + 1):
        total *= i
    return total
