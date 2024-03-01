import tkinter as tk
win = tk.Tk()#it means open a window
# win.geometry('400x400')


#1.Text component: width,height,background(bg),foreground(fg),font,padx,pady,state,"insert()"
text = tk.Text(win)#text component(container,parameter1,parameter2,...)
text.insert(tk.INSERT,"Tkinter is a Graph User Interface(GUI),\n")
text.insert(tk.INSERT,"Tkinter is a Graph User Interface(GUI),\n")
text.insert(tk.INSERT,"Tkinter is a Graph User Interface(GUI),\n")
text.insert(tk.INSERT,"Tkinter is a Graph User Interface(GUI),\n")
text.insert(tk.END,"Tkinter is a Graph User Interface(GUI),\n")
text.pack()
# text.config(state=tk.DISABLED)#state=tk.DISABLED, is setting the text edit to be disabled

#2.Entry component: width,height,background(bg),foreground(fg),textvariable,font,padx,pady,state
def checkPW():
    if(pw.get() == "1234"):
        msg.set("correct!")
    else:
        msg.set("false!")
#function() first, GUI second

# win = tk.Tk()

#放在同一個視窗就能動了
#it is work when in the same window.
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

#3.Radiobutton component: width,height,text,variable,background(bg),foreground(fg),font,padx,pady,value,command,"select"
def choose():
    msg.set("You favorite ball sport: "+ choice.get())

# win = tk.Tk()
choice = tk.StringVar()
msg = tk.StringVar()
# label
label = tk.Label(win,text = "Select favirite ball sport:")
label.pack()
# item, one item one pack
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
checkbox = [] # define a null list
ball = ['football','basketball','baseball','pingpong','tennis']# all items in list
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
    
    
lblmsg = tk.Label(win, fg="red",textvariable=msg) #msg reveal here
lblmsg.pack()







win.mainloop()