# -----------------------------
# Program by Samodelkin
# -----------------------------
import re

filename = "test.txt"
inputfile = open(filename, mode="r", encoding="UTF-8")

resultfilename = "result.txt"
resultfile = open(resultfilename, mode="w", encoding="UTF-8")

lookfor = r"[\w.-]+@\w+"

mytext = inputfile.read()

results = re.findall(lookfor, mytext)

for item in results:
    print(item)
    resultfile.write(item +"\n")



