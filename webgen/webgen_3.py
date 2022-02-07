
import tkinter.filedialog as tkf

indentation = 0
def Indent(level):
    dents = ""
    for i in range(level):
        """ Uncomment the appropriate indentataion type for your IDE"""
        ##dents += "\t"
        dents += "    "
    return dents


filename = tkf.askopenfilename()

update = "\"\"\"\n NAME\n\n ASSIGNMENT\n\n DATE\n\n PyVERSION\n\n \"\"\"\n"

with open(filename, "r") as script:
    for line in script:
        if line[0:3] == "def":
            indentation += 1
            docstring = Indent(indentation) + "\"\"\"\n"
            docstring += Indent(indentation + 1) + "SUMMARY\n"
            if "(" in line:
                opening = line.index("(")
                closing = line.index(")")
                parameters = line[opening+1:closing].split(",")
                if len(parameters) > 1 or parameters[0] != "":
                    docstring += Indent(indentation) + "Args:\n"
                    for p in parameters:
                        docstring += Indent(indentation + 1) + p.strip() + " (TYPE): DESCRIPTION\n"
                docstring += Indent(indentation) + "Returns:\n" + Indent(indentation + 1) + "DESCRIPTION\n"
            docstring += Indent(indentation) + "\"\"\"\n"
            update += line + docstring
            indentation -= 1
        elif "=" in line and line[line.index("=") + 1] == " " and line[line.index("=") - 1] == " ":
            docstring = "\"\"\""
            docstring += "DESCRIPTION"
            docstring += "\"\"\"\n"
            update += line + docstring
        else:
            update += line


with open(filename, "w") as documented:
        documented.write(update)












##############   WHITE SPACE FOR SCROLLING  ###############
