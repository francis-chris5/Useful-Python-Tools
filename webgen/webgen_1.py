
filename = input("Please, run this from the same directory as the script to be documented, and then input the filename here: ")


with open(filename, "r") as script:
    asString = ""
    for line in script:
        asString += line

lines = asString.split("\n")




for i in range(len(lines)):
    if(lines[i][0:3] == "def"):
        docstring = "    \"\"\"\n"
        docstring += "    DOCUMENTATION...\n"
        docstring += "    \"\"\""
        lines.insert(i + 1, docstring)
    elif("=" in lines[i] and lines[i][lines[i].index("=") + 1] == " "):
        docstring = "\"\"\""
        docstring += "DOCUMENTATION..."
        docstring += "\"\"\""
        lines.insert(i + 1, docstring)



lines.insert(0, "\"\"\"\n NAME\n\n ASSIGNMENT\n\n DATE\n\n PyVERSION\n\n \"\"\"\n")

print(lines)

with open(filename, "w") as documented:
    for l in lines:
        documented.write(l + "\n")












##############   WHITE SPACE FOR SCROLLING  ###############
