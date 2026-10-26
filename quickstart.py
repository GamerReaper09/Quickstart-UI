from tkinter import *
from tkinter import ttk
import keyboard
import json
import os
from PIL import Image as PILImage, ImageTk
import sys
from pathlib import Path

if getattr(sys, "frozen", False):
    directory = Path(sys.executable).parent
else:
    directory = Path(__file__).parent

if not os.path.exists(directory / "config.json"):
    raise FileNotFoundError("config.json not found")

with open(directory / "config.json","r") as f:
    config = json.load(f)


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple GUI")
        self.width = len(config)*100
        self.height = 100
        self.geometry(f"{self.width}x{self.height}")
        self.attributes('-topmost', True)
        self.attributes('-alpha', 0.8)
        self.resizable(width=False, height=False)
        self.overrideredirect(True)

        self.shown = False
        self.buttons = {}
        self.style = ttk.Style(self)
        self.style.theme_use("clam")
        self.style.map("Custom.TButton",
                       foreground=[('disabled', 'gray')],
                       background=[('active',"#4d4d4d"),('disabled', 'black')])
        self.style.configure("Custom.TButton", font=("Arial", 12), background="#1a1a1a", foreground="#f0f0f0",padding="0",relief="flat")

        self.frame = Frame(self)
        self.frame.grid_propagate(False)
        self.frame.rowconfigure(0, weight=1)
        for i, item in enumerate(config):
            self.frame.columnconfigure(i, weight=1, uniform="buttons")
            self.create_button(item["name"],0,i, item["path"],item["icon"])
        self.frame.pack(fill=BOTH, expand=True)

        self.frame.bind("<Leave>", lambda e: self.toggle(override=True))
        self.bind("<Button-1>", lambda e: self.after(200, self.toggle, True))

        self.withdraw()
        print("App launched without fatal errors. Alt+Shift to toggle. Alt+Shift+R to exit.")

    def create_button(self, name, row, column, path, icon):
        disabled = False
        if not os.path.exists(path):
            if os.path.exists(f"{path}/"):
                path += "/"
            else:
                disabled = True
        button = ttk.Button(self.frame, text=name, command=lambda: os.startfile(path),style="Custom.TButton")
        if disabled:
            button.state(["disabled"])
            button.configure(text="error")
        if not icon == "":
            if icon[-1:] == "/":
                icon = icon[:-1]
            img = PILImage.open(icon)
            img = img.resize((80,80), PILImage.Resampling.LANCZOS)
            icon = ImageTk.PhotoImage(img)
            button.configure(image=icon, text="")
            # noinspection unresolved-references
            button.image = icon
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