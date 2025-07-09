# # Write a program that gets the user to enter a string. It should keep getting the user to enter a string until they enter a valid string. Each time they enter a string an appropriate message should be displayed telling them whether the string they entered is valid or not.

# # For a string to be valid:

# # •   it must be between five and seven characters in length (inclusive)

# # •   it must consist only of uppercase letters

# # •   it must contain only unique characters (i.e. no character appears in the string more than once)

# # •   the sum of the ASCII codes of the characters in the string must be between 420 and 600 (inclusive).

# def unique(data):
#     return len([i for i in data if data.count(i) > 1]) == 0

# def sum_ascii(data):
#     return sum(ord(i) for i in data)

# while True:
#     print("enter text: ")
#     data = input("> ")
#     if 5 > len(data) or len(data) > 7 or not unique(data) or data != data.upper() or 420 > sum_ascii(data) or sum_ascii(data) > 600:
#         print("invalid")
#     else:
#         print("valid")
#         break

person = ["adwa", 100, True]
person[1]
person[2]
person[0] = "ava"
print(person)
# title: ranges - sublists and substrings

numbers =  [4, 6, 7, 8]
print(numbers[0:2])
word = "microphone" # just get "crop"
word2 = "speaker"
# task: get speakerphone
print(word2 + word[5:10])

# # index = 1
# # while index <= 5:
# #     print(index)
# #     index += 1
# # Print out the numbers 0 to 10.
# index = 0
# while index <= 10:
#     print(index)
#     index += 1

# extension: Print out the numbers 10 down to 0.
# index = 10
# while index >= 0:
#     print(index)
#     index -= 1

numbers =  [4, 6, 7, 8]
# print(numbers[0])
# print(numbers[1])
# print(numbers[2])
# print(numbers[3])
# numbers =  [4, 6, 7, 8]
# index = 0
# while index <= 3:
#     print(numbers[index])
#     index += 1

letters = ["c", "j", "k", "l"]
index = 0
while index <= 3:
    print(letters[index])
    index += 1













# # Title: Lists with Loops
# items = ["Slovakia", "Somalia", "Iran", "China", "India"]
# # Print out each item one at a time
# print(items[0])
# print(items[1])
# print(items[2])
# print(items[3])
# print(items[4])
# # Start = 0
# # Stop = 4
# # Step = +1

# # USING A WHILE LOOP
# items = ["Slovakia", "Somalia", "Iran", "China", "India"]
# counter = 0
# while counter <= 4:
#     print(items[counter])
#     counter += 1

# numbers = [4, 7, 1, 8, 2, 11, 91]

# i = 0
# while i <= 6:
#     if numbers[i] > 5:
#         print(numbers[i])
#     i += 1

# cities = ["London", "Berlin", "Dubai"]
# x = 0
# while x < len(cities):
#     if len(cities[x]) > 5:
#         print(cities[x])
#     x += 1


