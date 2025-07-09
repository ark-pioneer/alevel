data = [3,6,1,5]
swaps = False
i = 0
while True:
    if i == len(data)-1:
        if not swaps:
            break
        else:
            i = 0
            swaps = False
            continue
    else:
        if data[i] > data[i+1]:
            swaps = True
            temp = data[i]
            data[i] = data[i+1]
            data[i+1] = temp
    i+=1
print(data)
