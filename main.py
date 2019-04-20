draw_box = False

def draw_horizontal(x):
    line = " "
    for i in range(0, x):
        line += "-"" "
    if draw_box == True:
        print(line)
    return line


def draw_vertical(x):
    line = "|"
    for i in range(0, x):
        line += " ""|"
    if draw_box == True:
        print(line)
    return line

size = input("please give me the number:")
size = int(size)


print("draw_horizontal(size):" + draw_horizontal(size))
print("draw_horizontal(size):" + str(list(draw_horizontal(size))))



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


print("matrix:" + str(matrix))
matrix[0].pop(0)
matrix[0].insert(0, 'a')
print("matrix_changed" + str(matrix))
print("data:" + matrix[0][0])

def map(size):
    map_list = []
    for i in range(0, size * 2):
        if i % 2 == 0 or i == 0:
            map_box = list(draw_horizontal(size))
        if i % 2 == 1:
            map_box = list(draw_vertical(size))
        map_list.append(map_box)
    map_list.append(list(draw_horizontal(size)))

    return map_list

print("map:" + str(map(size)))

inbox = map(size)[0]
print("inbox:" + str(inbox))
print("inbox[0]:" + str(inbox[0]))

my_position = map(size)[0][0]
print("my_position:" + my_position)
data_position = data(size)[0][0]
print("data_position:" + data_position)

matrix = map(size)
x = 0
y = 0
data_position = data(size)[x][y]
a = 2 * x + 1
b = 2 * y + 1
my_position = matrix[a][b]
matrix[a].pop(b)
matrix[a].insert(b, 'O')
result = "".join(matrix[a])

print(result)
