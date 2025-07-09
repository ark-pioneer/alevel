# Iteration

# Count Controlled iteration
# while loop

# scenario: print Hello 5 times

# h = 9
# while h < 14:
#     print(h, "Hello")
#     h+=1


# scenario: print all items in a list or a string
# numbers = [7, 11, 93]
# i = 0
# while i < len(numbers):
#     print(i, numbers[i])
#     i+=1

veg = "chilli"
# i = 0 # start
# while i < len(veg): # 6 stop
#     print(i, veg[i])
#     i += 1 # step

# go backwards and print each character in veg
# start 5
# i = 5
# while i >= 0:
#     print(i, veg[i])
#     i -= 1

# count controlled iteration
# for loops

#scenario: print hello 5 times.

for i in range(5):  # with 1 arg, default START = 0, STEP = 1
    print("hello")

for i in range(4, 9): # with 2 args, default STEP = 1
    print("hello")

for i in range(4, 14, 2): # with 3 args, all explicitly defined START STOP STEP
    print(i, "hello") # 4, 6, 8, 10, 12

# scenario: print characters from a string
country = "england"
for i in country:
    print(i)

