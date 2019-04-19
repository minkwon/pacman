import sys


if len(sys.argv) < 2:
    map_size = 3
else:
    try:
        map_size = int(sys.argv[1])
    except ValueError:
        map_size = 10

