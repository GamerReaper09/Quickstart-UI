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
        self.geometry(f"{len(config)*100}x100")
        self.attributes('-topmost', True)
        self.attributes('-alpha', 1)
        self.resizable(width=False, height=False)

        self.shown = False
        self.buttons = {}

        self.frame = Frame(self)
        self.frame.grid_propagate(False)
        self.frame.rowconfigure(0, weight=1)
        for i, item in enumerate(config):
            self.frame.columnconfigure(i, weight=1, uniform="buttons")
            self.create_button(item["name"],0,i)
        self.frame.pack(fill=BOTH, expand=True)

    def create_button(self, name, row, column):
        button = Button(self.frame, text=name)
        button.grid(row=row, column=column,sticky="nsew")

    def toggle(self):
        if self.shown:
            self.shown = False
            self.withdraw()
        else:
            self.shown = False
            self.deiconify()

if __name__ == "__main__":
    app = App()
    keyboard.add_hotkey("alt+shift",app.toggle)
    keyboard.add_hotkey("alt+shift+r", app.destroy)
    app.mainloop()