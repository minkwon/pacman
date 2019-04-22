import screen
import random
import sys
import sound

# Emoji from
#
# https://unicode.org/emoji/charts/emoji-list.html

emoji_list = [
    "\U0001F606",  # laugh
    "\U0001F925",  # pinocchio
    "\U0001F495",  # two hearts
    "\U0001F47B"  # ghost
]

if len(sys.argv) < 2:
    size = 3
else:
    try:
        size = int(sys.argv[1])
    except ValueError:
        size = 3


def data(size):
    data = []
    for i in range(0, size):
        my_list = []
        for j in range(0, size):
            my_list.append('  ')
        data.append(my_list)

    return data

matrix = data(size)
matrix[0].pop(0)
matrix[0].insert(0, 'a')
print(matrix)

draw_box = False
def draw_vertical(x):
    vertical_list = []
    vertical_list.append('|')
    for i in range(0, x):
        vertical_list.append('  ')
        vertical_list.append('|')
    if draw_box == True:
        print(vertical_list)
    return vertical_list

print(draw_vertical(size))

def draw_horizontal(x):
    horizontal_list = []
    horizontal_list.append(' ')
    for i in range(0, x):
        horizontal_list.append('--')
        horizontal_list.append(' ')
    if draw_box == True:
        print(horizontal_list)
    return horizontal_list

print(draw_horizontal(size))


def map_list(size):
    map_list = []
    for i in range(0, size * 2):
        if i % 2 == 0 or i == 0:
            map_box = draw_horizontal(size)
        if i % 2 == 1:
            map_box = draw_vertical(size)
        map_list.append(map_box)
    map_list.append(draw_horizontal(size))

    return map_list


map_line = map_list(size)


def character_on_map():
    for i in range(0, len(matrix[0])):
            for j in range(0, len(matrix[0])):
                map_line[2* j + 1].pop(2 * i + 1)
                value = matrix[j].pop(i)
                matrix[j].insert(i, ' ')
                map_line[2 * j + 1].insert(2 * i + 1, value)
    return map_line




# data = data(size)
# character = emoji_list[3]
# x = 0
# y = 0
# row = 2 * x + 1
# col = 2 * y + 1
# data[row].pop(col)
# data[row].insert(col, character)
# change = "".join(data[row])
# new_position = [row, col]
character = emoji_list[3]
square = character_on_map()
x = 0
y = 0
row = 2 * x + 1
col = 2 * y + 1
square[row].pop(col)
square[row].insert(col, character)
change = "".join(square[row])
new_position = [row, col]
while True:
    key = screen.get_input()
    screen.print_on_screen("                                       You entered " + key, 0)

    if key == 'right':
        if new_position[1] < size * 2 - 1:
            square[row].pop(col)
            square[row].insert(col, '  ')
            col += 2
            new_position = [row, col]
            square[row].pop(col)
            square[row].insert(col, character)
            change = "".join(square[row])
        else:
            pass





    if key == 'left':
        if new_position[1] > 1:
            square[row].pop(col)
            square[row].insert(col, '  ')
            col -= 2
            new_position = [row, col]
            square[row].pop(col)
            square[row].insert(col, character)
            change = "".join(square[row])

    if key == 'down':
        if new_position[0] < size * 2 - 1:
            square[row].pop(col)
            square[row].insert(col, '  ')
            row += 2
            new_position = [row, col]
            square[row].pop(col)
            square[row].insert(col, character)
            change = "".join(square[row])

    if key == 'up':
        if new_position[0] > 1:
            square[row].pop(col)
            square[row].insert(col, '  ')
            row -= 2
            new_position = [row, col]
            square[row].pop(col)
            square[row].insert(col, character)
            change = "".join(square[row])

    for r_number, r in enumerate(square):
        screen.print_on_screen("".join(r), r_number)

