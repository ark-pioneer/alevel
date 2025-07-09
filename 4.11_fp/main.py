# # aggregating 
# nums = [4,9,3, 2]

# def add(list, total = 0):
#     if len(list) == 0:
#         return total
#     head = list[0]
#     tail = list[1:]
#     new_total = total + head
#     return add(tail, new_total)

# # print(add(nums))

# # def find_max(nums):
# #     m = nums[0]
# #     if nums[1] > m:
# #         m = nums[1]
# #     elif nums[2] > m:
# #         m = nums[2]
# #     return m

# # def find_max(nums, max = 0):
# #     if len(nums) == 0:
# #         return max
# #     head = nums[0]
# #     tail = nums[1:]
# #     if head > max:
# #         return find_max(tail, head)
# #     else:
# #         return find_max(tail, max)

# # print(find_max([4,8,2]))



# # def reverse(str, reversed_str=''):
# #     if len(str) == 0:
# #         return reversed_str
# #     head = str[0]
# #     tail = str[1:]
# #     return reverse(tail, head + reversed_str)

# # print(reverse("hello"))

# # def unique(list, unique_list):
# #     if len(list) == 0:
# #         return unique_list
# #     head = list[0]
# #     tail = list[1:]
# #     if head not in unique_list:
# #         return unique(tail, unique_list + [head])
# #     return unique(tail, unique_list)

# # print(unique([1,2,3,3,3,3,4,5], []))    

# # def count_cases(str, result):
# #     if len(str) == 0:
# #         return result
# #     head = str[0]
# #     tail = str[1:]
# #     if head == head.lower() and head.isalpha():
# #         updated_result = {
# #             "upper": result["upper"],
# #             "lower": result["lower"] + 1
# #         }
# #     elif head == head.upper() and head.isalpha():
# #         updated_result = {
# #             "upper": result["upper"] + 1,
# #             "lower": result["lower"]
# #         }
# #     else:
# #         updated_result = result
# #     return count_cases(tail, updated_result)

# # print(count_cases("The Quick Brown Fox", {"upper": 0, "lower": 0}))
    



# # def add(a, b):
# #     return a + b

# # print(reduce(add, [3, 9, 5, 3] , 0))

# # # 4. no side effects
# # # 3. no mutation
# # # 2. first class functions
# # # 1. higher order functions

# # # -> partial application of functions

# # # currying
# # def add(num):
# #     def temp(num2):
# #         return num + num2
# #     return temp

# # add5 = add(5)
# # print(add5(4))

# # ### partial application
# def product(a, b, c):
#     return a * b * c

# def partial(func, fixed_arg):
#     # return lambda a, b: func(fixed_arg, a, b)
#     def temp(a, b):
#         return func(fixed_arg, a, b)
#     return temp

# print(product(2,3,4))
# partial_product5 = partial(product, 5)
# partial_product9 = partial(product, 9)
# print(partial_product5(2, 3)) #? 30
# print(partial_product9(2, 3)) #? 54


  










# # # def sum(list, total=0):
# # #     if len(list) == 0:
# # #         return total
# # #     head = list[0]
# # #     tail = list[1:]
# # #     new_total = total + head
# # #     return sum(tail, new_total)

# # # # def sum(list, index=0, total=0):
# # # #     if index == len(list):
# # # #         return total
# # # #     new_total = total + list[index]
# # # #     next_index = index + 1
# # # #     return sum(list, next_index, new_total)

# # # print(sum(nums))

# # # # next: find the product of all the numbers.



# # # # 2 mapping.

# # # # new_nums = []
# # # # for num in nums:
# # # #     new_nums.append(num ** 2)
# # # # print(new_nums)

# # # # new_nums = [num**2 for num in nums]


# # # # filtering



# # # # 1. functional composition
# # # # 2. 


# # # # 1. pass functions around

# # # def add(num1, num2):
# # #     return num1 + num2
# # # def subtract(num1, num2):
# # #     return num1 - num2

# # # def apply(func, *args):
# # #     return func(*args)

# # # print(apply(add,7,8))
# # # print(apply(subtract,7,8))


# # # def find_max(nums):
# # #     m = nums[0]
# # #     if nums[1] > m:
# # #         m = nums[1]
# # #     elif nums[2] > m:
# # #         m = nums[2]
# # #     return m

# # # def find_max(nums, max = 0):
# # #     if len(nums) == 0:
# # #         return max
# # #     head = nums[0]
# # #     tail = nums[1:]
# # #     if head > max:
# # #         return find_max(tail, head)
# # #     else:
# # #         return find_max(tail, max)

# # # print(find_max([4,8,2]))


# # # nums = [8,4,1]

# # # def square(num):
# # #     return num ** 2

# # # mapping = map(square, nums)
# # # print((mapping.__next__()))
# # # print((mapping.__next__()))
# # # print((mapping.__next__()))
# # # print((mapping.__next__()))


# # immutability, pure functions, first class functions, higher order functions 


# # Why use functional programming?
# # - immutability
# # data does not change once it is declared.
# # Reduces errors from unexpected mutation
# # - pure functions
# # a function is pure when there are no side effects.
# # a side effect is when something happens in the function that is not the return value

# # def hello(word): #impure function
# #     print(word) # side effect
# #     return word + "!"

# # - first class functions
# # functions that can be passed around a program like a variable.
# # increased modularity and reuse small subroutines

# # def hello(word): #pure function
# #     return word + "!"

# # # new_hello = hello
# # # new_hello("jo")

# # def better_hello(func, smiley): # higher order function
# #     return func("Jo") + smiley

# # better_hello(hello, ":)") # Jo!:)


# # Practice
# # define two functions. One function is to be passed into the other.
# # a list of numbers, sum up all numbers in the list.




# # def add(a, b):
# #     return a + b
# # # add = lambda a,b: a + b
# def multiply(a, b):
#     return a * b
# # def halve(n):
# #     return n // 2

# def process_nums(func, start, list):
#     total = start
#     for num in list:
#         total = func(total, num)
#     return total

# # nums = [5,9,4]
# # # print(process_nums(add, nums))
# # print(process_nums(lambda a,b: a + b, nums))

# print(process_nums(multiply, 1, [2,3,2]))


# func = lambda a: a + ":)" # stores the func in a var
# print(func("hello ")) # calls the func

# print((lambda a: a + ":)")("hello ")) # "immediately invoked function expression"


# MAP
def square_all(nums, result):
    if len(nums) == 0:
        return result
    head = nums[0]
    tail = nums[1:]
    squared_num = head ** 2
    new_result = result + [squared_num]
    return square_all(tail, new_result)

print(square_all([4,5,6],[]))

def map(func, nums, result):
    if len(nums) == 0:
        return result
    head = nums[0]
    tail = nums[1:]
    return map(func, tail, result + [func(head)])

print(map(lambda x : x ** 2, [3,4,5], []))
print(map(lambda x : x ** 3, [3,4,5], []))

# def sum(nums, result=0):
#     if len(nums) == 0:
#         return result
#     head = nums[0]
#     tail = nums[1:]
#     return sum(tail, result + head)

# print(sum([14,9,2], []))
# from functools import reduce
# print(reduce(lambda a, b : a + b, [14, 9, 2], 8))

# print(square_all([4,8,2], [])) #> [16, 64, 4]
# print(list(map(lambda x : x **2, [4,8,2])))
# print(list(map(lambda x : x **2, [4,8,2])))

# def filter(func, nums, result):
#     if len(nums) == 0:
#         return result
#     head = nums[0]
#     tail = nums[1:]
#     if func(head):
#         return filter(func, tail, result + [head])
#     else:
#         return filter(func, tail, result)

# print(filter(lambda x : x > 5, [3,4,5,6], []))


# # ### partial application
# def product(a, b, c):
#     return a * b * c

# def partial(func, fixed_arg):
#     # return lambda a, b: func(fixed_arg, a, b)
#     def temp(a, b):
#         return func(a, b, fixed_arg)
#     return temp

# def concat(a, b, c):
#     return a + b + c

# add_smiley = partial(concat, " :)")
# print(add_smiley("hello ", "world"))
# print(add_smiley("hello ", "bek"))

# 1. One of the arguments is fixed.
# 2. Create a new function 
# 3. which uses the fixed argument

# print(product(2,3,4))
# partial_product_half = partial(product, 0.5)
# print(partial_product_half(4,3))
# partial_product9 = partial(product, 9)
# print(partial_product5(2, 3)) #? 30
# print(partial_product9(2, 3)) #? 54