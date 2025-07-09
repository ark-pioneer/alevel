# # dictionaries are structures that store data as key, value pairs

# student = {
#     "name": "Joseph",
#     "age": 15
# }

# print(student)
# print(student["name"])

# student["email"] = "test@ark.com"
# student["age"] = 10

# print(student)

# # what will happen if this next line runs?
# # print(student["year_group"])




# Dictionaries
# this is a data structure. 

# lists are also a data structure.
# We use lists to store data organised by index. (We start at index 0)
# dynamic: we can change the size of the structure. (as opposed to static)
# they can store multiple types of data
# access items directly: using index O(1) as opposed O(n)
# memory allocation for the structure can be contiguous or non-contiguous

# dictionaries
# We use lists to store data by key and value pairs
# dynamic
# store multiple types of data
# access items directly: using a key
# memory allocation for the structure can be contiguous or non-contiguous

classroom = {
    "num_chairs": 66,
    "num_students": 5
}

# Dictionaries are in general more structured than lists. The fact that we use keys means that the data
# is stored with more information about its intended use.

# Operation 1: reading data from a dictionary
print(classroom["num_chairs"])

# MWB task:
# create a dictionary that represents homework.
# - due_date
# - subject
hw = {
    "due_date": "yesterday"
}
print(hw["due_date"])


# Operatoin 2: add to or change data in a dictionary
hw["set_date"] = "today"

print(hw)

