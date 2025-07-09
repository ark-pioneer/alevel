# joseph's definition: 
# An assortment of data where the data within, i don't know how to say it, but using the key to access it

# The definition:
# - It is a key-value data store. This means that data is stored using keys. 
# - Each key in the structure points to the data it represents.
# - keys usually are strings, but are UNIQUE

# eg

table1 = {
    "type": "student desk",
    "size": "large",
    "chairs": 2
}

a = 1
scores = {
    "a": a,
    "b": 9
}

# get data from the dictionary using the key
print(table1["size"])

# change/write data to the dictionary
table1["material"] = "wood"
table1["chairs"] = 4
print(table1)


