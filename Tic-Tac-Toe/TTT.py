from tkinter import *

root = Tk()
root.title("TTT")

fonTuple = ('Arial',15,'bold')


turn = True
xscore = 0
oscore = 0


def clicked(button):
    global turn
    if button["text"] == ' ' and turn==True:
        button["text"] = 'X'
        button.config(bg='purple')
        turn = False
    elif button["text"] == ' ':
        button["text"] = 'O'
        button.config(bg='blue')
        turn = True
    if turn == True:
        if(checkIfWonO()):
            disable(1)
    elif turn == False:
        if not (checkIfWonX()):
            disable(2)
def reset():
    b0.config(state=ACTIVE,text=' ',bg='SystemButtonFace')
    b1.config(state=ACTIVE,text=' ',bg='SystemButtonFace')
    b2.config(state=ACTIVE,text=' ',bg='SystemButtonFace')
    b3.config(state=ACTIVE,text=' ',bg='SystemButtonFace')
    b4.config(state=ACTIVE,text=' ',bg='SystemButtonFace')
    b5.config(state=ACTIVE,text=' ',bg='SystemButtonFace')
    b6.config(state=ACTIVE,text=' ',bg='SystemButtonFace')
    b7.config(state=ACTIVE,text=' ',bg='SystemButtonFace')
    b8.config(state=ACTIVE,text=' ',bg='SystemButtonFace')

def disable(choice):
    global xscore,oscore
    if choice==2:
        xscore += 1
        XScore.config(text=xscore,font=('Comic Sans MS',20,'bold'))
        XScore.grid(row=1,column=4,rowspan=1)
    elif choice==1:
        oscore += 1
        OScore.config(text=oscore,font=('Comic Sans MS',20,'bold'))
        OScore.grid(row=5,column=4,rowspan=1)
    b0.config(state=DISABLED)
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)


def checkIfWonO():
    k = False
    if b0['text'] == 'O' and b1['text'] == 'O' and b2['text'] == 'O':
        b0.config(bg='red')
        b1.config(bg='red')
        b2.config(bg='red')
        k = True
    if b3['text'] == 'O' and b4['text'] == 'O' and b5['text'] == 'O':
        b3.config(bg='red')
        b4.config(bg='red')
        b5.config(bg='red')
        k = True
    if b6['text'] == 'O' and b7['text'] == 'O' and b8['text'] == 'O':
        b6.config(bg='red')
        b7.config(bg='red')
        b8.config(bg='red')
        k = True
    if b0['text'] == 'O' and b3['text'] == 'O' and b6['text'] =='O':
        b0.config(bg='red')
        b3.config(bg='red')
        b6.config(bg='red')
        k = True
    if b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O':
        b1.config(bg='red')
        b4.config(bg='red')
        b7.config(bg='red')
        k = True
    if b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O':
        b2.config(bg='red')
        b5.config(bg='red')
        b8.config(bg='red')
        k = True
    if b0['text'] == 'O' and b4['text'] == 'O' and b8['text'] == 'O':
        b0.config(bg='red')
        b4.config(bg='red')
        b8.config(bg='red')
        k = True
    if b6['text'] == 'O' and b4['text'] == 'O' and b2['text'] == 'O':
        b6.config(bg='red')
        b4.config(bg='red')
        b2.config(bg='red')
        k = True
    return k
def checkIfWonX():
    k = True
    if b0['text'] == 'X' and b1['text'] == 'X' and b2['text'] == 'X':
        b0.config(bg='lime')
        b1.config(bg='lime')
        b2.config(bg='lime')
        k = False
    if b3['text'] == 'X' and b4['text'] == 'X' and b5['text'] == 'X':
        b3.config(bg='lime')
        b4.config(bg='lime')
        b5.config(bg='lime')
        k = False
    if b6['text'] == 'X' and b7['text'] == 'X' and b8['text'] == 'X':
        b6.config(bg='lime')
        b7.config(bg='lime')
        b8.config(bg='lime')
        k = False
    if b0['text'] == 'X' and b3['text'] == 'X' and b6['text'] =='X':
        b0.config(bg='lime')
        b3.config(bg='lime')
        b6.config(bg='lime')
        k = False
    if b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X':
        b1.config(bg='lime')
        b4.config(bg='lime')
        b7.config(bg='lime')
        k = False
    if b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X':
        b2.config(bg='lime')
        b5.config(bg='lime')
        b8.config(bg='lime')
        k = False
    if b0['text'] == 'X' and b4['text'] == 'X' and b8['text'] == 'X':
        b0.config(bg='lime')
        b4.config(bg='lime')
        b8.config(bg='lime')
        k = False
    if b6['text'] == 'X' and b4['text'] == 'X' and b2['text'] == 'X':
        b6.config(bg='lime')
        b4.config(bg='lime')
        b2.config(bg='lime')
        k = False
    return k

b0 = Button(root,text=' ',height=6,width=12,font=fonTuple,command=lambda:clicked(b0))
b0.grid(row=0,column=0,rowspan=2)
b1 = Button(root,text=' ',height=6,width=12,font=fonTuple,command=lambda:clicked(b1))
b1.grid(row=0,column=1,rowspan=2)
b2 = Button(root,text=' ',height=6,width=12,font=fonTuple,command=lambda:clicked(b2))
b2.grid(row=0,column=2,rowspan=2)

b3 = Button(root,text=' ',height=6,width=12,font=fonTuple,command=lambda:clicked(b3))
b3.grid(row=2,column=0,rowspan=2)
b4 = Button(root,text=' ',height=6,width=12,font=fonTuple,command=lambda:clicked(b4))
b4.grid(row=2,column=1,rowspan=2)
b5 = Button(root,text=' ',height=6,width=12,font=fonTuple,command=lambda:clicked(b5))
b5.grid(row=2,column=2,rowspan=2)

b6 = Button(root,text=' ',height=6,width=12,font=fonTuple,command=lambda:clicked(b6))
b6.grid(row=4,column=0,rowspan=2)
b7 = Button(root,text=' ',height=6,width=12,font=fonTuple,command=lambda:clicked(b7))
b7.grid(row=4,column=1,rowspan=2)
b8 = Button(root,text=' ',height=6,width=12,font=fonTuple,command=lambda:clicked(b8))
b8.grid(row=4,column=2,rowspan=2)

X  = Label(root,text='X',font=('Comic Sans MS',20,'bold'))
X.grid(row=0,column=4,rowspan=1)
XScore = Label(root,text=" ")

O  = Label(root,text='O',font=('Comic Sans MS',20,'bold'))
O.grid(row=4,column=4,rowspan=1)
OScore = Label(root,text=" ")




resetButton = Button(root,text='RESET',height=6,width=10,font=fonTuple,command=reset)
resetButton.grid(row=2,column=4,rowspan=1)

mainloop()