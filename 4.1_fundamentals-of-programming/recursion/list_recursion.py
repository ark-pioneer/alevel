def list_recursion(list, current_index=0):
    if current_index >= len(list):
        return
    print(list[current_index])
    list_recursion(list, current_index+1)
