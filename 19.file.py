# -----------------------------
# Program by Samodelkin
# -----------------------------

inputfile = "c:\pass.txt"
outputfile = "c:\/aaa\pass2.txt"
myfile = open(inputfile, mode='r', encoding='ascii')
myfile2 = open(outputfile, mode='w', encoding='latin-1')  #mode a (append)
# print((myfile.read()))

for num, line in enumerate(myfile, 1):
    if "Samodelkin" in line:
        print("Hello " + str(num) + "  ", line.strip())
        myfile2.write("Found Samodelkin " + line)
    else:
        print("line " + line.strip())

myfile.close()
myfile2.close()