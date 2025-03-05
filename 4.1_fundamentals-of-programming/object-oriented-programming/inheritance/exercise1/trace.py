def procedure(num):
    str_a = str(num)
    result = ""
    count = 0
    while count < len(str(str_a)):
        int_a = int(str_a[count])
        for i in range(int_a):
            result += str_a[count]
        count += 1
    print(result)

procedure(32)
procedure(102)

# Trace the following values for the above function calls
# count  |  int_a  |  str_a[count]  |  result  |  output
