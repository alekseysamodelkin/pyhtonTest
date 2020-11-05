# -----------------------------
# Program by Samodelkin
# -----------------------------

def napechatat_privet(name):
    """Print Privet"""
    print("Wish You all the best!!!" + name)
    print("Hello hello hello")


def summa(x, y):
    return x+y


def factorial(i):
    """calculate factorial of number I"""
    otvet = 1
    for i in range(1, i + 1):
        otvet = otvet * i
    return otvet



print("______________________")
napechatat_privet("Samodelkin")
napechatat_privet("Aleksey")

x =summa(22,33)
print(factorial(5))


for i in range (1, 20+1):
    print(str(i) + " !\t = " + str(factorial(i)))








