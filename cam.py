import pygame as pg
import numpy as np
from time import sleep
from colors import *
from matrices import *
from drawing import *
from controls import *

screen_size_x = 1600
screen_size_y = 900

pg.init()

screen = pg.display.set_mode([screen_size_x, screen_size_y])

initialize_cuboids()
initialize_screen(screen_size_x, screen_size_y)

running = True
while running: 
    running, d = handle_controls()    
    screen.fill(background_color)
    draw_cuboids(screen, d)
    pg.display.flip()

pg.quit()