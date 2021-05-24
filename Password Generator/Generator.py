from tkinter import *
import random


root = Tk()
root.iconbitmap('ICO/Elite Captain Black Shielded.ico')
color = "maroon"

root.geometry("500x300")
root.title("Welcome to Password Generator!")
root.config(bg=color)

# this method displays the copy button on the screen when the Generate button is clicked
# def showCopy():
	# copyBut = Button(inputFrame,text = 'Copy',anchor=W,bg='black',fg='white',activebackground='red')
	# copyBut.grid(row=0,column=2,padx=10,pady=5)

nums = '0123456789'
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
special = '!@#$%^&*()-=[];,./`_+:"<>?~'

def copy():
	root.clipboard_clear()
	root.clipboard_append(label.get())
	label.delete(0,END)



def gen():
	copyBut = Button(inputFrame,text = 'Copy',anchor=W,bg='black',fg='white',activebackground='red',command=copy)
	copyBut.grid(row=0,column=2,padx=10,pady=5)
	password =''
	genlis = ''	
	try:
		length = int(numEntry.get())
	except ValueError:
		length = 12
	if lval.get() == 1:
		genlis += lower
	if uval.get() == 1:
		genlis += upper
	if nval.get() == 1:
		genlis += nums
	if sval.get() == 1:
		genlis += special
	
	try:
		for i in range(1):
			password = ''
			for j in range(length):
				password += random.choice(genlis)
		label.delete(0,END)
		label.insert(END,password)
	except IndexError:
		label.delete(0,END)
		label.insert(0,"Please Select atleast one of the options")

fontTuple = ("Comic Sans MS",20,"bold")


mainLabel = Label(root,text = "Welcome to Password Generator",bg = color,font=fontTuple,pady = 20)
mainLabel.pack(side=TOP)


frame = Frame(root,bg=color)
frame.pack()

lval = IntVar()
uval = IntVar()
nval = IntVar()
sval = IntVar()

lCheck = Checkbutton(frame,text="Lowercase([a-z])",anchor=W,bg=color,activebackground = "red",variable=lval)
uCheck = Checkbutton(frame,text="Uppercase([A-Z])",anchor=W,bg=color,activebackground = "red",variable=uval)
nCheck = Checkbutton(frame,text="Numbers([0,9])",anchor=W,bg=color,activebackground = "red",variable=nval)
sCheck = Checkbutton(frame,text="Special Charecters([!,@,#,$,%,^,&,*... etc])",anchor=W,bg=color,activebackground = "red",variable=sval)


lCheck.grid(row=0,column=0)
uCheck.grid(row=0,column=1,sticky=W+E)
nCheck.grid(row=1,column=0,sticky=W+E)
sCheck.grid(row=1,column=1,sticky=W+E)


inputFrame = LabelFrame(root,text="Input the length of the password",bg=color,fg = 'cyan')
inputFrame.pack(padx=70,pady=10,anchor=W)

numEntry = Entry(inputFrame)
numEntry.grid(row=0,column=0,padx=10,pady=5)

button = Button(inputFrame,text = "Generate",anchor=W,bg='black',fg='white',activebackground='red',command=gen)
button.grid(row=0,column=1,padx=10,pady=5)

label = Entry(root,justify=CENTER,width=59)
label.pack(padx=10)

mainloop()