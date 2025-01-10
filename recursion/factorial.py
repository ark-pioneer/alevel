def factorial(n, acc = 1):
    if n <= 1:
        return acc
    acc *= n
    return factorial(n-1, acc)

