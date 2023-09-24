#import pygame, init pygame, and create window

import pygame
import math
import random
import time
from math import pi, sin
from random import randint
pygame.init()
size = (1400, 1000)
screen = pygame.display.set_mode(size)
PI = pi
font = pygame.font.SysFont('Calibri', 25, True, False)
BLACK = (000, 000, 000)
WHITE = (255, 255, 255)
RED = (255, 000, 000)
GREEN = (000, 255, 000)
BLUE = (000, 000, 255)

done = False
clock = pygame.time.Clock()
pygame.display.set_caption("sawyers game")
screen.fill(WHITE)
text = font.render("Congratulations Sawyer!", True, BLUE)
screen.blit(text, [200,50])
text_2 = font.render("Congratulations Sawyer!", True, BLUE)
screen.blit(text_2, [50,650])

pygame.draw.rect(screen, BLACK, [100,100,100,200])

pygame.draw.rect(screen, RED, [100,100,200,200])

pygame.draw.rect(screen, GREEN, [100,300,200,200])

pygame.draw.rect(screen, BLUE, [300,300,200,200])

pygame.draw.rect(screen, BLACK, [300,500,200,200])

pygame.draw.rect(screen, RED, [500,500,200,200])

pygame.draw.rect(screen, GREEN, [700,500,200,200])

pygame.draw.rect(screen, BLUE, [900,500,200,200])

pygame.draw.rect(screen, BLACK, [1100,500,200,200])

pygame.draw.rect(screen, RED, [1300,500,200,200])

pygame.display.update()
pygame.display.flip()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
            break





