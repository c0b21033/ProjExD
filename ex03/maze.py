import tkinter as tk

root = tk.Tk()
root.title("迷路ゲーム")

cx, cy = 300, 400
c = tk.Canvas(root,width = 1500, height =900, bg = "black")
c.pack()
tori = tk.PhotoImage(file="ex03/fig/5.png")
c.create_image(cx, cy, image=tori, tag="tori")
root.mainloop()