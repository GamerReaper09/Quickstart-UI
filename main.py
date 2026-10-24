from tkinter import *
import keyboard

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple GUI")
        self.geometry(f"300x200")
        self.attributes('-topmost', True)
        self.attributes('-alpha', 0.8)
        self.resizable(width=False, height=False)

        self.shown = FALSE

        self.label = Label(self,text="Simple GUI")
        self.label.pack()

    def toggle(self):
        if self.shown:
            self.shown = FALSE
            self.withdraw()
        else:
            self.shown = TRUE
            self.deiconify()




if __name__ == "__main__":
    app = App()
    keyboard.add_hotkey("alt+shift",app.toggle)
    keyboard.add_hotkey("alt+shift+r", app.destroy)
    app.mainloop()