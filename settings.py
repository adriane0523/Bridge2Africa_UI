from tkinter import *
window=Tk()
# add widgets here
lbl=Label(window, text="Setting", fg='black', font=("Ariel", 12))
lbl.place(x=410, y=100)

btn=Button(window, text="Speech Speed", fg='black')
btn.place(x=410, y=200)

btn=Button(window, text="Shortcut", fg='black')
btn.place(x=400, y=300)

window.title('Main Menu')
window.geometry("900x600+10+20")
window.mainloop()
