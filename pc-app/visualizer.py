import pygame
import math

def init_display():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    return screen

def draw_frame(screen, reading):
    screen.fill((0, 0, 0))

    if reading is not None:
        pygame.draw.circle(screen, (0, 255, 0), polar_to_pixel(reading[0], reading[1], screen.get_width()//2, screen.get_height() - 30), 3)

    pygame.display.flip()


def handle_events():
    running = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    return running

def polar_to_pixel(angle, distance, center_x, center_y):
    angle_rad = math.radians(angle)
    x_offset = distance * math.cos(angle_rad)
    y_offset = -1 * distance * math.sin(angle_rad)

    x = center_x + x_offset
    y = center_y + y_offset

    return x, y





