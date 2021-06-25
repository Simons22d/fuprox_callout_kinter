import tkinter as tk
from subprocess import call
import os
root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()
root.title("Start Speech Module")



def caller():
    label1 = tk.Label(root, text='Running ...', fg='green', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 200, window=label1)
    call(["python",f"{os.path.join(os.getcwd(),'callout.py')}"])
    return {"phrase": "phrase"}


button1 = tk.Button(text='Start Speech Module', command=caller, bg='brown', fg='white')
canvas1.create_window(150, 150, window=button1)

root.mainloop()
