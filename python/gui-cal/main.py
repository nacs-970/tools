#scr : https://www.youtube.com/watch?v=NzSCNjn4_RI
import tkinter as tk

cal = ""

def button_press(num):
    global cal
    cal += str(num)
    txt_result.delete(1.0,"end")
    txt_result.insert(1.0,cal)

def equal():
    global cal
    try:
        resu=str(eval(cal))
        cal=""
        txt_result.delete(1.0,"end")
        txt_result.insert(1.0,resu)
    except:
        txt_result.delete(1.0,"end")
        txt_result.insert(1.0,"Error")

def clear():
    global cal
    cal = ""
    txt_result.delete(1.0,"end")

# Draw windows gui
window = tk.Tk()
window.geometry("352x275")
window.title("Calculator")

#Input field
txt_result = tk.Text(window, height=2, width=19,font=("Arial",24))
txt_result.grid(columnspan=5)

#Button number
bt1 = tk.Button(window,text="1",command=lambda: button_press(1),width=6,font=("Arial",14)) # lamda: refers first then call, so it dose add num to text field after open
bt1.grid(row=2,column=1)
bt2 = tk.Button(window,text="2",command=lambda: button_press(2),width=6,font=("Arial",14))
bt2.grid(row=2,column=2)
bt3 = tk.Button(window,text="3",command=lambda: button_press(3),width=6,font=("Arial",14))
bt3.grid(row=2,column=3)
bt4 = tk.Button(window,text="4",command=lambda: button_press(4),width=6,font=("Arial",14))
bt4.grid(row=3,column=1)
bt5 = tk.Button(window,text="5",command=lambda: button_press(5),width=6,font=("Arial",14))
bt5.grid(row=3,column=2)
bt6 = tk.Button(window,text="6",command=lambda: button_press(6),width=6,font=("Arial",14))
bt6.grid(row=3,column=3)
bt7 = tk.Button(window,text="7",command=lambda: button_press(7),width=6,font=("Arial",14))
bt7.grid(row=4,column=1)
bt8 = tk.Button(window,text="8",command=lambda: button_press(8),width=6,font=("Arial",14))
bt8.grid(row=4,column=2)
bt9 = tk.Button(window,text="9",command=lambda: button_press(9),width=6,font=("Arial",14))
bt9.grid(row=4,column=3)
bt0 = tk.Button(window,text="0",command=lambda: button_press(0),width=6,font=("Arial",14))
bt0.grid(row=5,column=2)

#Button operater + - * / ( )
btp = tk.Button(window,text="+",command=lambda: button_press("+"),width=6,font=("Arial",14))
btp.grid(row=2,column=4)
btm = tk.Button(window,text="-",command=lambda: button_press("-"),width=6,font=("Arial",14))
btm.grid(row=3,column=4)
btmu = tk.Button(window,text="*",command=lambda: button_press("*"),width=6,font=("Arial",14))
btmu.grid(row=4,column=4)
btd = tk.Button(window,text="/",command=lambda: button_press("/"),width=6,font=("Arial",14))
btd.grid(row=5,column=4)
btop = tk.Button(window,text="(",command=lambda: button_press("("),width=6,font=("Arial",14))
btop.grid(row=5,column=1)
btcl = tk.Button(window,text=")",command=lambda: button_press(")"),width=6,font=("Arial",14))
btcl.grid(row=5,column=3)
btclr = tk.Button(window,text="C",command=clear,width=6,font=("Arial",14)) # call function as entiy
btclr.grid(row=6,column=1)
bteq = tk.Button(window,text="=",command=equal,width=6,font=("Arial",14))
bteq.grid(row=6,column=2)
cool_txt = tk.Label(window,text="┬┴┬┴┤•ᴥ•ʔ├┬┴┬┴",width=11,font=("Arial",14)).grid(row=6,column=3,columnspan=2)

window.mainloop()

