from re import X
import tkinter as tk
import tkinter.messagebox as tkm
from turtle import right
def button_click(event):
    btn = event.widget #どのボタンが押されたか
    txt = btn["text"] #押されたボタンのtext属性を返す　（クラス）
    entry.insert(tk.END, txt)

root = tk.Tk()

root.geometry("300x600")
entry = tk.Entry(root, width=10, font=("Times New Roman", 40), justify="right")
entry.grid(row=0, column=0,  columnspan=3)

x = 0
y = 0
for n in range(9, -2, -1):
    if n == -1:
        button = tk.Button(root, text=f"+", font=("Times New Roman", 30),  width=4, height=2)
        button.bind("<1>", button_click)
        button.grid(row = y+1, column = x)
    else:
        button = tk.Button(root, text=f"{n}", font=("Times New Roman", 30),  width=4, height=2)
        button.bind("<1>", button_click)
        button.grid(row = y+1,column = x)
    x += 1
    if x % 3 == 0:
        x = 0
        y += 1

root.mainloop()