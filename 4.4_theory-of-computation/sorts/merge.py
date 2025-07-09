nums = [5, 9, 4, 1, 0,3,2,6]
#divide
#def bisect(list):
#    if len(list) == 1:
#        return list
#    else:
#        return bisect([list[:len(list)/2], list[len(list)/2:]])
def merge(sub_lists):
    if len(sub_lists) == 1:
        return sub_lists[0]

print(merge(nums))
