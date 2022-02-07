
import tkinter.filedialog as tkf

filename = tkf.askopenfilename()

update = "\"\"\"\n NAME\n\n ASSIGNMENT\n\n DATE\n\n PyVERSION\n\n \"\"\"\n"

with open(filename, "r") as script:
    for line in script:
        if line[0:3] == "def":
            docstring = "    \"\"\"\n"
            docstring += "        SUMMARY\n"
            if "(" in line:
                opening = line.index("(")
                closing = line.index(")")
                parameters = line[opening+1:closing].split(",")
                if len(parameters) > 1 or parameters[0] != "":
                    docstring += "    Args:\n"
                    for p in parameters:
                        docstring += "        " + p.strip() + " (TYPE): DESCRIPTION\n"
                docstring += "    Returns:\n        DESCRIPTION\n"
            docstring += "    \"\"\"\n"
            update += line + docstring
        elif "=" in line and line[line.index("=") + 1] == " ":
            docstring = "\"\"\""
            docstring += "DESCRIPTION"
            docstring += "\"\"\"\n"
            update += line + docstring
        else:
            update += line


with open(filename, "w") as documented:
        documented.write(update)












##############   WHITE SPACE FOR SCROLLING  ###############
