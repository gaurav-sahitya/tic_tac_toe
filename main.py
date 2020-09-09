from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont

root=Tk()
root.title("Tic Tac Toe")
root.geometry("500x500")

l=["b00","b01","b02","b10","b11","b12","b20","b21","b22"]
t=["t00","t01","t02","t10","t11","t12","t20","t21","t22"]

def resize(event):
    global b00,b01,b02,b10,b11,b12,b20,b21,b22
    for i in [b00,b01,b02,b10,b11,b12,b20,b21,b22]:
        height=i.winfo_height()
        height=3*(height//5)
        i["font"]=("roboto",height)

for i in l:
    exec(i+'''=Button(text="G")''')
    exec(f"{i}.grid(row={int(i[-2])},column={int(i[-1])},sticky='nsew')")
for i in range(3):
    root.grid_columnconfigure(i,weight=1)
    root.grid_rowconfigure(i,weight=1)

root.bind("<Configure>",resize)

root.mainloop()