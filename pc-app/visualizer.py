import pygame
import math

PIXELS_PER_CM = 550/400

def init_display():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    return screen

def draw_frame(screen, reading):
    screen.fill((0, 0, 0))

    draw_grid(screen)

    if reading is not None:
        pygame.draw.circle(screen, (0, 255, 0), polar_to_pixel(reading[0], reading[1], screen.get_width()//2, screen.get_height()-10), 3)

    pygame.display.flip()

def draw_grid(screen):
    center_x = screen.get_width()//2
    center_y = screen.get_height() - 10

    for distance_cm in range(50, 401, 50):
        r = distance_cm * PIXELS_PER_CM
        rectangle = pygame.Rect(center_x-r, center_y-r, 2*r, 2*r)
        pygame.draw.arc(screen, (105, 105, 105), rectangle, 0, math.pi, 2)



def handle_events():
    running = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    return running

def polar_to_pixel(angle, distance, center_x, center_y):
    angle_rad = math.radians(angle)
    x_offset = distance * math.cos(angle_rad) * PIXELS_PER_CM
    y_offset = -1 * distance * math.sin(angle_rad) * PIXELS_PER_CM

    x = center_x + x_offset
    y = center_y + y_offset

    return x, y





