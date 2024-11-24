import tkinter as tk

root = tk.Tk()
root.title("Ежедневник")
root.geometry("250x250")

for c in range(2): root.columnconfigure(index=c, weight=1)
for r in range(2): root.columnconfigure(index=r, weight=1)

btn1 = tk.Button(text="button1")
#растягиваем на 2 строчки
btn1.grid(row=0, column=0, ipadx=6, ipady=6, padx=5, pady=5)

btn2 = tk.Button(text="button2")
#растягиваем на 2 строчки
btn2.grid(row=0, column=1, rowspan=2, ipadx=6, ipady=55, padx=5, pady=5)

btn3 = tk.Button(text="button 3")
btn3.grid(row=1, column=0, ipadx=6, ipady=6, padx=5, pady=5)

root.mainloop()