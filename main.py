

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

print("data:" + data(size)[0][0])

def map(size):
    for i in range(0, size):
        map_list = []
        for j in range(0, size):
            map_box = []
            if i % 2 == 0 or i == 0:
                map_box.append(draw_horizontal(size))
            if i % 2 == 1:
                map_box.append(draw_vertical(size))
        map_list.append(map_box)

    return map_list





