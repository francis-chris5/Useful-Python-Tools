# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 04:39:45 2020

@author: Christopher S. Francis
"""


##
# A method to check a python script and produce a list of the imported libraries.\n
# @param path The filepath for the python script to be checked
# @return <b>list</b> 
def checkDependencies(path):
    if path[-3:] != ".py":
        return False
    else:
        dependency = []
        with open(path, "r") as script:
            for line in script:
                if line[0:6] == "import":
                    line = line[7:]
                    dependency.append(line[0:-1])
                elif line[0:4] == "from":
                    line = line[5:]
                    dependency.append(line[0:line.index(" ")])
    return dependency


