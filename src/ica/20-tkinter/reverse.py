import tkinter as tk


class BasicGui:
    def __init__(self):
        self.mainWin = tk.Tk()
        self.mainWin.title("String Reverser")

        instruction_label = tk.Label(self.mainWin, text="Enter a phrase and hit [Enter]:")
        instruction_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky='w')

        self.input_entry = tk.Entry(self.mainWin, width=40)
        self.input_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        output_heading_label = tk.Label(self.mainWin, text="Reversed Text:")
        output_heading_label.grid(row=2, column=0, padx=10, pady=(10, 0), sticky='w')

        self.display_label = tk.Label(self.mainWin, text="", fg="blue")
        self.display_label.grid(row=3, column=0, columnspan=2, padx=10, pady=(0, 10), sticky='w')

        quit_button = tk.Button(self.mainWin, text="Quit", command=self.quit_callback)
        quit_button.grid(row=4, column=1, padx=10, pady=10, sticky='se')

        self.input_entry.bind('<Return>', self.entry_response)

    def entry_response(self, event):
        original_text = self.input_entry.get()

        reversed_text = original_text[::-1]

        self.display_label['text'] = reversed_text

    def quit_callback(self):
        self.mainWin.destroy()

    def run(self):
        self.mainWin.mainloop()

myGui = BasicGui()
myGui.run()