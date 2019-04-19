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
            map_box = [draw_horizontal(size)]
        if i % 2 == 1:
            map_box = [draw_vertical(size)]
        map_list.append(map_box)
    map_list.append([draw_horizontal(size)])

    return map_list



while True:
    key = screen.get_input()
    screen.print_on_screen("                                       You entered " + key, 0)

    for i in range(0, size * 2):
        if i % 2 == 0 or i == 0:
            screen.print_on_screen(draw_horizontal(size), i)
        if i % 2 == 1:
            screen.print_on_screen(draw_vertical(size), i)
    screen.print_on_screen(draw_horizontal(size), size * 2)

    screen.print_on_screen('|O', 1)



    right_count = 0
    left_count = size - 1
    down_count = 0
    up_count = size - 1
    if screen.get_input() == 'right' and 0 < right_count <= size - 1:
        data[down_count].pop(right_count)
        right_count += 1
        left_count -= 1
        data[down_count].insert(right_count, 'O')

        if right_count > size - 1:
            right_count = size - 1

    if screen.get_input() == 'left' and 0 < left_count <= size - 1:
        data[down_count].pop(right_count)
        left_count += 1
        right_count -= 1
        data[down_count].insert(right_count, 'O')

        if left_count > size - 1:
            left_count = size - 1

    if screen.get_input() == 'down' and 0 < down_count <= size - 1:
        data[down_count].pop(right_count)
        down_count += 1
        up_count -= 1
        data[down_count].insert(right_count, 'O')

        if down_count > size - 1:
            down_count = size - 1

    if screen.get_input() == 'up' and 0 < up_count <= size - 1:
        data[down_count].pop(right_count)
        up_count += 1
        down_count -= 1
        data[down_count].insert(right_count, 'O')

        if up_count > size - 1:
            up_count = size - 1





