import tkinter as tk
from time import strftime


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        # self.overrideredirect(True)  # Remove window decorators
        self.tk.call('wm', 'overrideredirect', self, '1')  # Normally the above command would work but there is a bug that causes the Boolean to be ignored.

        self.x = None
        self.y = None

        self.label = tk.Label(fg="#FF0000", bg="#000000")  # Create a label with red font
        self.label.pack(anchor='center')  # Center the text
        self.label.bind("<ButtonPress-1>", self.start_move)  # Add the dragging functionality (Mouse Down)
        self.label.bind("<ButtonRelease-1>", self.stop_move)  # Mouse Up
        self.label.bind("<B1-Motion>", self.do_move)  # Mouse Movement
        self.time()  # Update the label with the current time

        self.start_centered()  # Make sure the window starts at the top center of the screen

    def time(self):
        """
        Update label once a second with time displayed as: "21:48"
        """
        self.label.config(text=strftime('%H:%M'))
        self.label.after(1000, self.time)

    def start_move(self, event):
        """
        Get the current XY coordinates of the window
        """
        self.x = event.x
        self.y = event.y

    def stop_move(self, event):
        """
        Reset the current recorded XY Coordinates
        """
        self.x = None
        self.y = None

    def do_move(self, event):
        """
        Move the window to the current location of the mouse pointer
        """
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.geometry(f"+{x}+{y}")

    def start_centered(self):
        """
        Ensure the window is centered horizontally at the top of the screen
        """
        self.update_idletasks()
        width = self.winfo_width()
        frm_width = self.winfo_rootx() - self.winfo_x()
        win_width = width + 2 * frm_width
        height = self.winfo_height()
        x = self.winfo_screenwidth() // 2 - win_width // 2
        self.geometry(f'{width}x{height}+{x}+{0}')
        self.attributes('-topmost', True)
        self.update()


app = App()
app.mainloop()
