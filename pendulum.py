import color
import renderer
import math
from math import sin, cos

width = 900
height = 900
title = 'Double Pendulum'

first = True

start_pair = [0, -200]
mid_pair   = [0, 0]
end_pair   = [0, 0]
points     = [start_pair, mid_pair, end_pair]
prev_pair  = [0, 0]
prev_points = []
#gravitational constant
g = 2.5

#rod length
r1 = 192
r2 = 192

#masses
m1 = 10
m2 = 10

#start angles
theta1 = math.pi/2
theta2 = math.pi

#angular velocity
vel1 = 0.0
vel2 = 0.0

#angular acceleration
acl1 = 0.0
acl2 = 0.0

#air resistance
resistance = 0.99

def draw():
    renderer.background(color.WHITE)
    renderer.translate(int(width/2), int(height/2))
    calc_angles()
    calc_rods()
    draw_rod()
    draw_mass()
    draw_lines()

def draw_rod():
    for i in range(len(points)-1):
        renderer.line(points[i], points[i+1], color.BLACK)

def draw_mass():
    renderer.circle2(points[1],  m1, color.BLACK)
    renderer.circle2(points[2], m2, color.BLACK)

def draw_lines():
    global first
    if (first == True):
        first = False
        return

    prev_points.append([prev_pair, points[2]])
    for i in range(len(prev_points)):
        renderer.line(prev_points[i][0], prev_points[i][1], color.BLACK)

def calc_angles():
    global vel1, vel2
    global acl1, acl2
    global theta1, theta2

    num1 = (-g*(2*m1+m2)*sin(theta1)
           -m2*g*sin(theta1-(2*theta2))
           -2*sin(theta1-theta2)*m2*((vel2*vel2)*r2
           +(vel1*vel1)*r1*cos(theta1-theta2)))

    num2 = (2*sin(theta1-theta2)*
           ((vel1*vel1)*r1*(m1+m2)
           +g*(m1+m2)*cos(theta1)
           +(vel2*vel2)*r2*m2*cos(theta1-theta2)))

    den = (2*m1+m2-m2*cos(2*theta1-2*theta2))
    den1 = r1*den
    den2 = r2*den

    acl1 = num1/den1
    acl2 = num2/den2
    acl1 *= resistance
    acl2 *= resistance
    vel1 += acl1
    vel2 += acl2
    theta1 += vel1
    theta2 += vel2

def calc_rods():
    global points
    global mid_pair, end_pair
    x1 = start_pair[0] + r1*sin(theta1)
    y1 = start_pair[1] + r1*cos(theta1)
    x2 = x1 + r2*sin(theta2)
    y2 = y1 + r2*cos(theta2)
    
    global prev_pair
    prev_pair = [points[2][0], points[2][1]]
    points[1] = [int(x1), int(y1)]
    points[2] = [int(x2), int(y2)]

if __name__ == '__main__':
    size = (width, height)
    renderer.init(size, title, draw)
