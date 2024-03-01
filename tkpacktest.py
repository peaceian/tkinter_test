import tkinter as tk

win = tk.Tk()
# 1.pack method
# padx,pady,side
button1 = tk.Button(win,text="這是按鈕一",width=20)
button2 = tk.Button(win,text="這是按鈕二",width=20)
button3 = tk.Button(win,text="這是按鈕三",width=20)
button4 = tk.Button(win,text="這是按鈕四",width=20)

button1.pack(padx=20,pady=5,side="top")# padx,pady, are setting the position
button2.pack(padx=20,pady=5,side="bottom")
button3.pack(padx=20,pady=5,side="left")
button4.pack(padx=20,pady=5,side="top")

# 2.grid method is using "table" to array the componenets position.
# row, column, padx, pady, rowpan, columnspan, sticky
# button methods are different and need to build other windows
win = tk.Tk()
button5 = tk.Button(win,text="這是按鈕五",width=20)
button5.grid(row=2, column=2,padx=5,pady=5)
button6 = tk.Button(win,text="這是按鈕六",width=20)
button6.grid(row=1, column=0,padx=5,pady=5)
button7 = tk.Button(win,text="這是按鈕七",width=20)
button7.grid(row=0, column=2,padx=5,pady=5)
button8 = tk.Button(win,text="這是按鈕八",width=20)
button8.grid(row=1, column=1,padx=5,pady=5)
button9 = tk.Button(win,text="這是按鈕九",width=20)
button9.grid(row=0, column=1,padx=5,pady=5)
button10 = tk.Button(win,text="這是按鈕十",width=20)
button10.grid(row=2, column=3,padx=5,pady=5)

# 3.place method of x,y coordinate is often used to set the component
# x, y, relx, rely, anchor

win = tk.Tk()
win.geometry('300x100')
label1 = tk.Label(win,text="輸入成績：")#(容器,文字)
label1.place(x=20,y=20)
# score = tk.StringVar()
entrySpace = tk.Entry(win,textvariable=tk.StringVar)#可直接寫進去
entrySpace.place(x=90,y=20)#(x,y)
btn=tk.Button(win,text="計算成績")
btn.place(x=80,y=50)




win.mainloop()