# def foo(a, b=4, c=6): 
#     print(a, b, c)
 
# foo(1)

from tkinter import *

window = Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)

#Label

my_label = Label(text="New Text", font=("Arial",24,"bold"))
my_label.pack()

#Button

def button_clicked():
    #my_label.config(text="Button got clicked")
    my_label.config(text=input.get())

button = Button(text="Click me",command=button_clicked)
button.pack()

##Entry

input = Entry(width=10)
input.insert(END,string="Some text to begin:") #some starting text to begin
print(input.get()) ##get the text string
input.pack()

#Text

text = Text(height = 5, width=30)
text.focus() #Put cursor in the box
text.insert(END, "Example of multi line text")
print(text.get("1.0",END)) ##Starting from the first line from character zero
text.pack()

#Spinbox

def spinbox_used():
    print(spinbox.get())

spinbox = Spinbox(from_=0,to=10,width=5,command=spinbox_used)
spinbox.pack()

#Scale

def scale_used(value):
    print(value)

scale = Scale(from_=0,to=100,command=scale_used)
scale.pack()

#Checkbutton

def checkbutton_used():
    print(checked_state.get())

checked_state = IntVar() #this is a class

checkbutton = Checkbutton(text="Is On ?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton

def radiobutton_used():
    print(radio_state.get())

radio_state = IntVar()

radiobutton1 = Radiobutton(text="Option1",value=1,variable=radio_state,command=radiobutton_used)
radiobutton2 = Radiobutton(text="Option2",value=2,variable=radio_state,command=radiobutton_used)
radiobutton1.pack()
radiobutton2.pack()

#Listbox

def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ['Apple','Orange','Banana','Pear']

for item in fruits:
    listbox.insert(fruits.index(item),item)

listbox.bind("<<ListboxSelect>>",listbox_used)
listbox.pack()


window.mainloop()