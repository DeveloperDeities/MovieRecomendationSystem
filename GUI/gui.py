
def fun():
    tkinter.END
def fu():
    global toBesearched
    window=tkinter.Tk()
    window.geometry("600x400")
    window.title("new window")
    tkinter.Label(window,text="hey"+toBesearched.get() ,fg="red").grid(row=10,columnspan=2)
    tkinter.Button(window,text="button2",fg="red",command=(fun)).grid(row=11,columnspan=2)
import tkinter
window=tkinter.Tk()
# setting the windows size
window.geometry("600x400")
window.title("GUI")
tkinter.Label(window,text="movie liked",fg="blue",bg="pink").grid(row=0,column=0)
toBesearched=tkinter.Entry(window,fg="black",bg="pink")
toBesearched.grid(row=0,column=1)
tkinter.Button(window,text="Login",fg="pink",command=(fu)).grid(row=3,columnspan=2)
window.mainloop()
