import tkinter as tk
import maze_maker
root = tk.Tk()
root.title("迷路ゲーム")

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy, key, mx, my
    if key == "Up":
        my-=1
    if key == "Right":
        mx+=1
    if key == "Left":
        mx-=1
    if key == "Down":
        my+=1
    cx, cy = mx*100+50, my*100+50
    c.coords("tori", cx, cy)
    root.after(100, main_proc)

mx, my = 1, 1
cx, cy = 300, 400
c = tk.Canvas(root,width = 1500, height =900, bg = "black")
c.pack()
maze = maze_maker.make_maze(15, 9)
maze_maker.show_maze(c, maze)
tori = tk.PhotoImage(file="ex03/fig/5.png")
c.create_image(cx, cy, image=tori, tag="tori")
key = ""
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
main_proc()
root.mainloop()