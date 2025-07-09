# def bsearch(data, t, result):
#     midpoint = len(data) // 2 # low - high / 2
#     mid = data[midpoint]
#     result.append(mid)
#     if mid == t:
#         return result
#     elif len(data) == 1:
#         result.append(None)
#         return result
#     elif t > mid:
#         return bsearch(data[(midpoint+1) :], t, result)
#     elif t < mid:
#         return bsearch(data[:midpoint], t, result)       

# data = list(range(8))
# target = 7
# a = bsearch(data, target, [])
# print(a, len(a))

# import math
# print(math.log2(8))
import time

a = time.time()
for i in range(100000000):
    c = 0
b = time.time()
print(a, b, b-a)
