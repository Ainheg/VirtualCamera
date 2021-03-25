import pygame as pg
import numpy as np
from math import sqrt
from matrices import *
from colors import *

cuboids = []
size_x = None
size_y = None


def create_cuboid(x, y, z, width, height):
    points = []
    points.append((x, y, z, 1))
    points.append((x + width, y, z, 1))
    points.append((x, y + height, z, 1))
    points.append((x, y, z + width, 1))
    points.append((x + width, y + height, z + width, 1))
    points.append((x + width, y + height, z, 1))
    points.append((x, y + height, z + width, 1))
    points.append((x + width, y, z + width, 1))
    return points

def initialize_screen(x, y):
    global size_x
    size_x = x
    global size_y
    size_y = y

def initialize_cuboids():
    global cuboids
    cuboids = []
    cuboids.append((create_cuboid(10, -40, 20, 40, 80), white))
    cuboids.append((create_cuboid(-50, -40, 20, 40, 60), white))
    cuboids.append((create_cuboid(10, -40, 80, 40, 120), white))
    cuboids.append((create_cuboid(-50, -40, 80, 40, 100), white))
    for cuboid in cuboids:
        print(cuboid)
        print("\n")
    #for i in range(4):
    #    cuboids.append(create_cuboid(60*(i+1), 60*(i+1), 60*(i+1), 40, 80))

def get_current_points():
    return cuboids

def translate_for_display(coords):
    return (size_x/2 + coords[0], size_y/2 - coords[1])

def yaw(a):
    for cuboid in cuboids:
        for i in range(len(cuboid[0])):
            vertex = cuboid[0][i]
            cuboid[0][i] = tuple(np.matmul(rotation_matrix_yaw(a), vertex))

def roll(a):
    for cuboid in cuboids:
        for i in range(len(cuboid[0])):
            vertex = cuboid[0][i]
            cuboid[0][i] = tuple(np.matmul(rotation_matrix_roll(a), vertex))

def pitch(a):
    for cuboid in cuboids:
        for i in range(len(cuboid[0])):
            vertex = cuboid[0][i]
            cuboid[0][i] = tuple(np.matmul(rotation_matrix_pitch(a), vertex))

def translate(dx, dy, dz):
    for cuboid in cuboids:
        for i in range(len(cuboid[0])):
            vertex = cuboid[0][i]
            cuboid[0][i] = tuple(np.matmul(translation_matrix(dx, dy, dz), vertex))


def projection_normalization(vtx, d):
    return [vtx[0]/vtx[3], vtx[1]/vtx[3], vtx[2]/vtx[3], 1]

def draw_lines(screen, cuboid, color):
    if (cuboid[0][2] > 0 and cuboid[1][2] > 0):
        pg.draw.aaline(screen, color, translate_for_display(cuboid[0]), translate_for_display(cuboid[1]))
    if (cuboid[0][2] > 0 and cuboid[2][2] > 0):
        pg.draw.aaline(screen, color, translate_for_display(cuboid[0]), translate_for_display(cuboid[2]))
    if (cuboid[0][2] > 0 and cuboid[3][2] > 0):
        pg.draw.aaline(screen, color, translate_for_display(cuboid[0]), translate_for_display(cuboid[3]))
    if (cuboid[4][2] > 0 and cuboid[5][2] > 0):
        pg.draw.aaline(screen, color, translate_for_display(cuboid[4]), translate_for_display(cuboid[5]))
    if (cuboid[4][2] > 0 and cuboid[6][2] > 0):
        pg.draw.aaline(screen, color, translate_for_display(cuboid[4]), translate_for_display(cuboid[6]))
    if (cuboid[4][2] > 0 and cuboid[7][2] > 0):
        pg.draw.aaline(screen, color, translate_for_display(cuboid[4]), translate_for_display(cuboid[7]))
    if (cuboid[2][2] > 0 and cuboid[5][2] > 0):
        pg.draw.aaline(screen, color, translate_for_display(cuboid[2]), translate_for_display(cuboid[5]))
    if (cuboid[2][2] > 0 and cuboid[6][2] > 0):
        pg.draw.aaline(screen, color, translate_for_display(cuboid[2]), translate_for_display(cuboid[6]))
    if (cuboid[7][2] > 0 and cuboid[1][2] > 0):
        pg.draw.aaline(screen, color, translate_for_display(cuboid[7]), translate_for_display(cuboid[1]))
    if (cuboid[7][2] > 0 and cuboid[3][2] > 0):
        pg.draw.aaline(screen, color, translate_for_display(cuboid[7]), translate_for_display(cuboid[3]))
    if (cuboid[3][2] > 0 and cuboid[6][2] > 0):
        pg.draw.aaline(screen, color, translate_for_display(cuboid[3]), translate_for_display(cuboid[6]))
    if (cuboid[1][2] > 0 and cuboid[5][2] > 0):
        pg.draw.aaline(screen, color, translate_for_display(cuboid[1]), translate_for_display(cuboid[5]))

def draw_cuboids(screen, d):
    for cuboid in cuboids:
        cuboid_projection = []
        for vertex in cuboid[0]:
            visible = False
            if (vertex[2] > 0):
                visible = True
            vertex_p = np.matmul(projection_matrix(d), vertex)
            vertex_p = projection_normalization(vertex_p, d)
            if (visible):
                vertex_p[2] = 1
            else:
                vertex_p[2] = 0
            cuboid_projection.append(tuple(vertex_p[0:3]))
        draw_lines(screen, cuboid_projection, cuboid[1])
        
    

