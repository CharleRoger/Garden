import os
from os.path import dirname
from fnmatch import fnmatch
import re

canonRoot = dirname(dirname(os.getcwd())) + "\\Canon"
pattern = "*.md"

linksToRemove = ["[[Universal calendar|AGS]]", "[[Universal calendar|BGS]]"]

for path, subdirs, files in os.walk(canonRoot):
    for filename in files:
        if not fnmatch(filename, pattern):
            continue
        fullpath = path + "\\" + filename
        fileEdited = False
        with open(fullpath, "r", encoding="utf8", newline='') as file:
            fileText = file.read()
            for link in linksToRemove:
                if link in fileText:
                    fileEdited = True
                    linkText = link.split('|')[1].replace("]]", "")
                    fileText = fileText.replace(link, linkText)
        if fileEdited:
            with open(fullpath, "w", encoding="utf8", newline='') as file:
                file.write(fileText)


"""
blah blah [[Universal Calendar|thing]]

[[Universal Calendar#AGS|AGS]]

[[Universal Calendar#year 0|the calendar]]

[[Universal Calendar|year 0]]
"""
