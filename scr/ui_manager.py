import curses


class UIManager:
    def __init__(self):
        self.stdscr = curses.initscr()  # Initialize the curses library and get a window object representing the screen
        curses.cbreak()  # React to keys instantly, without requiring the Enter key to be pressed

    def display_message(self, message):
        self.stdscr.addstr(0, 0, message)  # Display a message in the top-left corner of the screen
        self.stdscr.refresh()  # Refresh the screen to make the changes visible

    def get_user_input(self, prompt):
        self.stdscr.addstr(1, 0, prompt)  # Display a prompt for input on the second line of the screen
        self.stdscr.refresh()  # Refresh the screen to make the prompt visible

        # Wait for the user to input a string and press Enter, then decode and return it
        return self.stdscr.getstr(1, len(prompt)).decode()

    def cleanup(self):
        curses.nocbreak()  # Return the terminal to its normal operational mode
        curses.endwin()  # Terminate the window and return to the normal terminal interface
