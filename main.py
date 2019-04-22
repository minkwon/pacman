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

empty_space = '  '


if len(sys.argv) < 2:
    size = 3
else:
    try:
        size = int(sys.argv[1])
    except ValueError:
        size = 3

"""
    This method returns float between 0 and 1 excluding 1.
"""
def get_percentage():
    return random.uniform(0, 1)


draw_box = False
def draw_vertical(x):
    vertical_list = []
    vertical_list.append('|')
    for i in range(0, x):
        vertical_list.append(empty_space)
        vertical_list.append('|')
    if draw_box == True:
        print(vertical_list)
    return vertical_list


def draw_horizontal(x):
    horizontal_list = []
    horizontal_list.append(' ')
    for i in range(0, x):
        horizontal_list.append('--')
        horizontal_list.append(' ')
    if draw_box == True:
        print(horizontal_list)
    return horizontal_list



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


def data(size):
    data = []
    for i in range(0, size):
        my_list = []
        for j in range(0, size):
            if get_percentage() < 0.1:
                my_list.append(emoji_list[2])
            else:
                my_list.append(empty_space)

        data.append(my_list)

    return data



map_line = map_list(size)
matrix = data(size)





def character_on_map():
    for i in range(0, len(matrix[0])):
            for j in range(0, len(matrix[0])):
                map_line[2* j + 1].pop(2 * i + 1)
                value = matrix[j].pop(i)
                matrix[j].insert(i, empty_space)
                map_line[2 * j + 1].insert(2 * i + 1, value)
    return map_line


def right_side_checking():
    if square[row][col + 2] == empty_space:
        return '1'
    else:
        return '0'


def left_side_checking():
    if square[row][col - 2] == empty_space:
        return '1'
    else:
        return '0'


def down_side_checking():
    if square[row + 2][col] == empty_space:
        return '1'
    else:
         return '0'


def up_side_checking():
    if square[row - 2][col] == empty_space:
        return '1'
    else:
        return '0'




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
        if new_position[1] < size * 2 - 1 and right_side_checking() == '1':
            square[row].pop(col)
            square[row].insert(col, empty_space)
            col += 2
            new_position = [row, col]
            square[row].pop(col)
            square[row].insert(col, character)
            change = "".join(square[row])
        else:
            pass





    if key == 'left':
        if new_position[1] > 1 and left_side_checking() == '1':
            square[row].pop(col)
            square[row].insert(col, empty_space)
            col -= 2
            new_position = [row, col]
            square[row].pop(col)
            square[row].insert(col, character)
            change = "".join(square[row])

    if key == 'down':
        if new_position[0] < size * 2 - 1 and down_side_checking() == '1':
            square[row].pop(col)
            square[row].insert(col, empty_space)
            row += 2
            new_position = [row, col]
            square[row].pop(col)
            square[row].insert(col, character)
            change = "".join(square[row])

    if key == 'up':
        if new_position[0] > 1 and up_side_checking() == '1':
            square[row].pop(col)
            square[row].insert(col, empty_space)
            row -= 2
            new_position = [row, col]
            square[row].pop(col)
            square[row].insert(col, character)
            change = "".join(square[row])

    for r_number, r in enumerate(square):
        screen.print_on_screen("".join(r), r_number)



