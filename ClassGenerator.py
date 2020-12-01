# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 10:07:27 2020

@author: Chris
"""

def startClass(module="myModule", name="myClass", parent="", attributes=[]):
    with open(module + ".py", mode="a") as createClass:
        createClass.write("\n")
        createClass.write("\n")
        createClass.write("\n")
        createClass.write("class " + name + "(" + parent + "):\n")
        createClass.write("\tdef __init__(self, ")
        for att in attributes:
            if att != attributes[-1]:
                createClass.write(att + ", ")
            else:
                createClass.write(att + "):\n")
    
        for att in attributes:
            createClass.write("\t\tself.__" + att + " = " + att + "\n")
            

        for att in attributes:
            createClass.write("\n")
            first = att[0]
            createClass.write("\tdef get" + att.replace(first, first.upper(), 1) + "(self):\n")
            createClass.write("\t\treturn self.__" + att + "\n")
            
        for att in attributes:
            createClass.write("\n")
            first = att[0]
            createClass.write("\tdef set" + att.replace(first, first.upper(), 1) + "(self, " + att + "):\n")
            createClass.write("\t\tself.__" + att + " = " + att +"\n")
        
    