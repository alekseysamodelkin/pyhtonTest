# -----------------------------
# Program by Samodelkin
# -----------------------------

cities = ['New York', 'Moscow', "new dehly", 'Simferopol', 'Toronto']
print(cities)
print(len(cities))

print(cities[0])

print(cities[2].title())

cities[2] = "Tula"

print(cities)

cities.append('Kursk')
cities.append('Yalta')

print(cities)

cities.insert(2, 'SPb')
print(cities)

del cities[-2]
print(cities)

cities.remove('Tula')
print(cities)

cities.sort(reverse=True)

print(cities)



