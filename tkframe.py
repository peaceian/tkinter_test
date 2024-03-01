import tkinter as tk
win = tk.Tk()

# Frame: tk.Frame(container,parameter1,parameter2,text="",)
# width, height, background(bg)

# frame1 
frame1 = tk.Frame(win,padx=20,pady=10)
frame1.pack()

label1=tk.Label(frame1,text="標籤一：")
label1.grid(row=0,column=0)
entry1=tk.Entry(frame1)
entry1.grid(row=0,column=1)

# frame2
frame2 = tk.Frame(win,padx=20,pady=10)
frame2.pack()

btn1 = tk.Button(frame2,text="確定",padx=10)
btn1.grid(row=0,column=0,padx=5)
btn2 = tk.Button(frame2,text="取消",padx=10)
btn2.grid(row=0,column=2,padx=5)



win.mainloop()