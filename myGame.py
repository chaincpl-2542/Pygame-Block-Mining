import pygame
import random
from block import Block


pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
block_rect = pygame.Rect(WIDTH//2 - 50, HEIGHT//2 - 50, 100, 100)
block = Block(screen)

running = True
while running:
    screen.fill("WHITE")
    
    pygame.draw.rect(screen, "WHITE", block_rect)
    block.draw()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("Click")
    
    pygame.display.flip()

pygame.quit()