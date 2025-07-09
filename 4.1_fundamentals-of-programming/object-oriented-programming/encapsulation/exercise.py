def smiley():
    return ":)"

def happy():
    return ":D"

def sad():
    return ":("

def smilify(text):
    return text + smiley()

def happify(text):
    return text + happy()

def sadify(text):
    return text + sad()

# test with examples:
print(happify("Hello!"))
print(sad())
