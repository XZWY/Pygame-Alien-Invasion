import pygame
import sys

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((200, 200))
    
    while True:
        screen.fill((100, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print(event.key)
                screen.fill((0, 100, 0))
        pygame.display.flip()

run_game()
