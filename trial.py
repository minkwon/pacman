import screen
import random

# Emoji from
#
# https://unicode.org/emoji/charts/emoji-list.html

emoji_list = [
    "\U0001F606", # laugh
    "\U0001F925", # pinocchio
    "\U0001F495" # two hearts
]


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

size = 8

def data(size):
    data_list = []
    for i in range(0, size):
        data_box = []
        for j in range(0, size):
            data_box.append(' ')
        data_list.append(data_box)

    return data

for i in range(0, size):
    map_list = []
    for j in range(0, size * 2):
        map_box = []
        if i % 2 == 0 or i == 0:
            map_box.append(draw_horizontal(size))
        if i % 2 == 1:
            map_box.append(draw_vertical(size))
    map_list.append(map_box)
print(map_list)


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

