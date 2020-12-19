import pygame
import numpy as np
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
x1 = [randint(80, 1620), randint(80, 1620)]
y1 = [randint(80, 820), randint(80, 820)]
vx1 = [0, 15]
vy1 = [15, 0]
a = 30
f = 0
color1 = [(randint(0, 255), randint(0, 255), randint(0, 255)), (randint(0, 255), randint(0, 255), randint(0, 255))]
pygame.display.update()
clock = pygame.time.Clock()
finished = False
t = 0
n = 0
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True     
    for i in range(5):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (event.pos[0] - x[i]) ** 2 + (event.pos[1] - y[i]) ** 2 < (r[i]) ** 2:
                n += 2 ** i
        if (x[i] + r[i] + vx[i]) > 1700 or 0 > (x[i] + vx[i] - r[i]):
                vx[i] *= -1
        if (y[i] + r[i] + vy[i]) > 900 or 0 > (y[i] - r[i] + vy[i]):
                vy[i] *= -1
        for p in range(4):
            if ((((x[i] + vx[i]) - (x[i - 1 - p] + vx[i - 1 - p])) ** 2 + ((y[i] + vy[i]) - (y[i - 1 - p] + vy[i - 1 - p])) ** 2) < (r[i] + r[i - 1 - p]) ** 2):
                vx[i] *= -1
                vy[i] *= -1
                vx[i - 1 - p] *= -1
                vy[i - 1 - p] *= -1
        circle(screen, color[i], (x[i], y[i]), r[i])
        x[i] += vx[i]
        y[i] += vy[i]
    for j in range(2):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if ((0 < (event.pos[0] - x1[j]) < a * 2) and (0 < (event.pos[1] - y1[j]) < a * 2)):
                n += 10
        if (x1[j] + a + vx1[j]) > 1700 or 0 > (x1[j] + vx1[j] - a):
                vx1[j] *= -1
        if (y1[j] + a + vy1[j]) > 900 or 0 > (y1[j] - a + vy1[j]):
                vy1[j] *= -1
        rect(screen, color1[j], (x1[j], y1[j], 2 * a, 2 * a))
        x1[j] += vx1[j]
        y1[j] += vy1[j]
        vx1[0] = np.cos(f)*15
        vy1[0] = np.sin(f)*15
        vx1[1] = np.sin(f)*15
        vy1[1] = np.cos(f)*15
        f += 0.1
        t += 1
        if t > 1000:
            R = open('results.txt', 'a')
            R.write(input("Введите имя:") + ' ' + 'Score:{}'.format(n) + '\n')
            R.close()
            n = 0
            t = 0
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render('Score:{}'.format(n), False, (100, 100, 100))
    screen.blit(textsurface, (0, 0))
    pygame.display.update()
    screen.fill(BLACK)
pygame.quit()
