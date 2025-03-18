import pygame

#pygame setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

while running:
    if pygame.event.get(pygame.QUIT):
        running = False
        raise SystemExit

    #Logical update here

    screen.fill('black')

    #Render graphic here

    pygame.display.flip()   #Flip display
    clock.tick(60)          #Limit FPS: 60
pygame.quit()
