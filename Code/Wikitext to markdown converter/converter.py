import os
import re

inputLines = []
with open(os.getcwd() + "\Wikitext to markdown converter\input.txt", encoding='utf-8') as file:
    inputLines = file.readlines()

lineEnd = "£$%" # arbitrary string to match ends of a line, this is faster than regex(!?)
outputLines = []
for line in inputLines:
    if line == "\n" or line == "":
        continue
    line = lineEnd + line + lineEnd

    # Templates (for now just remove them, maybe do something elaborate with tables later)
    for template in re.findall('{{(.+?)}}', line):
        line = line.replace("{{" + template + "}}", "")

    # Unordered lists
    for i in [3, 2, 1]:
        line = line.replace(lineEnd + i * "*", lineEnd + (i - 1) * "\t" + "-")

    # Section headers
    for i in [3, 2, 1]:
        thing = i * "="
        line = line.replace(" " + thing + "\n" + lineEnd, "\n" + lineEnd)
        line = line.replace(lineEnd + thing + " ", lineEnd + (i - 1)*"#" + " ")

    # Bold and italics
    for i in [5, 3, 2]:
        thing = i * "'"
        line = line.replace(i * "'", (i - 1) * "*")

    # AGS and BGS
    line = line.replace(" AGS", " [[Universal calendar|AGS]]")
    line = line.replace(" BGS", " [[Universal calendar|BGS]]")

    line = line.replace(lineEnd, "")
    outputLines.append(line)

with open(os.getcwd() + "\Wikitext to markdown converter\output.txt", "w", encoding='utf-8') as file:
    file.writelines(outputLines)
