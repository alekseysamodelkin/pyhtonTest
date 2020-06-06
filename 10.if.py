# -----------------------------
# Program by Samodelkin
# -----------------------------

x = 15
if x == 25:
    print("yes")
else:
    print("no")

age = input("Age = ")
age = int(age)
if (age <= 7):
    print("baby")
elif (age > 7 and age < 12):
    print("kid")
elif (age > 12 and age < 20):
    print("teenager")
else:
    print("old")


all_cars = ['bmw','Kia', 'Lada', 'Izh', 'Man', 'Audi', 'vw', 'Ford']
german_cars = ['bmv', 'vw', 'Audi']

if 'Lada' in all_cars:
    print("Yes, Lada is here")
else:
    print("No Lada")

for xxx in all_cars:
    if xxx in german_cars:
        print(xxx + "  is German car")
    else:
        print(xxx + " is not German")


