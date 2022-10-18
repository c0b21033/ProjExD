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
    global cx, cy, mx, my, key
    if key == "Up" and maze[my-1][mx]== 0:
        my-=1
    if key == "Right" and maze[my][mx+1] == 0:
        mx+=1
    if key == "Left" and maze[my][mx-1]== 0:
        mx-=1
    if key == "Down" and maze[my+1][mx]== 0:
        my+=1
    cx = mx*100+50
    cy = my*100+50
    
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