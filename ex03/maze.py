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

# def main_loop():
#     if key == "Up":
#     if key == "Down":
#     if key == "Left":
#     if key == "Right":
def main_proc():
    global cx, cy, key
    if key == "Up":
        cy-=20
    if key == "Right":
        cx+=20
    if key == "Left":
        cx-=20
    if key == "Down":
        cy+=20
    c.coords("tori", cx, cy)
    root.after(100, main_proc)

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