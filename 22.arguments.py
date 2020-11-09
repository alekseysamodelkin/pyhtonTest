# -----------------------------
# Program by Samodelkin
# -----------------------------
import sys
import os

print("hello")

print(sys.argv[1:])

x = len(sys.argv)
if x > 1:
    if sys.argv[1] == "/?":
        print("Help argument")
    print("Arguments entered: " +str(sys.argv[1:]))
else:
    print("Arguments not provided")

os.system("dir > test.txt")
os.mkdir("22.place")
sys.exit()

