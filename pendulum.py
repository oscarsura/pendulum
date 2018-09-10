import renderer
import color

width = 600
height = 600
title = 'Double Pendulum'

start_pair = []
mid_pair   = []
end_pair   = []

def draw():
    renderer.background(color.WHITE)
    renderer.translate(int(width/2), int(height/2))
    draw_rod()
    draw_mass()

def draw_rod():


if __name__ == '__main__':
    size = (width, height)
    renderer.init(size, title, draw)
