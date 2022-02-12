# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 10:35:50 2022

@author: c.s.francis
@version: Python 3.10.2
"""


from tkinter import *
from ClassGenerator import *


class ClassGenerator():
    def __init__(self, gui=Tk()):
        gui.geometry("567x321")
        
        self.pnMainContent = Frame(gui)
        
        
        
            #################  INPUTS  ###############################
            
        self.lblModule = Label(self.pnMainContent, text="Module: \n(goes in a file with 'myModule' if left blank)")
        self.txtModule = Entry(self.pnMainContent)
        self.lblClassName = Label(self.pnMainContent, text="Class Name: ")
        self.txtClassName = Entry(self.pnMainContent)
        self.lblParent = Label(self.pnMainContent, text="Parent Class: ")
        self.txtParent = Entry(self.pnMainContent)
        self.lblAttributes = Label(self.pnMainContent, text="Parameters:\n(enter a comma separated list) ")
        self.txtAttributes = Entry(self.pnMainContent)
        self.lblDirectory = Label(self.pnMainContent, text="Filepath: \n(goes in a folder called 'myDirectory' if left blank')")
        self.txtDirectory = Entry(self.pnMainContent)
        
        
            ###################  CONTROLS  ###########################
            
        self.btnGenerate = Button(self.pnMainContent, text="Generate Class")
        self.btnGenerate.bind("<Button-1>", lambda event: self.GenerateClass(event, gui))
        
        
            #################  LAYOUT  ###################################
            
        self.pnMainContent.pack()
        #self.lblModule.grid(row=0, column=0, pady=5)
        #self.txtModule.grid(row=0, column=1, pady=5)
        self.lblClassName.grid(row=1, column=0, pady=5)
        self.txtClassName.grid(row=1, column=1, pady=5)
        self.lblParent.grid(row=2, column=0, pady=5)
        self.txtParent.grid(row=2, column=1, pady=5)
        self.lblAttributes.grid(row=3, column=0, pady=5)
        self.txtAttributes.grid(row=3, column=1, pady=5)
        #self.lblDirectory.grid(row=4, column=0, pady=5)
        #self.txtDirectory.grid(row=4, column=1, pady=5)
        self.btnGenerate.grid(row=5, column=0, columnspan=2, pady=15)
        
        
        
            #################  RUN...  ########################
        gui.mainloop()
        
        
    def GenerateClass(self, event, gui):
        module = self.txtModule.get()
        className = self.txtClassName.get()
        parent = self.txtParent.get()
        attributes = self.txtAttributes.get()
        if attributes != "":
            attributes = attributes.split(",")
        directory = self.txtDirectory.get()
        if className == "":
            dlgNoName = Toplevel(gui)
            dlgNoName.geometry("350x180")
            lblMessage = Label(dlgNoName, text="A classname is required")
            lblMessage.pack(pady=25)
        else:
            if module == "" and parent == ""and attributes=="" and directory == "":
                startClass(name=className)
            elif module == "" and parent == "" and directory == "":
                startClass(name=className, attributes=attributes)
            elif module == "" and directory == "":
                startClass(name=className, parent=parent, attributes=attributes)
            elif directory=="":
                startClass(module=module, name=className, parent=parent, attributes=attributes)
                
        
        
        
        
if __name__=="__main__":
    classgen = ClassGenerator()
        