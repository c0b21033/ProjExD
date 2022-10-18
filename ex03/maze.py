from sys import flags
import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker
from PIL import Image, ImageTk

def count_down(): #制限時間を制御する関数
    global tmr, time_flag, cid
    time_flag = True 
    tmr = tmr-0.01
    s = format(tmr, ".2f") #少数2桁まで表示
    label["text"] = s
    cid = root.after(10, count_down)

def key_down(event): #入力を受け付ける
    global key
    key = event.keysym
    if time_flag == False: #キーが入力されたら制限時間をスタートさせる
        root.after(1, count_down)

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy, mx, my, key, goal_flag, B_flag, B
    if goal_flag == True:#ゴールしたなら
        root.after_cancel(cid)#関数の停止
        tkm.showinfo("Congratulation", "GOAL!!")
        return
    if B_flag==True: #制限時間が過ぎてしまったら
        root.after_cancel(cid)
        c.create_image(50, 50, image=B, tag="B") #画像の表示
        tkm.showwarning("GAME OVER", "こうかとんは爆発してしまいした…\nR.I.P")
        return
    if key == "Up" and maze[my-1][mx]== 0:
        my-=1
    if key == "Right" and maze[my][mx+1] == 0 or maze[my][mx+1] == 2:
        mx+=1
        if maze[my][mx] == 2:#進む先がゴールだったら
            if maze[my][mx] == 2:
                goal_flag=True#ゴール判定をTrueにする
                
    if key == "Left" and maze[my][mx-1]== 0:
        mx-=1
    if key == "Down" and maze[my+1][mx]== 0 or maze[my+1][mx] == 2:
        my+=1
        if maze[my][mx] == 2:#進む先がゴールなら
            goal_flag=True
            
    cx = mx*100+50
    cy = my*100+50
    
    c.coords("tori", cx, cy)
    if tmr <= 0:#制限時間が過ぎてしまったら
        B_flag=True#ゲームオーバー判定をTrueにする
    root.after(100, main_proc)

time_flag = False #ゲームが始まっているか（ユーザーの最初の入力があったか）
goal_flag = False #ゴールしているかどうか
B_flag = False #ゲームオーバーかどうか
mx, my, cx, cy = 1, 1, 300, 400
key = ""
tmr = 2#制限時間
root = tk.Tk()
root.title("迷路ゲーム")
root.geometry("1500x1100")

label = tk.Label(root, font=("", 80))
label.pack()

c = tk.Canvas(root,width = 1500, height =900, bg = "black")
c.pack()
tori = tk.PhotoImage(file="ex03/fig/5.png")
B = Image.open("ex03/fig/B.jpg") #ゲームオーバーに使用する画像
B = ImageTk.PhotoImage(B)
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)

maze = maze_maker.make_maze(15, 9)
maze_maker.show_maze(c, maze)
maze[7][13] = 2 #ゴール地点の作成

main_proc()

c.create_rectangle(100, 100, 200, 200, fill="cyan")#スタートをcyanで描写
c.create_rectangle(1300, 700, 1400, 800, fill="red")#ゴール地点をredで描写
c.create_image(cx, cy, image=tori, tag="tori")

root.mainloop() 
