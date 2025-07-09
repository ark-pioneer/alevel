data = input("enter data: ")

try:
    number = int(data)
    print(number)
except ValueError as abc:
    print(abc)
    print("not possible")


