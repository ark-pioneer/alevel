text = input("enter text to search: ")
query = input("enter search term: ")
i = 0
result = []
found = False
while i < len(text):
    j = 0
    while j < len(query):
        if query[j] != text[i+j]:
            found = False
            break
        found = True
        j+=1
    if found:
        result.append(i)
    i+=1

if found:
    print(result)
else:
    print("not found!")