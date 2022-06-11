# Рекусрсия прохода по всем ветвям начиная с корня
# 2*i и 2*i+1
def step_to_leaf(index,way):
    global wood
    null = None
    lenght = len(wood)
    
    if 2*index-1 >= lenght:
        print(way) 
        return way
    if wood[2*index-1] == None and wood[2*index] == None:
        print(way)
        return way

    if wood[2*index-1] != None:
        way.append(wood[2*index-1])
        wood[2*index-1] = null
        step_to_leaf(index+1,way.copy())
        way.pop()
    if wood[2*index] != None:
        way.append(wood[2*index])
        wood[2*index] = null

        step_to_leaf(index+2,way.copy())
    



null = None
wood = [1,-3,6,null,4,101,null,7,null]
wood1 = wood.copy()
if len(wood) > 0:
    way = [wood[0]]
else:
    print("Нет ветвей")
    exit()

step_to_leaf(1,way)