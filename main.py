

def draw_horizontal(x):
    line = " "
    for i in range(0, x):
        line += "- "
    print(line)
    return line



def draw_vertical(x):
    line = "|"
    for i in range(0, x):
        line += " |"
    print(line)
    return line

size = input("please give me the number:")
size = int(size)

for i in range(0,size):
    draw_horizontal(size)
    draw_vertical(size)
draw_horizontal(size)



def data(size):
    data = []
    for i in range(0,size):
        my_list = []
        for j in range(0,size):
            my_list.append(' ')
        data.append(my_list)

    return data



list = data(size)


print(list)
list.pop([0][0])
list.insert([0][0], 'a')
print(list)
print("data:" + list[0][0])

def map(size):
    map_list = []
    for i in range(0, size * 2):
        if i % 2 == 0 or i == 0:
            map_box = [draw_horizontal(size)]
        if i % 2 == 1:
            map_box = [draw_vertical(size)]
        map_list.append(map_box)
    map_list.append([draw_horizontal(size)])

    return map_list

print(map(size))




