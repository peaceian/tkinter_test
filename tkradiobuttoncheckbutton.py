import tkinter as tk

win = tk.Tk()
#3.Radiobutton component: width,height,text,variable,background(bg),foreground(fg),font,padx,pady,value,command,"select"
def choose():
    msg.set("You favorite ball sport: "+ choice.get())


choice = tk.StringVar()
msg = tk.StringVar()
# label
label = tk.Label(win,text = "Select favirite ball sport:")
label.pack()
# item
item1 = tk.Radiobutton(win,text="football",value="football",variable=choice,command=choose)
item1.pack()
item2 = tk.Radiobutton(win,text="basketball",value="basketball",variable=choice,command=choose)
item2.pack()
item3 = tk.Radiobutton(win,text="baseball",value="baseball",variable=choice,command=choose)
item3.pack()
# label
lblmsg = tk.Label(win,fg="red",textvariable=msg)
lblmsg.pack()
# default the select and function work.
item1.select()
choose()

#4.Checkbox component: width,height,text,variable,background(bg),foreground(fg),font,padx,pady,command,"select"
#impact**********
#Checkbox multi-choose 
def multichoose():
    str = "Your favorite ball sport: "
    for i in range(0, len(checkbox)):
        if (checkbox[i].get()==1):
            str = str + ball[i] +" "
    msg.set(str)

# win = tk.Tk()
checkbox = []
ball = ['football','basketball','baseball']
msg = tk.StringVar()
# label
label = tk.Label(win,text= "Select your favorite ball sports:")
label.pack()

#reveal the selected items
for i in range(0, len(ball)):
    tem = tk.IntVar()
    checkbox.append(tem)
    item = tk.Checkbutton(win, text=ball[i],variable=checkbox[i],command=multichoose)
    item.pack()
lblmsg = tk.Label(win, fg="red",textvariable=msg)
lblmsg.pack()







win.mainloop()