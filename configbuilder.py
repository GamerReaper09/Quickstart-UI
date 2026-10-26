import json
import tkinter
import tkinter.filedialog as filedialog
import os

config = []
class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Config Builder")
        self.geometry("700x200")

        self.frame = tkinter.Frame(self)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=4)
        self.frame.columnconfigure(2, weight=1)
        self.frame.pack(fill="both")

        self.name = tkinter.StringVar()
        self.name_label = tkinter.Label(self.frame, text="Name:")
        self.name_label.grid(row=0, column=0)
        self.name_input = tkinter.Entry(self.frame, textvariable=self.name)
        self.name_input.grid(row=0, column=1,sticky="ew")

        self.path = tkinter.StringVar()
        self.path_label = tkinter.Label(self.frame, text="Path:")
        self.path_label.grid(row=1, column=0)
        self.path_input = tkinter.Entry(self.frame, textvariable=self.path)
        self.path_input.grid(row=1, column=1,sticky="ew")
        self.path_button = tkinter.Button(self.frame, text="Browse", command=self.browse_path)
        self.path_button.grid(row=1, column=2)

        self.icon = tkinter.StringVar()
        self.icon_label = tkinter.Label(self.frame, text="Icon (Optional):")
        self.icon_label.grid(row=2, column=0)
        self.icon_input = tkinter.Entry(self.frame, textvariable=self.icon)
        self.icon_input.grid(row=2, column=1, sticky="ew")
        self.icon_button = tkinter.Button(self.frame, text="Browse", command=self.browse_icon)
        self.icon_button.grid(row=2, column=2)

        self.submit_button = tkinter.Button(self, text="Add Item", command=self.create_item)
        self.submit_button.pack(fill="x", padx=50, pady=(10,0))

        self.amount = tkinter.StringVar()
        self.amount.set("Items: 0")
        self.stats = tkinter.Label(self, text="Items: ", textvariable=self.amount)
        self.stats.pack()

        self.create_button = tkinter.Button(self, text="Create Config", command=self.create_config)
        self.create_button.pack(fill="x", padx=50)

    def browse_path(self):
        ask_path = filedialog.askopenfilename()
        if ask_path:
            self.path.set(ask_path)
    def browse_icon(self):
        ask_icon = filedialog.askopenfilename()
        if ask_icon:
            self.icon.set(ask_icon)

    def create_item(self):
        config.append({"name": self.name.get(), "path": self.path.get(), "icon": self.icon.get()})
        self.amount.set(f"Items: {len(config)}")
    def create_config(self):
        save_path = filedialog.asksaveasfilename(defaultextension=".json", initialfile="config.json", filetypes=[("JSON", "*.json")])
        if save_path:
            with open(save_path, "w") as f:
                json.dump(config, f, indent=4)
            self.destroy()
        else:
            print("No save path selected. Config not saved.")

print("Config builder for Quickstart UI")
print("Each item requires a name and path. Icon is optional.")
method = input("Do you want to enter everything manually or use a gui? (m/g): ").lower()

if method == "g":
    root = App()
    root.mainloop()
elif method == "m":
    while True:
        name = input("Name: ")
        path = input("Path: ")
        icon = input("Icon (optional): ")
        config.append({"name": name, "path": path, "icon": icon})
        cont = input("Add another item? (y/n): ").lower()
        if cont != "y":
            save_path = input("Enter the path to save the config (e.g., config.json): ")
            if os.path.exists(os.path.dirname(save_path)):
                with open(save_path, "w") as f:
                    json.dump(config, f, indent=4)
                    print(f"Config saved to {save_path}")
            else:
                print("Invalid path. Config not saved.")
                break


