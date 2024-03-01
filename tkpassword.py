def checkPW():
    if(pw.get() == "1234"):
        msg.set("correct!")
    else:
        msg.set("false!")
#function() first, GUI second
import tkinter as tk
win = tk.Tk()
pw = tk.StringVar()
msg = tk.StringVar()
label = tk.Label(win,text="please input password:")
label.pack()
entry = tk.Entry(win,textvariable=pw)
entry.pack()
button = tk.Button(win,text='login',command=checkPW)
button.pack()
lblmsg = tk.Label(win,fg='red',textvariable=msg)
lblmsg.pack()


win.mainloop()