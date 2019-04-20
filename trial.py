import screen
import random
import sys




# Emoji from
#
# https://unicode.org/emoji/charts/emoji-list.html

emoji_list = [
    "\U0001F606", # laugh
    "\U0001F925", # pinocchio
    "\U0001F495" # two hearts
]

if len(sys.argv) < 2:
    size = 3
else:
    try:
        size = int(sys.argv[1])
    except ValueError:
        size = 3



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




def data(x):
    data_list = []
    for i in range(0, x):
        data_box = []
        for j in range(0, x):
            data_box.append(' ')
        data_list.append(data_box)
    return data

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




matrix = map(size)
x = 0
y = 0
row = 2 * x + 1
col = 2 * y + 1
matrix[row].pop(col)
matrix[row].insert(col, 'O')
change = "".join(matrix[row])
new_position = [row, col]
while True:
    key = screen.get_input()
    screen.print_on_screen("                                       You entered " + key, 0)

    if key == 'right':
        if new_position[1] < size * 2 - 1:
            matrix[row].pop(col)
            matrix[row].insert(col, ' ')
            col += 2
            new_position = [row, col]
            matrix[row].pop(col)
            matrix[row].insert(col, 'O')
            change = "".join(matrix[row])
        if new_position[1] >= size * 2 - 1:
            matrix[row].pop(size * 2 - 1)
            matrix[row].insert(size * 2 - 1, 'O')
            change = "".join(matrix[row])

    if key == 'left':
        if new_position[1] > 1:
            matrix[row].pop(col)
            matrix[row].insert(col, ' ')
            col -= 2
            new_position = [row, col]
            matrix[row].pop(col)
            matrix[row].insert(col, 'O')
            change = "".join(matrix[row])
        if new_position[1] <= 1:
            matrix[row].pop(1)
            matrix[row].insert(1, 'O')
            change = "".join(matrix[row])

    if key == 'down':
        if new_position[0] < size * 2 - 1:
            matrix[row].pop(col)
            matrix[row].insert(col, ' ')
            row += 2
            new_position = [row, col]
            matrix[row].pop(col)
            matrix[row].insert(col, 'O')
            change = "".join(matrix[row])
        if new_position[0] >= size * 2 - 1:
            matrix[size * 2 - 1].pop(col)
            matrix[size * 2 - 1].insert(col, 'O')
            change = "".join(matrix[row])

    if key == 'up':
        if new_position[0] > 1:
            matrix[row].pop(col)
            matrix[row].insert(col, ' ')
            row -= 2
            new_position = [row, col]
            matrix[row].pop(col)
            matrix[row].insert(col, 'O')
            change = "".join(matrix[row])
        if new_position[0] < 1:
            matrix[size * 2 - 1].pop(col)
            matrix[size * 2 - 1].insert(col, 'O')
            change = "".join(matrix[row])

    for r_number, r in enumerate(matrix):
        screen.print_on_screen("".join(r), r_number)

