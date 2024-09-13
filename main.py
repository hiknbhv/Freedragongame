import pygame

pygame.init()

Window_Width = 1000
Window_Height = 400
display_surface = pygame.display.set_mode((Window_Width, Window_Height))
pygame.display.set_caption("Feed The Dragon")



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False