import numpy as np
import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1500, 750))

rect(screen, (0, 255, 255), (0, 0, 1500, 375))
rect(screen, (0, 0, 153), (0, 375, 1500, 175))
rect(screen, (255, 255, 0), (0, 550, 1500, 200))
for j in range(37):
    c = j * np.pi / 36
    polygon(screen, (255, 255, 0),[(int(1200 + 100 * np.cos(c)), int(150 - 100 * np.sin(c))), (int(1200 + 100 * np.cos(np.pi * 2 / 3 + c)), int(150 - 100 * np.sin(np.pi * 2 / 3 + c))), (int(1200 + 100 * np.cos(np.pi * 4 / 3 + c)), int(150 - 100 * np.sin(np.pi * 4 / 3 + c)))])
for i in range(15):
    circle(screen, (255, 255, 0), (40 + 160 * i, 580), 50)
    circle(screen, (0, 0, 153), (120 + 160 * i, 520), 50)
def ship(spx, spy, sl, sw):
    polygon(screen, (102, 51, 0), [(spx, spy), (spx + sl * 4, spy), (spx + sl * 3, spy + sw), (spx, spy + sw)])
    arc(screen, (102, 51, 0), (spx - sw, spy - sw, 2 * sw, 2 * sw), np.pi, 1.5 * np.pi, sw)
    circle(screen, (0, 0, 0), (spx + sl * 3, spy + int(sw / 2)), int(0.4 * sw))
    circle(screen, (255, 255, 255), (spx + sl * 3, spy + int(sw / 2)), int(0.3 * sw))
    rect(screen, (0, 0, 0), (spx + sl, spy - 3 * sw, int(sl / 10), 3 * sw))
    polygon(screen, (204, 204, 204), [(spx + sl + int(sl / 10), spy - 3 * sw), (spx + int(sl * 1.2), spy - int(1.5 * sw)), (spx + sl + int(sl / 10), spy), (spx + sl * 2, spy - int(1.5 * sw))])
def cloud(clx, cly, a, b):
    ellipse(screen,(255, 255, 255), (clx, cly, 4 * a, 4 * b))
    ellipse(screen,(255, 255, 255), (clx + a, cly - 2 * b, 4 * a, 4 * b))
    ellipse(screen,(255, 255, 255), (clx + 2 * a, cly, 4 * a, 4 * b))
    ellipse(screen,(255, 255, 255), (clx + 3 * a, cly - 2 * b, 4 * a, 4 * b))
    ellipse(screen,(255, 255, 255), (clx + 4 * a, cly, 4 * a, 4 * b))
    ellipse(screen,(255, 255, 255), (clx + 5 * a, cly - 2 * b, 4 * a, 4 * b))
    ellipse(screen,(255, 255, 255), (clx + 6 * a, cly, 4 * a, 4 * b))
def umbrella(umx, umy, ul, uw):
    rect(screen, (102, 51, 0), (umx, umy, ul * 2, uw * 3))
    polygon(screen, (204, 51, 51), [(umx + ul, umy - uw), (umx + 16 * ul, umy), (umx - 14 * ul, umy)])
    for k in range(6):
        polygon(screen, (0, 0, 0), [(umx + ul, umy - uw), (umx + 16 * ul - 6 * ul * k, umy), (umx - 14 * ul, umy)], 1)

umbrella(150, 500, 7, 50)    
ship(800, 450, 150, 60)
cloud(200, 200, 30, 25)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
