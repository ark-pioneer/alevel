# open
# read
# close

with open("data.txt", "r") as f:
    while True:
        line = f.readline()
        if line == "":
            break
        print(line)
# write the first word of each line, if there's data, into a new file.
# each word should be on a separate line.

# with open("first_words", "w") as new_file:
#     with open("data.txt", "r") as f:
#         while True:
#             line = f.readline()
#             if line == "":
#                 break
#             split_line = line.split(" ")
#             if len(split_line) > 0:
#                 new_file.write(split_line[0])

with open("AQA-7517-SSV.csv", "r") as f:
    data = f.read()
    print(data)
    























# with open("data.txt", "r") as f:
#     while True:
#         line = f.readline()
#         print(repr(line))
#         if line == "":
#             break
