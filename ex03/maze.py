import tkinter as tk

root = tk.Tk()
root.title("迷路ゲーム")

c = tk.Canvas(root,width = 1500, height =900, bg = "black")
c.pack()

root.mainloop()