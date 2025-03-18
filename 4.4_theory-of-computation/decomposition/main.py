
map = [
    ['t', 't', 'p'],
    ['t', 't', 't'],
    ['-', 'p', 'p']
]

# def find_trees(map, row, col):
#     tree_count = 0
#     if row + 1 < len(map) and map[row+1][col] == 't':
#         tree_count += 1
#     if col -1 >= 0 and map[row][col-1]  == 't':
#         tree_count += 1
#     if col +1 < len(map) and map[row][col+1] == 't':
#         tree_count += 1
#     if row -1 >= 0 and map[row-1][col] == 't':
#         tree_count += 1
#     return tree_count

# i = 0
# total = 0
# while i < len(map):
#     j = 0
#     while j < len(map[i]):
#         if map[i][j] == "p":
#             trees = find_trees(map, i, j)
#             total += trees
#             print("# num trees around person at row", i, "col", j, ":", trees)
#         j+=1
#     i+=1
# print("total trees next to people:", total)

def next_to_person(map, row, col):
    if row + 1 < len(map) and map[row+1][col] == 'p':
        return True
    if col -1 >= 0 and map[row][col-1]  == 'p':
        return True
    if col +1 < len(map) and map[row][col+1] == 'p':
        return True
    if row -1 >= 0 and map[row-1][col] == 'p':
        return True

i = 0
tree_count = 0
while i < len(map):
    j = 0
    while j < len(map[i]):
        if map[i][j] == "t":
            if next_to_person(map, i, j):
                tree_count += 1
        j+=1
    i+=1
print("total trees next to people:", tree_count)


# How many trees surround the person?
# process:
# - simplify problem
# - identify input and output.

# simplify problem: 1st approach 
# - person is given at row 1, col 0
# - check same row, different colum: the next one
# - the one before
# - then check same column, row -1, row +1

# row = 2
# col = 1
# tree_count = 0
# if col-1 >= 0 and map[row][col-1] == "t":
#     tree_count += 1

# if col+1 < len(map[row]) and map[row][col+1] == "t":
#     tree_count +=1

# if row-1 >= 0 and map[row-1][col] == "t":
#     tree_count += 1

# if row+1 < len(map) and map[row+1][col] == "t":
#     tree_count +=1


# row = 1
# col = 0
# tree_count = 0
# if map[row-1][col] == "t":
#     tree_count += 1

# if map[row+1][col] == "t":
#     tree_count +=1

# print(tree_count)

# then
# - check col
# - then find position of person.
# - ensure if out of bounds, ignore
# - then more people, dont double count, so look at every tree.
# i1 = 0
# while i1 < len(map):
#     i2 = 0
#     while i2 < len(map[i1]):
#         if map[i1][i2] == 't':
#             increment count if person next to it.



# What is decomposition?

map = [
    ['t', 'p', '-'],
    ['t', 't', '-'],
    ['-', 't', '-']
]

tree_count = 0
row = 0
col = 1

# top_row = map[row-1]
# middle_row = map[row]
# bottom_row = map[row+1]

if row-1 >= 0 and map[row-1][col] == 't':
    tree_count +=1
if map[row][col-1] == 't':
    tree_count += 1
if map[row][col+1] == 't':
    tree_count += 1
# if the index of the row below p is out of bounds, stop
if row + 1 < len(map) and map[row+1][col] == 't':
    tree_count += 1

print(tree_count)
