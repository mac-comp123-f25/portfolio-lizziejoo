import tkinter as tk

# ----- GUI class and methods -----
class BasicGui:
    def __init__(self):
        self.mainWin = tk.Tk()
        self.mainWin.title("Greeter App")

        quit_button = tk.Button(self.mainWin, text="Quit", command=self.quit_callback)
        quit_button.grid(row=0, column=0)

        hello_button = tk.Button(self.mainWin, text="Hello", command=self.hello_callback)
        hello_button.grid(row=1, column=0)

        goodbye_button = tk.Button(self.mainWin, text="Goodbye", command=self.goodbye_callback)
        goodbye_button.grid(row=2, column=0)

        self.welcome_label = tk.Label(self.mainWin, text="Welcome")
        self.welcome_label.grid(row=1, column=1)

    def quit_callback(self):
        self.mainWin.destroy()

    def hello_callback(self):
        self.welcome_label.config(text="Hello")

    def goodbye_callback(self):
        self.welcome_label.config(text="Goodbye")

    def run(self):
        self.mainWin.mainloop()

# ----- Main program -----
myGui = BasicGui()
myGui.run()