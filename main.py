draw_box = False

def draw_horizontal(x):
    line = " "
    for i in range(0, x):
        line += "- "
    if draw_box == True:
        print(line)
    return line



def draw_vertical(x):
    line = "|"
    for i in range(0, x):
        line += " |"
    if draw_box == True:
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



matrix = data(size)


print(matrix)
matrix[0].pop(0)
matrix[0].insert(0, 'a')
print(matrix)
print("data:" + matrix[0][0])

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




