# -----------------------------
# Program by Samodelkin
# -----------------------------
import  sys

filename = "anketaa.py"
while True:

    try:
        print("Inside TRY")
        myfile = open(filename, mode='r')
    except Exception:
        print("Inside Except")
        print("Error found")
        print(sys.exc_info()[1])
#    sys.exit()
        filename = input("Enter correct filename!")
    else:
        print("Inside Else")
        print(myfile.read())
        sys.exit()
    finally:
        print("inside Finally")

print("___________END___________")

