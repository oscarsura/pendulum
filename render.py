import pygame

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

def loop():
    done = False

    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill((0xFF, 0xFF, 0xFF))
        pygame.display.flip()
        clock.tick(60)

start()
loop()
