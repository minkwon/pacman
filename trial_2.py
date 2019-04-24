import screen
import random
import sys
import sound

# Emoji from
#
# https://unicode.org/emoji/charts/emoji-list.html

emoji_list = {
    "laugh": "\U0001F606",  # laugh
    "pinocchio": "\U0001F925",  # pinocchio
    "two hearts": "\U0001F495",  # two hearts
    "ghost": "\U0001F47B",  # ghost
    "vampire": "\U0001F9DB",  # vampire
    "fairy": "\U0001F9DA",
    "wizard": "\U0001F9D9",
    "bat": "\U0001F987",
    "cactus": "\U0001F335",
    "croissant": "\U0001F950",
    "dango": "\U0001F361",
    "evergreen tree": "\U0001F332",
    "house": "\U0001F3E0",
    "cherries": "\U0001F352"




}

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
            if 0.05 <= get_percentage() < 0.1:
                my_list.append(emoji_list['cherries'])
            elif 0.1 <= get_percentage() and get_percentage() < 0.2:
                my_list.append(emoji_list['evergreen tree'])
            else:
                my_list.append(empty_space)

        data.append(my_list)

    return data


map_line = map_list(size)
matrix = data(size)


def character_on_map():
    for i in range(0, len(matrix[0])):
        for j in range(0, len(matrix[0])):
            map_line[2 * j + 1].pop(2 * i + 1)
            value = matrix[j].pop(i)
            matrix[j].insert(i, empty_space)
            map_line[2 * j + 1].insert(2 * i + 1, value)
    return map_line


def check_side(x, y):
    if square[x][y] == empty_space:
        return '1'
    elif square[x][y] == emoji_list['cherries']:
        return '2'
    elif square[x][y] == emoji_list['bat']:
        return '3'
    else:
        return '0'



def right_side_checking():
    return check_side(new_position[0], new_position[1] + 2)


def left_side_checking():
    return check_side(new_position[0], new_position[1] - 2)


def down_side_checking():
    return check_side(new_position[0] + 2, new_position[1])


def up_side_checking():
    return check_side(new_position[0] - 2, new_position[1])

def enemy_right_side_checking():
    return check_side(enemy_position[0], enemy_position[1] + 2)


def enemy_left_side_checking():
    return check_side(enemy_position[0], enemy_position[1] - 2)


def enemy_down_side_checking():
    return check_side(enemy_position[0] + 2, enemy_position[1])


def enemy_up_side_checking():
    return check_side(enemy_position[0] - 2, enemy_position[1])

def make_new_position(direction, row, col):
    square[row].pop(col)
    square[row].insert(col, empty_space)

    if direction == 'right':
        col += 2
    elif direction == 'left':
        col -= 2
    elif direction == 'down':
        row += 2
    elif direction == 'up':
        row -= 2

    square[row].pop(col)
    square[row].insert(col, character)

    return [row, col]







character = emoji_list['ghost']
square = character_on_map()
x = 0
y = 0
row = 2 * x + 1
col = 2 * y + 1
square[row].pop(col)
square[row].insert(col, character)
new_position = [row, col]
point = 0

enemy = emoji_list['bat']
a = 2
b = 0
r = 2 * a + 1
c = 2 * b + 1
square[r].pop(c)
square[r].insert(c, enemy)
enemy_position = [r, c]

def enemy_moving(direction, r, c):
    square[r].pop(c)
    square[r].insert(c, empty_space)

    if direction == 'right':
        r += 2
    elif direction == 'left':
        c -= 2
    elif direction == 'down':
        c += 2
    elif direction == 'up':
        r -= 2

    square[r].pop(c)
    square[r].insert(c, enemy)

    return [r, c]


while True:
    key = screen.get_input()
    screen.print_on_screen("                                               Position " + str(new_position), 0)
    screen.print_on_screen("                                               Point " + str(point), 1)

    if key == 'right':
        if new_position[1] < size * 2 - 1:
            if right_side_checking() == '1':
                new_position = make_new_position(key, new_position[0], new_position[1])
            elif right_side_checking() == '2':
                new_position = make_new_position(key, new_position[0], new_position[1])
                point += 1
            elif right_side_checking() == '3':
                point -= 1
                if point < 0:
                    point = 0

        if enemy_position[0] < size * 2 - 1:
            if enemy_down_side_checking() == '1':
                enemy_position = enemy_moving(key, enemy_position[0], enemy_position[1])



    elif key == 'left':
        if new_position[1] > 1:
            if left_side_checking() == '1':
                new_position = make_new_position(key, new_position[0], new_position[1])
            elif left_side_checking() == '2':
                new_position = make_new_position(key, new_position[0], new_position[1])
                point += 1
            elif left_side_checking() == '3':
                point -= 1
                if point < 0:
                    point = 0

        if enemy_position[1] > 1:
            if enemy_left_side_checking() == '1':
                enemy_position = enemy_moving(key, enemy_position[0], enemy_position[1])



    elif key == 'down':
        if new_position[0] < size * 2 - 1:
            if down_side_checking() == '1':
                new_position = make_new_position(key, new_position[0], new_position[1])
            elif down_side_checking() == '2':
                new_position = make_new_position(key, new_position[0], new_position[1])
                point += 1
            elif down_side_checking() == '3':
                point -= 1
                if point < 0:
                    point = 0

        if enemy_position[1] < size * 2 - 1:
            if enemy_right_side_checking() == '1':
                enemy_position = enemy_moving(key, enemy_position[0],enemy_position[1])



    elif key == 'up':
        if new_position[0] > 1:
            if up_side_checking() == '1':
                new_position = make_new_position(key, new_position[0], new_position[1])
            elif up_side_checking() == '2':
                new_position = make_new_position(key, new_position[0], new_position[1])
                point += 1
            elif up_side_checking() == '3':
                point -= 1
                if point < 0:
                    point = 0

        if enemy_position[0] > 1:
            if enemy_up_side_checking() == '1':
                enemy_position = enemy_moving(key, enemy_position[0], enemy_position[1])


    for r_number, r in enumerate(square):
        screen.print_on_screen("".join(r), r_number)
