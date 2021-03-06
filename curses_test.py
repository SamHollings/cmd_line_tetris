#curses.setupterm("This is a test terminal") # doesn't do anything

# terminal font size and type
import ctypes

kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
kernel32.SetConsoleTitleW(u"My New Title")

LF_FACESIZE = 32
STD_OUTPUT_HANDLE = -11

class COORD(ctypes.Structure):
    _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

class CONSOLE_FONT_INFOEX(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_ulong),
                ("nFont", ctypes.c_ulong),
                ("dwFontSize", COORD),
                ("FontFamily", ctypes.c_uint),
                ("FontWeight", ctypes.c_uint),
                ("FaceName", ctypes.c_wchar * LF_FACESIZE)]

font = CONSOLE_FONT_INFOEX()
font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX) # The size of this structure, in bytes. This member must be set to sizeof(CONSOLE_FONT_INFOEX) before calling GetCurrentConsoleFontEx or it will fail.
font.nFont = 4 # The index of the font in the system's console font table.
font.dwFontSize.X = 10 # A COORD structure that contains the width and height of each character in the font, in logical units. The X member contains the width, while the Y member contains the height.
font.dwFontSize.Y = 10 # A COORD structure that contains the width and height of each character in the font, in logical units. The X member contains the width, while the Y member contains the height.
font.FontFamily = 54 #The font pitch and family. For information about the possible values for this member, see the description of the tmPitchAndFamily member of the TEXTMETRIC structure.
font.FontWeight = 400 # normal weight is 400, whilst bold is 700
font.FaceName = "Lucida Console"

handle = kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
kernel32.SetCurrentConsoleFontEx(
        handle, ctypes.c_long(False), ctypes.pointer(font))

import curses
stdscr = curses.initscr()
curses.start_color()
curses.use_default_colors()

screen_height = 50#25
screen_width = 100#50
maxc = 255

# control terminal size and shape
stdscr = curses.newwin(screen_height, screen_width, 0, 0)
curses.resize_term(screen_height,screen_width)

curses.cbreak()
curses.noecho()
curses.curs_set(0)
# stdscr.move(50,50)
stdscr.keypad(1)



# fill the background in
stdscr.addstr(0,0,"\n".join(["".join(["." for x in range(0,screen_width-1)])
                             for y in range(0,screen_height-1)]),curses.color_pair(1))

# display some colours:
c_height = int(screen_height / 2)

list_of_colours = range(maxc)
colours_rows = [list_of_colours[i:i+screen_width] for i in range(0, len(list_of_colours), screen_width) ]
colour_rows_coords =  [tuple(zip(row,list(range(screen_width)))) for row in colours_rows]

for pixel_colour_y, row in enumerate(colour_rows_coords):
    for (pixel_colour_c, pixel_colour_x) in row:
        curses.init_pair(pixel_colour_c+1,pixel_colour_c,-1)
        stdscr.addstr(c_height+pixel_colour_y,pixel_colour_x,'#',curses.color_pair(pixel_colour_c+1))

# # add colours
# for i in range(0, curses.COLORS):
#     curses.init_pair(i + 1, i, -1)
# try:
#     for i in range(0, 255):
#         stdscr.addstr(str(i), curses.color_pair(i))
# except curses.ERR:
#     # End of screen reached
#     pass

# write some stuff
stdscr.addstr(0,10,"Hit 'q' to quit")
stdscr.refresh()

key = ''
while key != ord('q'):
    key = stdscr.getch()
    stdscr.addch(20,25,key)
    stdscr.refresh()
    if key == curses.KEY_UP:
        stdscr.addstr(2, 20, "Up")
    elif key == curses.KEY_DOWN:
        stdscr.addstr(3, 20, "Down")

    # dynamic title
    kernel32.SetConsoleTitleW(u"My New Title - keypress : {0}".format(key))

curses.endwin()