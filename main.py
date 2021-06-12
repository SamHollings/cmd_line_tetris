""" Command Line Tetris Python application
This is based on the video by "one lonely coder" - https://www.youtube.com/watch?v=8OK8_tHeCIA&t=140s
and rewritten in Python.
Author: Sam Hollings"""

# Assets

# create tetromino class

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

def indexer_2d_to_1d(x,y, w=4, rotation=0):
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