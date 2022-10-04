import tkinter as tk
import tkinter.messagebox as tkm
from random import randint
from copy import deepcopy
def button_click(event):
    btn = event.widget #どのボタンが押されたか
    txt = btn["text"] #押されたボタンのtext属性を返す　（クラス）
    board_shuffle()
    if txt == "+": 
        entry.insert(tk.END, txt)
    elif txt == "=":
        n = entry.get()
        result = eval(n)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    else:
        entry.insert(tk.END, txt)


root = tk.Tk()

root.geometry("300x600")
entry = tk.Entry(root, width=10, font=("Times New Roman", 40), justify="right")
entry.grid(row=0, column=0,  columnspan=3)

def board_shuffle():
    x = 0
    y = 0
    mark = ""
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "+", "="]
    numbers2 = deepcopy(numbers)
    for i,num in enumerate(numbers, 1):
        n = randint(0, len(numbers2)-1)
        mark = numbers2.pop(n)
        button = tk.Button(root, text=f"{mark}", font=("Times New Roman", 30),  width=4, height=2)
        button.bind("<1>", button_click)
        button.grid(row = y+1,column = x)
        x += 1
        if x % 3 == 0:
            x = 0
            y += 1
# for n in range(9, -3, -1):
#     if n < 0:
#         if n == -1:
#             mark = "+"
#         elif n == -2:
#             mark = "="
#     else:
#         mark = n
#     button = tk.Button(root, text=f"{mark}", font=("Times New Roman", 30),  width=4, height=2)
#     button.bind("<1>", button_click)
#     button.grid(row = y+1,column = x)
#     x += 1
#     if x % 3 == 0:
#         x = 0
#         y += 1
board_shuffle()
root.mainloop()