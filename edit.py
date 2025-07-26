import curses
import json

class SettingsEditor:
    def __init__(self, filename="settings.json"):
        self.filename = filename
        self.settings = self.load_settings()
        self.keys = list(self.settings.keys())
        self.current_index = 0
        self.edit_mode = False
        self.edit_value = ""

    def load_settings(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_settings(self):
        with open(self.filename, "w") as f:
            json.dump(self.settings, f, indent=4)

    def draw(self, screen):
        screen.clear()
        height, width = screen.getmaxyx()

        # Draw border
        #screen.box("|","_")
        screen.box("|","-")

        # Title
        title = "Settings Editor"
        screen.addstr(1, (width - len(title)) // 2, title)

        # Instructions
        instructions = " Arrows to Select. Enter to Edit/Accept. Esc to Save&Exit."
        screen.addstr(height - 2, 1, instructions)

        # Display settings
        start_y = 3
        for i, key in enumerate(self.keys):
            y = start_y + i
            if y >= height - 3:
                break

            if i == self.current_index:
                screen.attron(curses.color_pair(1))  # Highlight current line
                screen.addstr(y, 2, f"> {key}: {self.settings[key]}", curses.color_pair(1))
                screen.attroff(curses.color_pair(1))
            else:
                screen.addstr(y, 2, f"  {key}: {self.settings[key]}")

        # Edit mode
        if self.edit_mode:
            edit_str = f"Edit {self.keys[self.current_index]}: {self.edit_value}"
            screen.addstr(height - 6, 1, edit_str)

        screen.refresh()

    def handle_input(self, key):
        if self.edit_mode:
            if key == 27:  # Esc
                self.edit_mode = False
                self.edit_value = ""
            elif key == 10:  # Enter
                self.apply_edit()
            elif key == 127 or key == curses.KEY_BACKSPACE:  # Backspace
                self.edit_value = self.edit_value[:-1]
            elif 32 <= key <= 126:  # Printable characters
                self.edit_value += chr(key)
        else:
            if key == curses.KEY_DOWN:
                self.current_index = min(self.current_index + 1, len(self.keys) - 1)
            elif key == curses.KEY_UP:
                self.current_index = max(self.current_index - 1, 0)
            elif key == 10:  # Enter
                self.edit_mode = True
                self.edit_value = str(self.settings[self.keys[self.current_index]])
            elif key == 27:  # Esc
                return False
        return True

    def apply_edit(self):
        key = self.keys[self.current_index]
        try:
            # Attempt to convert to the original type
            original_type = type(self.settings[key])
            if original_type is bool:
                self.settings[key] = self.edit_value.lower() == 'true'
            elif original_type is int:
                self.settings[key] = int(self.edit_value)
            elif original_type is float:
                self.settings[key] = float(self.edit_value)
            else:
                self.settings[key] = self.edit_value
        except ValueError:
            pass  # If conversion fails, keep it as a string
        self.edit_mode = False
        self.edit_value = ""

    def run(self, screen):
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)  # Highlight color
        running = True
        while running:
            self.draw(screen)
            key = screen.getch()
            running = self.handle_input(key)
        self.save_settings()

if __name__ == "__main__":
    def main(screen):
        editor = SettingsEditor()
        editor.run(screen)

    curses.wrapper(main)