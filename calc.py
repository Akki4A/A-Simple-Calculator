
from tkinter import *
from tkinter import messagebox
############ BACKEND ############
opr = ""
A = 0
val = ""


def btClick(numbers):
    global val
    val = val + str(numbers)
    data.set(val)

def btPlusClick():
    global A
    global opr
    global val
    A = int(val)
    opr = "+"
    val = val + "+"
    data.set(val)

def btMinusClick():
    global A
    global opr
    global val
    A = int(val)
    opr = "-"
    val = val + "-"
    data.set(val)

def btMulClick():
    global A
    global opr
    global val
    A = int(val)
    opr = "*"
    val = val + "*"
    data.set(val)

def btDivClick():
    global A
    global opr
    global val
    A = int(val)
    opr = "/"
    val = val + "/"
    data.set(val)

def btCleardisp():
    global A
    global opr
    global val
    val = ""
    A = 0
    opr = ""
    data.set(val)

def btEqualsInput():
    global A
    global opr
    global val
    val2 = val
    if opr == "+":
        x = int((val2.split('+')[1]))
        C = A + x
        data.set(C)
        val = str(C)
    elif opr == "-":
        x = int((val2.split('-')[1]))
        C = A - x
        data.set(C)
        val = str(C)
    elif opr == "*":
        x = int((val2.split('*')[1]))
        C = A * x
        data.set(C)
        val = str(C)
    elif opr == "/":
        x = int((val2.split('/')[1]))
        if x == 0:
            messagebox.showerror("Error","Division by Zero is not Supported")
            A = ""
            val = ""
            data.set(val)
        else:
            C = int(A/x)
            data.set(C)
            val = str(C)



root = Tk()
root.geometry("300x400+300+300")
root.resizable(0,0)
root.title('Simple Calculator')

######## FRONT END #########
#main executing screen.
data = StringVar()
lbl = Label(root,text = "data", anchor = SE, font = ('Verdana',20),textvariable = data, bg = 'powder blue'
)
lbl.pack(expand = True, fill = 'both')

#Rows
btr1 = Frame(root, bg ="#000000") 
btr1.pack(expand = True, fill = 'both')

btr2 = Frame(root)
btr2.pack(expand = True, fill = 'both')

btr3 = Frame(root)
btr3.pack(expand = True, fill = 'both')

btr4 = Frame(root)
btr4.pack(expand = True, fill = 'both')

#Button row 1 
bt7 = Button(btr1,text = "7",font = ('Verdana', 22), relief = GROOVE, border = 0, command = lambda:btClick(7))
bt7.pack(side = LEFT, expand = True, fill = 'both')

bt8 = Button(btr1,text = "8",font = ('Verdana', 22), relief = GROOVE, border = 0, command = lambda:btClick(8))
bt8.pack(side = LEFT, expand = True, fill = 'both')

bt9 = Button(btr1,text = "9",font = ('Verdana', 22), relief = GROOVE, border = 0, command = lambda:btClick(9))
bt9.pack(side = LEFT, expand = True, fill = 'both')

btminus = Button(btr1,text = "-",font = ('Verdana', 22), relief = GROOVE, border = 0, command = btMinusClick)
btminus.pack(side = LEFT, expand = True, fill = 'both')


#Button row 2 
bt4 = Button(btr2,text = "4",font = ('Verdana', 22), relief = GROOVE, border = 0, command = lambda:btClick(4))
bt4.pack(side = LEFT, expand = True, fill = 'both')

bt5 = Button(btr2,text = "5",font = ('Verdana', 22), relief = GROOVE, border = 0, command = lambda:btClick(5))
bt5.pack(side = LEFT, expand = True, fill = 'both')

bt6 = Button(btr2,text = "6",font = ('Verdana', 22), relief = GROOVE, border = 0, command = lambda:btClick(6))
bt6.pack(side = LEFT, expand = True, fill = 'both')

btadd = Button(btr2,text = "+",font = ('Verdana', 22), relief = GROOVE, border = 0, command = btPlusClick)
btadd.pack(side = LEFT, expand = True, fill = 'both')


#Button row 3 
bt1 = Button(btr3,text = "1",font = ('Verdana', 22), relief = GROOVE, border = 0, command = lambda:btClick(1))
bt1.pack(side = LEFT, expand = True, fill = 'both')

bt2 = Button(btr3,text = "2",font = ('Verdana', 22), relief = GROOVE, border = 0, command = lambda:btClick(2))
bt2.pack(side = LEFT, expand = True, fill = 'both')

bt3 = Button(btr3,text = "3",font = ('Verdana', 22), relief = GROOVE, border = 0, command = lambda:btClick(3))
bt3.pack(side = LEFT, expand = True, fill = 'both')

btmul = Button(btr3,text = "*",font = ('Verdana', 22), relief = GROOVE, border = 0, command = btMulClick)
btmul.pack(side = LEFT, expand = True, fill = 'both')


#Button row 4
btclear = Button(btr4,text = "C",font = ('Verdana', 22), relief = GROOVE, border = 0, command = btCleardisp)
btclear.pack(side = LEFT, expand = True, fill = 'both')

bt0 = Button(btr4,text = "0",font = ('Verdana', 22), relief = GROOVE, border = 0, command = lambda:btClick(0))
bt0.pack(side = LEFT, expand = True, fill = 'both')

btdiv = Button(btr4,text = "/",font = ('Verdana', 22), relief = GROOVE, border = 0, command = btDivClick)
btdiv.pack(side = LEFT, expand = True, fill = 'both')

btequals = Button(btr4,text = "=",font = ('Verdana', 22), relief = GROOVE, border = 0, command = btEqualsInput)
btequals.pack(side = LEFT, expand = True, fill = 'both')



root.mainloop()
