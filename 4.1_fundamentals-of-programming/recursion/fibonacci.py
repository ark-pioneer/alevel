def fibonacci(num):
    if num <= 2:
        return num-1
    else:
        return fibonacci(num-2) + fibonacci(num-1)