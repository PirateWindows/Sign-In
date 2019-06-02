import datetime
import tkinter
from PIL import Image,ImageTk

m = tkinter.Tk()
m.iconbitmap('download.ico')
m.title("Sign-In")
Name = tkinter.Label(m, text = "Name: ")
Apartment = tkinter.Label(m, text = "Apartment: ")
Guests = tkinter.Label(m, text = "# of Guests")



NameIn = tkinter.Entry(m)
ApartmentIn = tkinter.Entry(m)
GuestsIn = tkinter.Entry(m)
def DocumentWrite():
    file = open("Sign-In", "a+")
    date = datetime.datetime.now()
    file.write(NameIn.get()+"\t\t\t" + ApartmentIn.get()+"\t"+GuestsIn.get() +"\t" + str(date) +"\n")
    NameIn.delete(first = 0, last = 50)
    ApartmentIn.delete(first=0, last=50)
    GuestsIn.delete(first=0, last=50)
    file.close()

DoneBtn = tkinter.Button(m, text = "Done", width= 50, command = DocumentWrite)
Name.grid()
NameIn.grid(row =0, column=1)
Apartment.grid()
ApartmentIn.grid(row =1, column=1)
Guests.grid()
GuestsIn.grid(row = 2, column = 1)
DoneBtn.grid()


m.mainloop()

