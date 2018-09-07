import time
import pygame
import random

width = 600
height = 600
screen = None
title = 'Double Pendulum'

def start():
    pygame.init()
    size = (width, height)
    global screen
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(title)
    loop()

def draw():
    pygame.draw.ellipse(screen, (255, 255, 255), [random.randint(0, width), random.randint(0, height), 4,4], 2)

def loop():
    done = False

    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        draw()
        pygame.display.flip()
        clock.tick(60)

start()
