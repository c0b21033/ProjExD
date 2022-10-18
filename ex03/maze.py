import tkinter as tk

root = tk.Tk()
root.title("迷路ゲーム")

def key_down(event):
    global key
    key = event.keysym
    print(key)

cx, cy = 300, 400
c = tk.Canvas(root,width = 1500, height =900, bg = "black")
c.pack()
tori = tk.PhotoImage(file="ex03/fig/5.png")
c.create_image(cx, cy, image=tori, tag="tori")
key = ""
root.bind("<KeyPress>", key_down)
root.mainloop()