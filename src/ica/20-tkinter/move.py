import tkinter as tk


class MoveWordsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Move Words")

        self.canvas = tk.Canvas(root, bg="lightblue")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.text_id = self.canvas.create_text(150, 150, text="Lizzie", fill="darkred", font=("Arial", 24))

        for key in ["w", "a", "s", "d", "Up", "Left", "Down", "Right"]:
            root.bind(f"<{key}>", self.move_callback)

        quit_button = tk.Button(root, text="Quit", command=root.destroy, bg="lightcoral", fg="white")
        quit_button.pack(pady=10)

    def move_callback(self, event):
        key_pressed = event.keysym
        print(f"Key pressed: {key_pressed}")

        if key_pressed in ["w", "Up"]:
            self.canvas.move(self.text_id, 0, -10)
        elif key_pressed in ["a", "Left"]:
            self.canvas.move(self.text_id, -10, 0)
        elif key_pressed in ["s", "Down"]:
            self.canvas.move(self.text_id, 0, 10)
        elif key_pressed in ["d", "Right"]:
            self.canvas.move(self.text_id, 10, 0)


if __name__ == "__main__":
    root = tk.Tk()
    app = MoveWordsApp(root)
    root.mainloop()

