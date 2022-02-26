import tkinter as tk
from tkinter import ttk

root = tk.Tk()
# pass in the parent "root"
ttk.Label(root, text="Hello, World!", padding=(30, 10)).pack()  

root.mainloop()
