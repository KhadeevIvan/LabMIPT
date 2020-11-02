import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 60
screen = pygame.display.set_mode((1700, 900))

BLACK = (0, 0, 0)
x = [randint(80, 1620), randint(80, 1620), randint(80, 1620), randint(80, 1620), randint(80, 1620)]
y = [randint(80, 820), randint(80, 820), randint(80, 820), randint(80, 820), randint(80, 820)]
vx = [randint(5, 10), randint(10, 12), randint(12, 15), randint(15, 17), randint(17, 20)]
vy = [randint(0, 15), randint(0, 15), randint(0, 15), randint(0, 15), randint(0, 15)]
r = [60, 50, 40, 30, 20]
color = [(randint(0, 255), randint(0, 255), randint(0, 255)), (randint(0, 255), randint(0, 255), randint(0, 255)), (randint(0, 255), randint(0, 255), randint(0, 255)), (randint(0, 255), randint(0, 255), randint(0, 255)), (randint(0, 255), randint(0, 255), randint(0, 255))]
pygame.display.update()
clock = pygame.time.Clock()
finished = False
n = 0
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True     
    for i in range(0, 5):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (event.pos[0] - x[i]) ** 2 + (event.pos[1] - y[i]) ** 2 < (r[i]) ** 2:
                n += 2 ** i
        if (x[i] + r[i] + vx[i]) > 1700 or 0 > (x[i] + vx[i] - r[i]):
                vx[i] *= -1
        elif (y[i] + r[i] + vy[i]) > 900 or 0 > (y[i] - r[i] + vy[i]):
                vy[i] *= -1
        circle(screen, color[i], (x[i], y[i]), r[i])
        x[i] += vx[i]
        y[i] += vy[i]
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render('Score:{}'.format(n), False, (100, 100, 100))
    screen.blit(textsurface, (0, 0))
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
