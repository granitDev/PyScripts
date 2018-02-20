#! /usr/bin/python

import os

ignoreList = ["title_names.py", "mm"]
exitList = ["exit", "EXIT", "done", "DONE", "n", "no", "N", "NO","Quit","quit","Q","q"]
helpList = ["-h","--help","help","man","h"]

helpText = """
--------------------------------------------------------
Enter a complete file path into the directory of which
you want the contents to be appended with a suffix.

You will then be asked for the suffix text to append.
Suffixes are appended before the extension.

Append Suffix is not recursive.
Sub directories will be renamed but not their contents.
--------------------------------------------------------

"""

suffix = ""

def getDirLoc():
    global suffix
    dirLoc = input("This will add a suffix to all files in a directory\n Directory?\n")
    if dirLoc in helpList:
        print(helpText)
        return getDirLoc()
    if dirLoc in exitList:
        exit(0)
    suffix = input("Suffix: ")
    return dirLoc

location = getDirLoc()

while True:
    location += "\\"

    for file in os.listdir(location):
        newName = file
        dotIdx = file.rfind(".")
        newName = file[:dotIdx] + suffix + file[dotIdx:]
        print(newName)
        file = location + file
        newName = location + newName
        print(newName)
        os.rename(file, newName)

    location = getDirLoc()

exit(0)