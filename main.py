""" Command Line Tetris Python application
This is based on the video by "one lonely coder" - https://www.youtube.com/watch?v=8OK8_tHeCIA&t=140s
and rewritten in Python.
Author: Sam Hollings"""

import textwrap
from curses import wrapper

# Assets

def indexer_rotator(x,y, w=4, rotation=0):
    if rotation == 0:
        i = x*w + y
    elif rotation == 1: # 90 degrees
        i = 12+y-(x*4)
    elif rotation == 1:  # 90 degrees
        i = 12 + y - (x * 4)
    elif rotation == 2: # 180 degrees
        i = 15 - (y * 4)- x
    elif rotation == 3: # 270 degrees
        i = 3 + y + (x * 4)
    return i

# field definition

SCREEN_WIDTH = 80 # nScreenWidth
SCREEN_HEIGHT = 30 # nScreenHeight
FIELD_WIDTH = 12 # nFieldWidth
FIELD_HEIGHT = 18 # nFieldHeight
FIELD = '' #pField

# initialise the array
ACTIVE_FIELD = [0]*(FIELD_WIDTH*FIELD_HEIGHT) # Create play field buffer
for x in range(0,  FIELD_WIDTH): # Board Boundary
    for y in range (0, FIELD_HEIGHT):
        if x == 0 or x == FIELD_WIDTH - 1 or y == FIELD_HEIGHT - 1:
            cell_value = 9
        else:
            cell_value = 0
        ACTIVE_FIELD[indexer_rotator(x, y, w=FIELD_WIDTH)] = cell_value


# create tetromino object

tetromino = []

# 0 - line
tetromino.append("..X." \
                 "..X." \
                 "..X." \
                 "..X.")

# 1 - Zed
tetromino.append("..X." \
                 ".XX." \
                 ".X.." \
                 "....")

# 2 - "S"
tetromino.append(".X.." \
                 ".XX." \
                 "..X." \
                 "....")
# 3 - square
tetromino.append("...." \
                 ".XX." \
                 ".XX." \
                 "....")


# 4 - "T"
tetromino.append("..X." \
                 ".XX." \
                 "..X." \
                 "....")

# 5 - "L"
tetromino.append("...." \
                 ".XX." \
                 "..X." \
                 "..X.")

# 6 - backwards-L
tetromino.append("...." \
                 ".XX." \
                 ".X.." \
                 ".X..")


# Display

# Draw the field

## testing
FIELD_WIDTH = 4
FIELD_HEIGHT = 4

SCREEN_WIDTH = 10
SCREEN_HEIGHT = 10
# end test

screen = ['.']*(SCREEN_WIDTH*SCREEN_HEIGHT)
offset = 2

for x in range(0, FIELD_WIDTH):
    for y in range(0, FIELD_HEIGHT):
        screen[((y + offset) * SCREEN_WIDTH) + (x + offset)] = " ABCDEFG=#"[[9,9,9,9,9,0,0,9,9,0,0,9,9,9,9,9][y * FIELD_WIDTH + x]];
        #screen[(y + offset) * SCREEN_WIDTH + (x + offset)] = " ABCDEFG=#"[ACTIVE_FIELD[y * FIELD_WIDTH + x]];

def wrap(string, max_width):
    s=''
    for i in range(0,len(string),max_width):
        s=s+string[i:i+max_width]
        s=s+'\n'
    return s

#print(wrap("".join(screen),SCREEN_WIDTH))
#
# exit()

# for y, row in enumerate(wrap("".join(screen),SCREEN_WIDTH)):
#     print(row)

def main(stdscr):
    # Clear screen
    stdscr.clear()

    stdscr.addstr(0, 0, wrap("".join(screen),SCREEN_WIDTH))

    stdscr.refresh()
    stdscr.getkey()

wrapper(main)