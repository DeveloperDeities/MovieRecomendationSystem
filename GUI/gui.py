from codingpart.colaborativeFiltering.usingKNN import recomender,mat_movies,stringFinal
global toBesearched

def close_window():
    window.destroy()
def fu():
    window=tkinter.Tk()
    window.geometry("600x400")
    window.title("new window")
    recomender(toBesearched.get(), mat_movies, 10)
    tkinter.Label(window, text=stringFinal, fg="red").grid(row=10, columnspan=2)
    tkinter.Button(window,text="exit",fg="red",command=(close_window())).grid(row=11,columnspan=2)
import tkinter
window=tkinter.Tk()
filename = tkinter.PhotoImage(file = "/root/PycharmProjects/MovieRecomendationSystem/GUI/backgroud.png")
background_label = tkinter.Label(image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# setting the windows size
window.geometry("600x400")
window.title("GUI")
tkinter.Label(window,text="movie liked",fg="blue",bg="pink").grid(row=0,column=0)
toBesearched=tkinter.Entry(window,fg="black",bg="pink")
toBesearched.grid(row=0,column=1)
tkinter.Button(window,text="search",fg="pink",command=(fu)).grid(row=3,columnspan=2)
window.mainloop()
