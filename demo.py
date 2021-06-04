from tkinter import *

window = Tk()
window.title("Your Calculator App")

#------Calculate Function-------
def cal():
    val1 = int(inp1.get("1.0", "end-1c"))
    val2 = int(inp2.get("1.0", "end-1c"))
    opt = varx.get()
    if(opt == 1):
        val = val1+val2
    elif(opt == 2):
        val = val1-val2
    elif(opt == 3):
        val = val1*val2
    elif(opt == 4):
        val = val1/val2
    l4.config(text=val)
    l4.place(x=400, y=190)
#-------------------------------

#-------Styling Of Window-------
canvas = Canvas(window, height=600, width=900, bg="#263D42")
canvas.pack()

frame = Frame(window, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

#-----------Header--------------
l0 = Label(window, text="Math-It", anchor=CENTER, fg="#f7050d", font="roman 28 bold", bg="#b3fa2f")
l0.place(relx=0.4, y=5)
#-------------------------------

#---------Inner Labels----------
l1 = Label(frame, text="Enter the 1st number:", font="times 17 bold")
l1.place(x=10, y=10)

l2 = Label(frame, text="Enter the 1st number:", font="times 17 bold")
l2.place(x=10, y=60)

l3 = Label(frame, text="The output is:", font="times 17 bold")
l3.place(x=90, y=190)

l4 = Label(frame, font="times 17 bold")
#-------------------------------

#---------Input Fields----------
inp1 = Text(frame, height=1, bg="#edebeb")
inp1.place(x=250, y=8, relwidth=0.64, relheight=0.08)

inp2 = Text(frame, height=1, bg="#edebeb")
inp2.place(x=250, y=58, relwidth=0.64, relheight=0.08)
#-------------------------------

#-------Radio buttons-----------
varx = IntVar()

R1 = Radiobutton(frame, text="Addition", variable=varx, value=1, background="light blue", command=cal)
R1.pack(side=TOP, ipady=5)
R1.place(x=50, y=130)

R2 = Radiobutton(frame, text="Subtraction", variable=varx, value=2, background="light blue", command=cal)
R2.pack(side=TOP, ipady=5)
R2.place(x=180, y=130)

R3 = Radiobutton(frame, text="Multiplication", variable=varx, value=3, background="light blue", command=cal)
R3.pack(side=TOP, ipady=5)
R3.place(x=330, y=130)

R4 = Radiobutton(frame, text="Division", variable=varx, value=4, background="light blue", command=cal)
R4.pack(side=TOP, ipady=5)
R4.place(x=490, y=130)
#-------------------------------


# -----------------------------
window.mainloop()