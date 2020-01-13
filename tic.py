import tkinter as tk
from tkinter import messagebox
top=tk.Tk()
bclick=True
count=0
#tk.messagebox.showinfo("Note","Game Starts With X")
def click(btn):
    global bclick,count
     
    if btn["text"]=="" and bclick==True:
        btn["text"]="X"
        bclick=False
        count+=1
        win()
    elif btn["text"]=="" and bclick==False:
        btn["text"]="O"
        bclick=True
        count+=1
        win()
    

def win():
    
    if (btn1['text'] == 'X' and btn2['text'] == 'X' and btn3['text'] == 'X' or
        btn4['text'] == 'X' and btn5['text'] == 'X' and btn6['text'] == 'X' or
        btn7['text'] =='X' and btn8['text'] == 'X' and btn9['text'] == 'X' or
        btn1['text'] == 'X' and btn5['text'] == 'X' and btn9['text'] == 'X' or
        btn3['text'] == 'X' and btn5['text'] == 'X' and btn7['text'] == 'X' or
        btn1['text'] == 'X' and btn2['text'] == 'X' and btn3['text'] == 'X' or
        btn1['text'] == 'X' and btn4['text'] == 'X' and btn7['text'] == 'X' or
        btn2['text'] == 'X' and btn5['text'] == 'X' and btn8['text'] == 'X' or
        btn7['text'] == 'X' and btn6['text'] == 'X' and btn9['text'] == 'X'):
         a=e1.get()+" wins"
         tk.messagebox.showinfo("WINNER WINNER",a)
        
    elif (btn1['text'] == 'O' and btn2['text'] == 'O' and btn3['text'] == 'O' or
          
        btn4['text'] == 'O' and btn5['text'] == 'O' and btn6['text'] == 'O' or
        btn7['text'] =='O' and btn8['text'] == 'O' and btn9['text'] == 'O' or
        btn1['text'] == 'O' and btn5['text'] == 'O' and btn9['text'] == 'O' or
        btn3['text'] == 'O' and btn5['text'] == 'O' and btn7['text'] == 'O' or
        btn1['text'] == 'O' and btn2['text'] == 'O' and btn3['text'] == 'O' or
        btn1['text'] == 'O' and btn4['text'] == 'O' and btn7['text'] == 'O' or
        btn2['text'] == 'O' and btn5['text'] == 'O' and btn8['text'] == 'O' or
        btn7['text'] == 'O' and btn6['text'] == 'O' and btn9['text'] == 'O'):
        a=e2.get()+" wins"
        tk.messagebox.showinfo("WINNER WINNER",a)
    elif count==8:
         tk.messagebox.showinfo("tie","Tie")
        

    
top.title("o-x Game")
p1=tk.Label(top,text="player 1")
p2=tk.Label(top,text="Player 2")

p1.grid(row=0)
p2.grid(row=1)
e1=tk.Entry(top)
e1.grid(row=0,column=1)
e2=tk.Entry(top)
e2.grid(row=1,column=1)
    


btn1=tk.Button(top,command=lambda:click(btn1))
btn1.grid(row=4,column=0)

btn2=tk.Button(top,command=lambda:click(btn2))
btn2.grid(row=4,column=1)

btn3=tk.Button(top,command=lambda:click(btn3))
btn3.grid(row=4,column=2)

btn4=tk.Button(top,command=lambda:click(btn4))
btn4.grid(row=5,column=0)

btn5=tk.Button(top,command=lambda:click(btn5))
btn5.grid(row=5,column=1)

btn6=tk.Button(top,command=lambda:click(btn6))
btn6.grid(row=5,column=2)

btn7=tk.Button(top,command=lambda:click(btn7))
btn7.grid(row=6,column=0)

btn8=tk.Button(top,command=lambda:click(btn8))
btn8.grid(row=6,column=1)

btn9=tk.Button(top,command=lambda:click(btn9))
btn9.grid(row=6,column=2)

