import pygame

class Block:
    
    def __init__(self,screen):
        self.screen = screen
        self.blockRect = pygame.Rect(screen.get_width()//2 - 50, screen.get_height()//2 - 50, 100, 100)
    
    def draw(self):
        pygame.draw.rect(self.screen, "BROWN", self.blockRect)
    
    def dig_block():
        pass
        
    