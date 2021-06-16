""" Command Line Tetris Python application
This is based on the video by "one lonely coder" - https://www.youtube.com/watch?v=8OK8_tHeCIA&t=140s
and rewritten in Python.
Author: Sam Hollings"""

import curses

# initialise the terminal
stdscr = curses.initscr()

# begin_x = 20; begin_y = 7
# height = 100; width = 100
# stdscr = curses.newwin(height, width, begin_y, begin_x)

curses.cbreak()
curses.noecho()
stdscr.nodelay(True)
curses.curs_set(0)
stdscr.keypad(1)

# Assets


def indexer_rotator(x,y, w=4, rotation=0):
    """

    :param x:
    :param y:
    :param w:
    :param rotation:
    :return:
    """
    if rotation == 0:
        i = y*w + x
    elif rotation == 1: # 90 degrees
        i = 12+y-(x*4)
    elif rotation == 1:  # 90 degrees
        i = 12 + y - (x * 4)
    elif rotation == 2: # 180 degrees
        i = 15 - (y * 4)- x
    elif rotation == 3: # 270 degrees
        i = 3 + y + (x * 4)
    return i


def wrap(string, max_width):
    """

    :param string:
    :param max_width:
    :return:
    """
    s=''
    for i in range(0,len(string),max_width):
        s=s+string[i:i+max_width]
        s=s+'\n'
    return s

def does_piece_fit(n_tetromino, rotation, pos_x, pos_y):
    """

    :param n_tetromino:
    :param rotation:
    :param pos_x:
    :param pos_y:
    :return:
    """
    for x in range(0,4):
        for y in range(0,4):
            # get index of the piece component
            i_piece = indexer_rotator(x, y, rotation)

            # get index of the corresponding place on the filed
            i_field = indexer_rotator(pos_x + x, pos_y + y)

            if ((pos_x + x) >= 0 and (pos_x + x) < FIELD_WIDTH and
                (pos_y + y) >= 0 and (pos_y + y) < FIELD_HEIGHT and
                tetromino[n_tetromino][i_piece] == 'X' and ACTIVE_FIELD[i_field] != 0):
                return False
    return True

# field definition
SCREEN_WIDTH = 70 #80 # nScreenWidth
SCREEN_HEIGHT = 25#30 # nScreenHeight
FIELD_WIDTH = 12 # nFieldWidth
FIELD_HEIGHT = 18 # nFieldHeight
FIELD = '' #pField

# initialise the array
ACTIVE_FIELD = [0]*(FIELD_WIDTH*FIELD_HEIGHT) # Create play field buffer
for x in range(0,  FIELD_WIDTH): # Board Boundary
    for y in range (0, FIELD_HEIGHT):
        if x == 0:
            cell_value = 9
        elif x == FIELD_WIDTH - 1:
            cell_value = 9
        elif y == FIELD_HEIGHT - 1:
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

# define the field
screen = ['.']*(SCREEN_WIDTH*SCREEN_HEIGHT)
offset = 2

character_set = " ABCDEFG=#"
#character_set = [' ','A','B','C','D','E','F','G','=','#']

# Game logic
current_piece = 2
current_rotation = 0
current_x = int(FIELD_WIDTH / 2)
current_y = 0


# Game loop
game_over = False
while game_over is False:
    # Game Timing ###############################
    import time
    time.sleep(0.05)

    # Input #####################################
    key = stdscr.getch()

    input_left = curses.KEY_LEFT
    input_down = curses.KEY_DOWN
    input_right = curses.KEY_RIGHT

    if key == ord('z'):
        current_rotation+=1
        if current_rotation > 3:
            current_rotation = 0

    if key == curses.KEY_DOWN:
        current_y = min(current_y + 1, FIELD_HEIGHT - 4)

    if key == curses.KEY_LEFT:
        current_x = max(current_x - 1,0)
    if key == curses.KEY_RIGHT:
        current_x = min(current_x + 1,FIELD_WIDTH - 4)

    if current_piece < 0:
        current_piece = 0
    if current_piece > 6:
        current_piece = 6



    # Game logic ################################

    # Render Output #############################

    # Draw field
    stdscr.clear() # Clear screen

    for x in range(0, FIELD_WIDTH):
        for y in range(0, FIELD_HEIGHT):
            screen[(y + offset) * SCREEN_WIDTH + (x + offset)] = character_set[ACTIVE_FIELD[y * FIELD_WIDTH + x]];

    # Draw Current Piece
    for piece_x in range(0, 4):
        for piece_y in range(0, 4):
            if (tetromino[current_piece][indexer_rotator(piece_x,piece_y, w=4, rotation=current_rotation)] == 'X'):
                screen[(current_y + piece_y + offset) * SCREEN_WIDTH +
                       (current_x + piece_x + offset)] = character_set[current_piece+1];


    # display frame
    stdscr.addstr(0, 0, wrap("".join(screen), SCREEN_WIDTH))

    # Draw instructions
    stdscr.addstr(0, 20, "Hit 'q' to quit")
    stdscr.addstr(1, 20, f"Current Piece: {current_piece}")
    if key == ord('q'): # Q to exit
        break

    stdscr.refresh()

curses.endwin()