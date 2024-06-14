# def foo(a, b=4, c=6): 
#     print(a, b, c)
 
# foo(1)

from tkinter import *

def button_clicked():
    km = round(int(input.get())*1.6)
    conversion.config(text=f"{km}")

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=250, height=150)
window.config(padx=20,pady=20)

#Label

miles = Label(text="Miles", font=("Arial",10,"normal"))
miles.grid(column=2,row=0)

is_equal_to = Label(text="is equal to", font=("Arial",10,"normal"))
is_equal_to.grid(column=0,row=1)

conversion = Label(text="0", font=("Arial",10,"normal"))
conversion.grid(column=1,row=1)

KM = Label(text="Km", font=("Arial",10,"normal"))
KM.grid(column=2,row=1)

#Button

button = Button(text="Calculate",command=button_clicked)
button.grid(column=1,row=3)

##Entry

input = Entry(width=5)
#input.insert(END,string="Some text to begin:") #some starting text to begin
print(input.get()) ##get the text string
input.grid(column=1,row=0)


window.mainloop()