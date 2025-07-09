# data = "Hello, everyone\n".encode("utf-8")
# data += "Good luck for your exams! :)".encode("utf-8")
# data += bytes([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
# print(data)
# with open("message.bin", "wb") as file:
#     file.write(data)

# with open("message.bin", "rb") as file:
#     while True:
#         byte = file.read(1)
#         if not byte:
#             break
#         print(byte.decode("utf-8"))




# 1. string -> binary string
# 2. write binary string to file
# 3. read binary string from file
# 4. binary string -> string

message = "Hello, everyone\nGood luck for your exams! :)"
data = message.encode("utf-8")
with open("message.bin", "wb") as file:
    file.write(data)

with open("message.bin", "rb") as file: 
    while True:
        byte = file.read(3)
        print(repr(byte))
        print(byte, not byte, byte == False, byte == b"")
        if not byte: # end of file, no more chunks
            break
        print(byte.decode("utf-8"))



numbers = ["cat", "dog", "mouse", "hamster"]

# count how many items in the list have more than 3 characters

for char in "hello":
    print(char)