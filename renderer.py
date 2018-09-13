import os, sys

x_offset = 0
y_offset = 0

with open(os.devnull, 'w') as out:
    prev = sys.stdout
    sys.stdout = out
    import pygame
    from pygame import gfxdraw
    sys.stdout = prev

screen = None

def init(size, title, func):
    pygame.init()
    global screen
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(title)
    loop(func)

def loop(func):
    done = False
    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        func()
        pygame.display.flip()
        clock.tick(240)

def background(color):
    screen.fill(color)

def shift(pair):
    newpair = [pair[0] + x_offset, pair[1] + y_offset]
    return newpair

def translate(x, y):
    global x_offset, y_offset
    x_offset = x
    y_offset = y

def ellipse(color, rect, weight = 0):
    rect[0] += x_offset
    rect[1] += y_offset
    pygame.draw.ellipse(screen, color, rect, weight)

def circle(x, y, radius, color, weight = 0):
    x += x_offset
    y += y_offset
    pygame.gfxdraw.aacircle(screen, x, y, radius, color)
    pygame.gfxdraw.filled_circle(screen, x, y, radius, color)

def circle2(pair, radius, color, weight = 0):
    circle(pair[0], pair[1], radius, color, weight)

def line(start_pair, end_pair, color):
    start_pair = shift(start_pair)
    end_pair = shift(end_pair)
    pygame.draw.aaline(screen, color, start_pair, end_pair, 1)
