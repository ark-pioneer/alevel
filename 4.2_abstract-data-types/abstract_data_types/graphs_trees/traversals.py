tree = {
    "root": 0,
    "values": ["john", "gary", "ella", "alex", "chris"],
    "left":  [2, 0, 3, 0, 0],
    "right": [1, 0, 0, 4, 0]
}

def traverse(tree, index, visited):
    if tree["left"][index] != 0:
        traverse(tree,  tree["left"][index], visited)
        
    visited.append(tree["values"][index])
    
    if tree["right"][index] != 0:
        traverse(tree,  tree["right"][index], visited)

    if len(visited) == len(tree["values"]):
        return visited

def find_place(value, tree, index, new_index):
    if value < tree["values"][index]:
        if tree["left"][index] == 0:
            tree["left"][index] = new_index
        else:
            find_place(value, tree, tree["left"][index], new_index)
    else:
        if tree["right"][index] == 0:
            tree["right"][index] = new_index
        else:
            find_place(value, tree, tree["right"][index], new_index)
            
def insert(tree, value, index=0):
    tree["values"].append(value)
    tree["left"].append(0)
    tree["right"].append(0)
    
    new_index = len(tree["values"])-1
    
    find_place(value, tree, index, new_index)

insert(tree, "fred")

print(traverse(tree, tree["root"], []))