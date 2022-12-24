from tkinter import *

import tkinter.messagebox as msgbox

from tkinter.filedialog import askopenfilename, asksaveasfilename

import os

import time

def newFile():

 global file

 root.title("Untilted - Notepad")

 TextArea.delete(1.0,END)

def openFile():

 global file

 file = askopenfilename(defaultextension = " .txt", filetypes=[("All files","*.*"),("Other Text Documents","*.txt")])

 if file =="":

  file =None

 else:

  root.title(os.path.basename(file)+ " - Notepad")

  f=open(file,"r")

  TextArea.insert(1.0, f.read())

  f.close()

def saveFile():

 global file

 if file == None:

  file = None

  file = asksaveasfilename(initialfile="Santosh.txt",defaultextension=".txt",     

  filetypes=[("All files","*.*"),("Other text documents",

  "*.txt")])

  if file =="":

   file =None

  else :

   f=open(file,"w")

   f.write(TextArea.get(1.0,END))

   f.close()

   root.title(os.path.basename(file) + " - Notepad")

 else:

  f=open(file,"w")

  f.write(TextArea.get(1.0,END))

  f.close()

def cut():

 TextArea.event_generate(("<<Cut>>"))

 

def copy():

 TextArea.event_generate(("<<Copy>>"))

 

def paste():

 TextArea.event_generate(("<<Paste>>"))

 

def about():

 msgbox.showinfo("Untilted - Notepad","HELLO EVERYONETHIS NOTEPAD\nIS CREATED BY SANTOSH BELAL \nTHE GREATEST IDIOT OF ALL TIME..")

 

def italic():

 value = msgbox.askretrycancel("Untilted - Notepad","SORRY THE FONT SERVICE\nIS NOT AVAILABLE YET\nWE WILL ADD THIS FEATURE\nIN UPCOMING FUTURE")

 if value==True:

  while True:

   time.sleep(1)

   value = msgbox.askretrycancel("Untilted - Notepad","SORRY THE FONT SERVICE\nIS NOT AVAILABLE YET\nWE WILL ADD THIS FEATURE\nIN UPCOMING FUTURE")

   if value == False:

    msgbox.showinfo("Untilted - Notepad","SORYY FOR THE INCONVENIENCE SERVICE")

    break

def bold():

 value = msgbox.askretrycancel("Untilted - Notepad","SORRY THE FONT SERVICE\nIS NOT AVAILABLE YET\nWE WILL ADD THIS FEATURE\nIN UPCOMING FUTURE")

 if value==True:

  while True:

   time.sleep(1)

   value = msgbox.askretrycancel("Untilted - Notepad","SORRY THE FONT SERVICE\nIS NOT AVAILABLE YET\nWE WILL ADD THIS FEATURE\nIN UPCOMING FUTURE")

   if value == False:

    msgbox.showinfo("Untilted - Notepad","SORYY FOR THE INCONVENIENCE SERVICE")

    break

def underline():

 value = msgbox.askretrycancel("Untilted - Notepad","SORRY THE FONT SERVICE\nIS NOT AVAILABLE YET\nWE WILL ADD THIS FEATURE\nIN UPCOMING FUTURE")

 if value==True:

  while True:

   time.sleep(1)

   value = msgbox.askretrycancel("Untilted - Notepad","SORRY THE FONT SERVICE\nIS NOT AVAILABLE YET\nWE WILL ADD THIS FEATURE\nIN UPCOMING FUTURE")

   if value == False:

    msgbox.showinfo("Untilted - Notepad","SORYY FOR THE INCONVENIENCE SERVICE")

    break

if __name__ == '__main__' :

 root = Tk()

 root.geometry("600x800")

 root.title("Untilted - Notepad")

 scrollbar = Scrollbar(root)

 scrollbar.pack(side = RIGHT ,fill =Y)

 MenuBar = Menu(root)

 TextArea = Text(root,font="lucida 8", yscrollcommand =scrollbar.set)

 file = None

 TextArea.pack(expand=True,fill="both")

 Filemenu= Menu(MenuBar)

 Filemenu.add_command(label="New", command=newFile)

 Filemenu.add_command(label="Open", command=openFile)

 Filemenu.add_command(label="Save", command=saveFile)

 Filemenu.add_separator()

 Filemenu.add_command(label="Exit", command=root.destroy)

 

 MenuBar.add_cascade(label="File",menu=Filemenu)

 Editmenu = Menu(MenuBar)

 Editmenu.add_command(label="Cut", command=cut)

 Editmenu.add_command(label="Copy", command=copy)

 Editmenu.add_command(label="Paste", command=paste)

 

 MenuBar.add_cascade(label="Edit", menu=Editmenu)

 

 Helpmenu = Menu(root)

 Helpmenu.add_command(label="About Notepad", command=about)

 MenuBar.add_cascade(label="Help", menu=Helpmenu)

 

 Fontmenu = Menu(MenuBar)

 Fontmenu.add_command(label="Italic", command=italic)

 Fontmenu.add_command(label="Bold", command=bold)

 Fontmenu.add_command(label="Underline", command=underline)

 

 MenuBar.add_cascade(label="Font",menu=Fontmenu)

 

 root.config(menu=MenuBar)

 scrollbar.config(command=TextArea.yview)

 root.mainloop()
