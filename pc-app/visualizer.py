import pygame
import math
import time

MAX_RANGE = 400
MAX_AGE = 2
PIXELS_PER_CM = 550/MAX_RANGE
BASE_COLOR = (0, 255, 0)

def get_center(screen):
    center_x = screen.get_width() // 2
    center_y = screen.get_height() - 10
    return center_x, center_y


def init_display():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    return screen


def draw_frame(screen, reading, trail, font):
    screen.fill((0, 0, 0))
    center_x, center_y = get_center(screen)

    draw_grid(screen, center_x, center_y, font)

    if reading is not None:
        pygame.draw.circle(screen, BASE_COLOR, polar_to_pixel(reading[0], reading[1], center_x, center_y), 3)
        pygame.draw.line(screen, (0, 120, 120), (center_x, center_y), polar_to_pixel(reading[0], MAX_RANGE, center_x, center_y), 1)
    draw_trail(screen, trail, center_x, center_y)
    pygame.display.flip()


def draw_grid(screen, center_x, center_y, font):
    for distance_cm in range(50, 401, 50):
        r = distance_cm * PIXELS_PER_CM
        rectangle = pygame.Rect(center_x-r, center_y-r, 2*r, 2*r)
        pygame.draw.arc(screen, (105, 105, 105), rectangle, 0, math.pi, 2)

        label_pos = polar_to_pixel(90, distance_cm, center_x-17, center_y)
        label_text = str(distance_cm) + "cm"
        text_surface = font.render(label_text, True, (200, 200, 200))
        screen.blit(text_surface, label_pos)


def draw_trail(screen, trail, center_x, center_y):
    for entry in trail:
        angle, distance, timestamp = entry
        age = time.time() - timestamp
        if (MAX_AGE >= age):
            brightness = (MAX_AGE-age)/MAX_AGE
        else:
            brightness = 0
        r = int(BASE_COLOR[0] * brightness)
        g = int(BASE_COLOR[1] * brightness)
        b = int(BASE_COLOR[2] * brightness)
        color = (r, g, b)
        pygame.draw.circle(screen, color, polar_to_pixel(angle, distance, center_x, center_y), 2)



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





