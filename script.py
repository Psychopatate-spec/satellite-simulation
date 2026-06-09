import pygame
import math
import time

starttime = time.time()

pygame.init()

screen = pygame.display.set_mode((800, 600))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Handle satellites movement here
    #"1" is for the first satellite, "2" for the second

    Pos01 = pygame.math.Vector2(400, 300)
    Pos01 = pygame.math.Vector2(400, 100)

    M1 = 1
    M2 = 1
    G = 6.674*10**(-11)

    dt = time.time() - starttime

    r = 400
    f = G*M1*M2/r**2

    a1 = G*M2/r**2
    a2 = G*M1/r**2

    v1 = 

    screen.fill((0, 0, 0))

    #Draw satellites here

    pygame.display.flip()

pygame.quit()