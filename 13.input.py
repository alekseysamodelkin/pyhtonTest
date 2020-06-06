# -----------------------------
# Program by Samodelkin
# --------------------------

name = input("Enter your name: ")

print("Privet, " + name)

Num1 = input("Enter X: ")
Num2 = input("Enter Y: ")

Summa = int(Num1) + int(Num2)

print(Summa)

message = ""

while True:
    message = input("Enter passwd ")
    if message == 'da':
        break
    print(message + " passwd was incorrect")

print("passwd was " + message)

mylist = []
msg = ""

while msg != 'stop'.upper():
    msg = input("enter new item and STOP to finish ")
    mylist.append(msg)

print(mylist)







