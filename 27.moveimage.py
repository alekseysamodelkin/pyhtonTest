# -----------------------------
# Program by Samodelkin
# -----------------------------

import pygame

max_x = 1600
max_y = 1200
IMG_SIZE_L = 200
IMG_SIZE_U = 100

pygame.init()

screen = pygame.display.set_mode((max_x, max_y)) #pygame.FULLSCREEN)
pygame.display.set_caption("Samodelkin's game :)")

print(pygame.image.get_extended())

my_image = pygame.image.load("0127.png").convert()
my_image = pygame.transform.scale(my_image, (IMG_SIZE_L, IMG_SIZE_U))

x = 10
y = 200
bg_color = (0, 100, 0)

move_right = False
move_left = False
move_down = False
move_up = False

game_over = False

while game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_UP:
                move_up = True
            if event.key == pygame.K_DOWN:
                move_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_UP:
                move_up = False
            if event.key == pygame.K_DOWN:
                move_down = False

    if move_left:
        x -= 1
        if x < 0:
            x = 0

    if move_right:
        x +=1
        if x > max_x-IMG_SIZE_L:
            x = max_x-IMG_SIZE_L

    if move_up:
        y -= 1
        if y < 0:
            y = 0

    if move_down:
        y += 1
        if y > max_y - IMG_SIZE_U:
            y = max_y - IMG_SIZE_U



    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = event.pos

    screen.fill(bg_color)
    screen.blit(my_image, (x, y))
    pygame.display.flip()