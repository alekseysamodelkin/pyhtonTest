# -----------------------------
# Program by Samodelkin
# -----------------------------

cars = ['bmw', 'vw', 'seat', 'skoda', 'lada']

for x in cars:
    print(x.title())

for x in range(1, 6):
    print(x)

mynumberlist = list(range(0, 10))
print(mynumberlist)

for x in mynumberlist:
    x = x * 2
    print(x)
mynumberlist.sort(reverse=True)
print(mynumberlist)
print("max number is " + str(max(mynumberlist)))
print("sum of list is " + str(sum(mynumberlist)))

mycars = cars [1:4]
print(mycars)
mycars = cars [-3:]
print(mycars)


