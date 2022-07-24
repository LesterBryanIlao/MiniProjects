from tkinter import*
from PIL import ImageTk, Image
import circuit2
import circuit1
import circuit3

def call_GUI1():
    win1 = Toplevel(main)
    circuit1.one(win1)
    return
    
def call_GUI2():
    win2 = Toplevel(main)
    circuit2.one(win2)
    return

def call_GUI3():
    win3 = Toplevel(main)
    circuit3.one(win3)
    return


def destroy():
    main.destroy()

if __name__ == "__main__":
    main = Tk()
    main.title('SuperMesh Calculator')
    main.geometry('1280x720')
    img1 = ImageTk.PhotoImage(Image.open("1.png"))
    main.wm_iconphoto(True, img1)

    bgImage = PhotoImage(file=r'Calculator.png').subsample(1)
    Label(main, image=bgImage).place(relheight = 1, relwidth = 1)

    button_1 = Button(main, text='Example1', width='16',font=('Calibri',11),command=call_GUI1)
    button_1.place(x=354, y=544)

    button_2 = Button(main, text='Example2', width='16',font=('Calibri',11), command=call_GUI2)
    button_2.place(x=572, y=544)

    button_3 = Button(main, text='Example3', width='16',font=('Calibri',11), command=call_GUI3)
    button_3.place(x=790, y=544)
    
    Quit=Button(main, text='Quit', width='8', font=('Calibri',11), command=destroy)
    Quit.place(x=603, y=633)
    
    main.mainloop()