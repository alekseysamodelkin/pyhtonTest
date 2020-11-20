# -----------------------------
# Program by Samodelkin
# -----------------------------

import pygame

max_x = 1600
max_y = 1200

pygame.init()

screen = pygame.display.set_mode((max_x, max_y)) #pygame.FULLSCREEN)
pygame.display.set_caption("Samodelkin's game :)")

print(pygame.image.get_extended())

my_image = pygame.image.load("0127.png").convert()

x = 10
y = 200
bg_color = (0, 100, 0)

game_over = False

while game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
            if event.key == pygame.K_LEFT:
                x -= 20
            if event.key == pygame.K_RIGHT:
                x += 20
            if event.key == pygame.K_UP:
                y -= 20
            if event.key == pygame.K_DOWN:
                y += 20
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

    screen.fill(bg_color)
    screen.blit(my_image, (x, y))
    pygame.display.flip()
