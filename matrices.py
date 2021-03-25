import numpy as np
from math import sin, cos, radians

def projection_matrix(d):
    return np.array([[1, 0, 0, 0],
                      [0, 1, 0, 0],
                      [0, 0, 1, 0],
                      [0, 0, 1/d, 0]])

def rotation_matrix_yaw(a):
    a = radians(a)
    return np.array([[cos(a), 0, sin(a), 0],
                     [0, 1, 0, 0],
                     [-sin(a), 0, cos(a), 0],
                     [0, 0, 0, 1]])

def rotation_matrix_roll(a):
    a = radians(a)
    return np.array([[cos(a), -sin(a), 0, 0],
                     [sin(a), cos(a), 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])

def rotation_matrix_pitch(a):
    a = radians(a)
    return np.array([[1, 0, 0, 0],
                     [0, cos(a), -sin(a), 0],
                     [0, sin(a), cos(a), 0],
                     [0, 0, 0, 1]])

def translation_matrix(dx, dy, dz):
    return np.array([[1, 0, 0, dx],
                     [0, 1, 0, dy],
                     [0, 0, 1, dz],
                     [0, 0, 0, 1]])



