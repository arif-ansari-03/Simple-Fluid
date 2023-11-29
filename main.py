import pygame
import time

#### update func

def update_water(waterh, waterv, c, s):
    global maxh

    if (len(water) == 1):
        return
    water[0] = water[1]
    water[-1] = water[-2]

    k = c**2 / s**2
    del_t = 1
    b = 0.02

    for i in range(len(water)):
        if i-1 < 0 or i+1 >= len(water):
            continue
        ai = k * (water[i-1] + water[1+i] - 2 * water[i]) - b * waterv[i]
        waterv[i] = waterv[i] + ai * del_t
        waterh[i] = waterh[i] + (waterv[i] * del_t)

        if waterh[i] > maxh:
            waterh[i] = maxh

        if waterh[i] < 0:
            waterh[i] = 0

pygame.init()
screen = pygame.display.set_mode((500, 400))


n = 240
water = [20 for x in range(n//2)] + [50 for x in range(n//2)]
waterv = n * [0]

maxh = 100
offset = 100
width = 2

i = 0

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            
    if not running:
        break

    screen.fill(pygame.Color(0, 0, 0, 0))
    for i in range(len(water)):
        # Rect(left, top, width, height)
        column = pygame.Rect(width*i, maxh-water[i]*2 + offset, width, water[i]*2+offset)
        pygame.draw.rect(screen, pygame.Color(100, 100, 255, 255), column)       

    update_water(water, waterv, 1, 10) 


    if running:
        pygame.display.update()

