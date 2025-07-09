# # 1 groups similar data and methods together.
# # 2 limiting access(scope) to those data and methods.
# # class

# class Pencil():
#     def __init__(self, type):
#         self.type = type

# p = Pencil("2B")









# type1 = "dog"
# hunger1 = 10
# type2 = "cat"
# hunger2 = 4

# def update_hunger1(val):
#     hunger1 += val

# def update_hunger2(val):
#     hunger2 += val






# class Animal():
#     def __init__(self, type, hunger):
#         self.type = type
#         self.hunger = hunger

#     def update_hunger(self, val):
#         self.hunger += val

# animal1 = Animal("dog", 10)
# animal2 = Animal("cat", 4)


# OUTPUT "The first few prime numbers are:"

# FOR Count1  2 TO 50 DO
#   Count2  2
#   Prime  "Yes"
#   WHILE Count2 * Count2 <= Count1 DO
#     IF (Count1 MOD Count2 = 0) THEN
#       Prime  "No"
#     ENDIF
#     Count2  Count2 + 1
#   ENDWHILE
#   IF Prime = "Yes" THEN
#     OUTPUT Count1
#   ENDIF
# ENDFOR

isbn = []
for count in range (0, 13):
    print("please enter next digit of ISBN: ")
    isbn.append(int(input()))

calculated_digit = 0
count = 0
while count < 12:
    calculated_digit += isbn[count]
    count += 1
    calculated_digit += isbn[count] * 3
    count += 1

while calculated_digit >= 10:
    calculated_digit -= 10
calculated_digit = 10 - calculated_digit
if calculated_digit == 10:
    calculated_digit = 0
if calculated_digit == isbn[12]:
    print("valid isbn")
else:
    print("invalid isbn")