import tkinter as tk
from subprocess import call
import os

root = tk.Tk()
root.title("Start Speech Module")

canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()


def hello():
    root.wm_title("test")
    label1 = tk.Label(root,text='Running ... ', fg='green', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 200, window=label1)
    call(["python", f"{os.path.join(os.getcwd(), 'callout.py')}"])
    return {"phrase": "phrase"}


label1 = tk.Label(root, text='Speechr.', fg='black', font=('helvetica', 12, 'bold'))
button1 = tk.Button(text='Start Speech Module', command=hello, bg='brown', fg='white')
canvas1.create_window(150, 150, window=button1)

root.mainloop()
