# -----------------------------
# Program by Samodelkin
# -----------------------------
#    (-----ITEM------)
#       key:value

enemy = {
    'loc_x': 70,
    'loc_y': 50,
    'color': 'green',
    'health': 100,
    'name': 'SuperMan',
}

print(enemy)

print("location X = " + str(enemy['loc_x']))
print("location Y = " +str(enemy['loc_y']))
print("Name is " + (enemy['name']))

enemy['rank'] = 'Monstr'
print(enemy)

del enemy['rank']
print(enemy)

enemy['loc_x'] = enemy['loc_x'] + 40
enemy['health']-=30
if enemy['health'] < 80:
    enemy['color'] = 'yellow'



print(enemy.keys())
print(enemy.values())



