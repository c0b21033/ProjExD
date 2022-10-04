from re import X
import tkinter as tk
import tkinter.messagebox as tkm
def button_click(event):
    btn = event.widget #どのボタンが押されたか
    txt = btn["text"] #押されたボタンのtext属性を返す　（クラス）
    tkm.showinfo(txt, f"{txt}ボタンが押されました")
root = tk.Tk()

root.geometry("300x500")
x = 0
y = 0
for n in range(9, -1, -1):
    button = tk.Button(root, text=f"{n}", font=("Times New Roman", 30),  width=4, height=2)
    button.bind("<1>", button_click)
    button.grid(row = y,column = x)
    x += 1
    if x % 3 == 0:
        x = 0
        y += 1

root.mainloop()