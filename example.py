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


while True:
    key = screen.get_input()

    emoji = emoji_list[random.randrange(3)]

    screen.print_on_screen(" - - - -", 0)
    screen.print_on_screen("| | | | |", 1)

    screen.print_on_screen("You entered " + key + " " + emoji, 2)
    screen.print_on_screen(" - - - -", 4)


