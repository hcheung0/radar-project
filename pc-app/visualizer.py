import pygame

def init_display():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    return screen

def draw_frame(screen, reading):
    screen.fill((0, 0, 0))
    pygame.display.flip()  

def handle_events():
    running = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    return running



