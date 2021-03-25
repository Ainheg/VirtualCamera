import pygame as pg
from drawing import *

rot_yaw_cw = False
rot_yaw_ccw = False
rot_roll_cw = False
rot_roll_ccw = False
rot_pitch_cw = False
rot_pitch_ccw = False
translate_x_dec = False
translate_y_dec = False
translate_z_dec = False
translate_x_inc = False
translate_y_inc = False
translate_z_inc = False
zoom_plus = False
zoom_minus = False
d = 100

def handle_controls():
    dx = 0
    dy = 0
    dz = 0
    running = True

    global rot_yaw_cw 
    global rot_yaw_ccw 
    global rot_roll_cw 
    global rot_roll_ccw 
    global rot_pitch_cw 
    global rot_pitch_ccw 
    global translate_x_dec 
    global translate_y_dec 
    global translate_z_dec 
    global translate_x_inc 
    global translate_y_inc 
    global translate_z_inc 
    global zoom_plus
    global zoom_minus
    global d

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_j:
                rot_yaw_ccw = True
            if event.key == pg.K_l:
                rot_yaw_cw = True
            if event.key == pg.K_u:
                rot_roll_ccw = True
            if event.key == pg.K_o:
                rot_roll_cw = True
            if event.key == pg.K_i:
                rot_pitch_ccw = True
            if event.key == pg.K_k:
                rot_pitch_cw = True
            if event.key == pg.K_d:
                translate_x_inc = True
            if event.key == pg.K_a:
                translate_x_dec = True
            if event.key == pg.K_w:
                translate_z_inc = True
            if event.key == pg.K_s:
                translate_z_dec = True
            if event.key == pg.K_r:
                translate_y_inc = True
            if event.key == pg.K_f:
                translate_y_dec = True   
            if event.key == pg.K_KP_PLUS:
                zoom_plus = True
            if event.key == pg.K_KP_MINUS:
                zoom_minus = True 
        if event.type == pg.KEYUP:
            if event.key == pg.K_j:
                rot_yaw_ccw = False
            if event.key == pg.K_l:
                rot_yaw_cw = False
            if event.key == pg.K_u:
                rot_roll_ccw = False
            if event.key == pg.K_o:
                rot_roll_cw = False
            if event.key == pg.K_i:
                rot_pitch_ccw = False
            if event.key == pg.K_k:
                rot_pitch_cw = False
            if event.key == pg.K_d:
                translate_x_inc = False
            if event.key == pg.K_a:
                translate_x_dec = False
            if event.key == pg.K_w:
                translate_z_inc = False
            if event.key == pg.K_s:
                translate_z_dec = False
            if event.key == pg.K_r:
                translate_y_inc = False
            if event.key == pg.K_f:
                translate_y_dec = False
            if event.key == pg.K_KP_PLUS:
                zoom_plus = False
            if event.key == pg.K_KP_MINUS:
                zoom_minus = False 
    if (zoom_plus and not zoom_minus):
        d = d * 1.01
    if (zoom_minus and not zoom_plus):
        d = d * 0.99
    if (translate_x_dec and not translate_x_inc):
        dx = 0.2
    if (translate_x_inc and not translate_x_dec):
        dx = -0.2
    if (translate_y_dec and not translate_y_inc):
        dy = 0.2
    if (translate_y_inc and not translate_y_dec):
        dy = -0.2        
    if (translate_z_dec and not translate_z_inc):
        dz = 0.2
    if (translate_z_inc and not translate_z_dec):
        dz = -0.2   
    translate(dx, dy, dz)
    if (rot_yaw_ccw and not rot_yaw_cw):
        yaw(0.1)
    if (rot_yaw_cw and not rot_yaw_ccw):
        yaw(-0.1)
    if (rot_roll_ccw and not rot_roll_cw):
        roll(-0.1)
    if (rot_roll_cw and not rot_roll_ccw):
        roll(0.1)
    if (rot_pitch_ccw and not rot_pitch_cw):
        pitch(0.1)
    if (rot_pitch_cw and not rot_pitch_ccw):
        pitch(-0.1)
    return running, d