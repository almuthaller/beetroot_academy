# Calculating factorials from an iterative and a recursive approach


def iterative_factorial(num):
    fac = 1
    while num >= 1:
        fac *= num
        num -= 1

    return fac


def recursive_factorial(num):
    if num == 1:
        return 1
    else:
        return num * recursive_factorial(num - 1)


print(iterative_factorial(10))
print(recursive_factorial(10))
