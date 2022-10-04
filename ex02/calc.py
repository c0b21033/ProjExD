import tkinter as tk
import tkinter.messagebox as tkm
def button_click(event):
    btn = event.widget #どのボタンが押されたか
    txt = btn["text"] #押されたボタンのtext属性を返す　（クラス）
    tkm.showinfo(txt, f"{txt}ボタンが押されました")
root = tk.Tk()

root.geometry("500x200")
root.mainloop()