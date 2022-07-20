

#
#   name: colLib
#   program: library for collision detection
#



import pygame
from math import *

pygame.init()


def collideCircle(c1, c2):
    return sqrt((c1[0] - c2[0]) ** 2 +(c1[1] - c2[1]) ** 2) <= c1[2] + c2[2]


def colCircleRect(c, r):
    cr = pygame.Rect(c[0] - c[2], c[1] - c[2], c[2] * 2, c[2] * 2)
    rc = [r.x + r.width / 2, r.y + r.height / 2, r.width/2]
    
    return (cr.colliderect(r)) and (collideCircle(c, rc))
     


