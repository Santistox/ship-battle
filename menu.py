import sys,os
import curses

def calc_center(width, text):
    return int((width // 2) - (len(text) // 2) - len(text) % 2)

def draw_menu(stdscr):
    k = 0
    cursor_x = 0
    cursor_y = 0

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Loop where k is the last character pressed
    while (k != ord('q')):

        # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        if k == curses.KEY_DOWN:
            cursor_y = cursor_y + 1
        elif k == curses.KEY_UP:
            cursor_y = cursor_y - 1
        elif k == curses.KEY_RIGHT:
            cursor_x = cursor_x + 1
        elif k == curses.KEY_LEFT:
            cursor_x = cursor_x - 1

        cursor_x = max(0, cursor_x)
        cursor_x = min(width-1, cursor_x)

        cursor_y = max(0, cursor_y)
        cursor_y = min(height-1, cursor_y)
        if cursor_x == 10 and cursor_y == 10:
            title = "Ship Battle 2022"[:width-1]
        else:
            title = "Ship Battle 2021"[:width-1]

        # Declaration of strings
        # title = "Ship Battle 2021"[:width-1]
        subtitle = "MAIN MENU"[:width-1]

        menu_btn_1 = "[1] START NEW BATTLE"[:width-1]
        menu_btn_2 = "[2] YOUR BATTLES"[:width-1]
        menu_btn_3 = "[3] GAME RULES"[:width-1]
        menu_btn_4 = "[4] SETTINGS"[:width-1]
        menu_btn_5 = "[5] UPGRADES"[:width-1]
        menu_btn_6 = "[6] CHANGELOG"[:width-1]
        menu_btn_7 = "[7] AUTHORS"[:width-1]

        menu_help = "press any key from 1 to 7"[:width-1]
        keystr = "Last key pressed: {}".format(k)[:width-1]
        statusbarstr = "Press 'q' to exit | Pos: {}, {}".format(cursor_x, cursor_y)
        if k == 0:
            keystr = "No key press detected..."[:width-1]

        # Centering calculations
        # start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
        # start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
        # start_x_keystr = int((width // 2) - (len(keystr) // 2) - len(keystr) % 2)
        start_y = int((height // 2) - 15)

        # Rendering some text
        whstr = "DEBUG: ON | Width: {}, Height: {}".format(width, height)
        stdscr.addstr(0, 0, whstr, curses.color_pair(1))

        # Render status bar
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(height-1, 0, statusbarstr)
        stdscr.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(3))

        # Turning on attributes for title
        stdscr.attron(curses.color_pair(2))
        stdscr.attron(curses.A_BOLD)

        # Rendering title
        stdscr.addstr(start_y, calc_center(width, title), title)

        # Turning off attributes for title
        stdscr.attroff(curses.color_pair(2))
        stdscr.attroff(curses.A_BOLD)

        # Print rest of text
        stdscr.addstr(start_y + 2, calc_center(width, subtitle), subtitle)

        menu_btn_1_color = 0
        if cursor_x < calc_center(width, menu_btn_1) + len(menu_btn_1) and cursor_x > calc_center(width, menu_btn_1) and cursor_y == (start_y + 5):
             menu_btn_1_color = curses.color_pair(1)
        else:
            menu_btn_1_color = 0
        stdscr.addstr(start_y + 5, calc_center(width, menu_btn_1), menu_btn_1, menu_btn_1_color)
        stdscr.addstr(start_y + 6, calc_center(width, menu_btn_2), menu_btn_2)
        stdscr.addstr(start_y + 7, calc_center(width, menu_btn_3), menu_btn_3)
        stdscr.addstr(start_y + 8, calc_center(width, menu_btn_4), menu_btn_4)
        stdscr.addstr(start_y + 9, calc_center(width, menu_btn_5), menu_btn_5)
        stdscr.addstr(start_y + 10, calc_center(width, menu_btn_6), menu_btn_6)
        stdscr.addstr(start_y + 11, calc_center(width, menu_btn_7), menu_btn_7)
        
        stdscr.addstr(start_y + 15, calc_center(width, menu_help), menu_help)
        stdscr.addstr(start_y + 16, calc_center(width, keystr), keystr, curses.color_pair(1))
        stdscr.move(cursor_y, cursor_x)

        # Refresh the screen
        stdscr.refresh()

        # Wait for next input
        k = stdscr.getch()

def main():
    curses.wrapper(draw_menu)

if __name__ == "__main__":
    main()