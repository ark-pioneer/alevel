data = bytes([10, 20, 30, 40, 50])  # a sequence of raw bytes

with open("data.bin", "wb") as file:
    file.write(data)


text = "Hello"
data = text.encode("utf-8")  # convert string → bytes

with open("message.bin", "wb") as file:
    file.write(data)

with open("data.bin", "rb") as file:
    content = file.read()

print(content)  # e.g. b'\n\x14\x1e(2'

with open("message.bin", "rb") as file:
    data = file.read()

text = data.decode("utf-8")
print(text)


with open("image.jpg", "rb") as file: 
    while True:
        # read a chunk of the file (e.g. 1024 bytes)
        chunk = file.read(1024)
        if not chunk:
            # if chunk is empty, we've reached end of the file
            break
        # do something with chunk

with open("data.bin", "rb") as file:
    while True:
        byte = file.read(1)
        if not byte:
            break
        print(byte)

