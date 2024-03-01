import tkinter as tk
win = tk.Tk()
win.geometry()#x is alphabet
win.title('title practice')#title setting

label1=tk.Label(win,text="This is label conponent!",fg="red",bg="yellow",font=("Times Roman",16),padx=20,pady=10)
label1.pack()
# label component:width,height,text,textvarible,background(bg),foreground(fg),font,padx,pady
# .pack()

def click1():
    textvar.set("I have be clicked!")

textvar = tk.StringVar()
button1 = tk.Button(win, textvariable=textvar, command=click1)#command:set function() while clicking botton
textvar.set('按鈕')
button1.pack()
# button component width,height,text,textvarible,background(bg),foreground(fg),font,padx,pady,command

def clickme():
    global count
    count+=1
    labeltext.set("you clicked "+str(count)+" times !")
    if(btntext.get()=="Click me!"):
        btntext.set('back to origin!')
    else:
        btntext.set('Click me!')
        
labeltext = tk.StringVar()
btntext = tk.StringVar()
count = 0
label2 = tk.Label(win, fg="red",bg="yellow",font=("Times Roman",16),textvariable=labeltext)
labeltext.set('Welcome to Tkinter!')
label2.pack()
button2 = tk.Button(win,textvariable=btntext,command=clickme)
btntext.set("Click me!")
button2.pack()

win.mainloop()