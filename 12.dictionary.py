# -----------------------------
# Program by Samodelkin
# -----------------------------

enemy = {
    'loc_x': 70,
    'loc_y': 50,
    'color': 'green',
    'health': 100,
    'name': 'SuperMan',
    'awards': ['Za Stalona', 'Za otvagu'],
    'image': ['image1.jpg', 'image2.jpg', 'image3.jpg']
}

all_enemies = []

all_enemies.append(enemy)
all_enemies.append(enemy)
all_enemies.append(enemy)

for x in range(0,10):
    all_enemies.append(enemy.copy())

all_enemies[5]['health'] = 30
all_enemies[9]['name'] = 'Kozel'
all_enemies[4]['loc_x'] += 10

for en in all_enemies:
    print((en))

print(all_enemies)




