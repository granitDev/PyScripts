#! /usr/bin/python

import os

ignoreList = ["title_names.py", "mm"]
exitList = ["exit", "EXIT", "done", "DONE", "n", "no", "N", "NO","Quit","quit","Q","q"]
helpList = ["-h","--help","help","man","h"]

helpText = """
-------------------------------------------------------
Enter a complete file path into the directory of which
you want the contents to be renamed in 'title' format.

File extensions will be ignored.

Title File Names is not recursive.
Sub directories will be renamed but not their contents.
-------------------------------------------------------

"""

def getDirLoc():
    dirLoc = input("Which directory to rename?\n")
    if dirLoc in helpList:
        print(helpText)
        return getDirLoc()
    if dirLoc in exitList:
        exit(0)
    return dirLoc

location = getDirLoc()

while True:
    location += "\\"

    for file in os.listdir(location):
        newName = file.lower()
        wordList = newName.split(" ")
        newName = ""
        print(wordList)
        for w in wordList:
            if w not in ignoreList:
                if w[0].isalpha():
                    cList = list(w)
                    cList[0] = cList[0].title()
                    w = "".join(cList)
                    newName += w + " "
                else:
                    newName += w + " "
            else:
                newName += w + " "
        print("Renaming " + file + " to " + newName)
        file = location + file
        newName = location + newName
        os.rename(file, newName)

    location = getDirLoc()

exit(0)