from tkinter import *
import keyboard
import json
import os

with open("config.json","r") as f:
    config = json.load(f)


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple GUI")
        self.width = len(config)*100
        self.height = 100
        self.geometry(f"{self.width}x{self.height}")
        self.attributes('-topmost', True)
        self.attributes('-alpha', 0.6)
        self.resizable(width=False, height=False)
        self.overrideredirect(True)

        self.shown = True
        self.buttons = {}

        self.frame = Frame(self)
        self.frame.grid_propagate(False)
        self.frame.rowconfigure(0, weight=1)
        for i, item in enumerate(config):
            self.frame.columnconfigure(i, weight=1, uniform="buttons")
            self.create_button(item["name"],0,i, item["path"])
        self.frame.pack(fill=BOTH, expand=True)

        self.frame.bind("<Leave>", lambda e: self.toggle(override=True))
        self.bind("<Button-1>", lambda e: self.after(200, self.toggle, True))

        self.withdraw()

    def create_button(self, name, row, column, path):
        button = Button(self.frame, text=name, command=lambda: print(name,path))
        button.grid(row=row, column=column,sticky="nsew")

    def toggle(self, override=False):
        if override:
            self.shown = False
            self.withdraw()
        elif self.shown:
            self.shown = False
            self.withdraw()
        else:
            self.shown = True
            self.geometry(f"+{int(self.winfo_pointerx()-self.width/2)}+{int(self.winfo_pointery()-self.height/2)}")
            self.deiconify()

if __name__ == "__main__":
    app = App()
    keyboard.add_hotkey("alt+shift",app.toggle)
    keyboard.add_hotkey("alt+shift+r", app.destroy)
    app.mainloop()