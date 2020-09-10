from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont

root=Tk()
root.title("Tic Tac Toe")
root.geometry("500x500")

b=["b00", "b01", "b02", "b10", "b11", "b12", "b20", "b21", "b22"]
t=["t00","t01","t02","t10","t11","t12","t20","t21","t22"]
count=0

def resize(event):
    global b00,b01,b02,b10,b11,b12,b20,b21,b22,height
    max_width=0
    for i in [b00,b01,b02,b10,b11,b12,b20,b21,b22]:
        height=i.winfo_height()
        height=height//2
        i["font"]=("roboto",height)
        max_width=max(max_width,i.winfo_width())
    for i in [b00,b01,b02,b10,b11,b12,b20,b21,b22]:
        i["width"]=max_width

def IsWin():
    l=[[b00,b01,b02],[b10,b11,b12],[b20,b21,b22],[b00,b10,b20],[b01,b11,b21],[b02,b12,b22],[b00,b11,b22],[b20,b11,b02]]
    winners=[]
    for i in l:
        winner=i[1].cget("text")
        if all([j.cget("text")==winner for j in i]) and winner:
            winners.append(i)
    return winners

def click(b):
    global count
    if not b.cget("text"):
        if count%2==0 and not IsWin():
            b["text"]="X"
        elif count%2==1 and not IsWin():
            b["text"]="O"
        count += 1
        if IsWin() or count==9:
            for i in [b00,b01,b02,b10,b11,b12,b20,b21,b22]:
                i.config(state=DISABLED)
            if IsWin():
                for i in IsWin():
                    for j in i:
                        j.config(font=("roboto",height,"bold"),disabledforeground="red")

for i in b:
    exec(i+f'''=Button(command=lambda: click({i}))''')
    exec(f"{i}.grid(row={int(i[-2])},column={int(i[-1])},sticky='nsew')")
for i in range(3):
    root.grid_columnconfigure(i,weight=1)
    root.grid_rowconfigure(i,weight=1)

root.bind("<Configure>",resize)
root.mainloop()