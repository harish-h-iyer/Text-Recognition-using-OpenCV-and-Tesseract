from tkinter import *
from tkinter.filedialog import askopenfilename
import cv2
import sys
import pytesseract

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Version 1.0")
   button.pack()

def images():

    file1 = None

    file1=askopenfilename()

    if __name__ == '__main__':

      imPath = file1

    def sel():
       selection = "Enter the file name to save :"
       label.config(text = selection)
       if var.get() == 1:
           config = ('-l eng --oem 1 --psm 3')
           im = cv2.imread(imPath, cv2.IMREAD_COLOR)
           text = pytesseract.image_to_string(im, config=config)
           def clicked():
               Input = entry1.get()
               FileName = str(Input + ".txt")
               TextFile = open(FileName,"w")
               with open(FileName, 'w') as f:
                   print(text, file=f)

           entry1 = Entry(root)
           button1 = Button(root,text="Save to a file", command = clicked)
           entry1.pack()
           button1.pack()


       elif var.get() == 2:
           config = ('-l hin --oem 1 --psm 3')
           im = cv2.imread(imPath, cv2.IMREAD_COLOR)
           text = pytesseract.image_to_string(im, config=config)
           def clicked():
               Input = entry1.get()
               FileName = str(Input + ".txt")
               TextFile = open(FileName,"w")
               with open(FileName, 'w') as f:
                   print(text, file=f)

           entry1 = Entry(root)
           button1 = Button(root,text="Save to a file", command = clicked)
           entry1.pack()
           button1.pack()

       elif var.get() == 3:
           config = ('-l tam --oem 1 --psm 3')
           im = cv2.imread(imPath, cv2.IMREAD_COLOR)
           text = pytesseract.image_to_string(im, config=config)
           def clicked():
               Input = entry1.get()
               FileName = str(Input + ".txt")
               TextFile = open(FileName,"w")
               with open(FileName, 'w') as f:
                   print(text, file=f)

           entry1 = Entry(root)
           button1 = Button(root,text="Save to a file", command = clicked)
           entry1.pack()
           button1.pack()

       elif var.get() == 4:
           config = ('-l tel --oem 1 --psm 3')
           im = cv2.imread(imPath, cv2.IMREAD_COLOR)
           text = pytesseract.image_to_string(im, config=config)
           def clicked():
               Input = entry1.get()
               FileName = str(Input + ".txt")
               TextFile = open(FileName,"w")
               with open(FileName, 'w') as f:
                   print(text, file=f)

           entry1 = Entry(root)
           button1 = Button(root,text="Save to a file", command = clicked)
           entry1.pack()
           button1.pack()


    var = IntVar()
    R1 = Radiobutton(root, text="English", variable=var, value=1,
                      command=sel)
    R1.pack( anchor = W )

    R2 = Radiobutton(root, text="Hindi", variable=var, value=2,
                      command=sel)
    R2.pack( anchor = W )

    R3 = Radiobutton(root, text="Tamil", variable=var, value=3,
                      command=sel)
    R3.pack( anchor = W)

    R4 = Radiobutton(root, text="Telugu", variable=var, value=4,
                      command=sel)
    R4.pack( anchor = W)

    label = Label(root)
    label.pack()

root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Run", command=images)

menubar.add_cascade(label="Image", menu=filemenu)


helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
root.mainloop()
