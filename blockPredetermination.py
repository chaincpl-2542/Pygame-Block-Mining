import pygame
import random

dropRate = {
    'copper': 50,
    'silver': 35,
    'gold': 10,
    'diamond': 5
} 
class BlockPredetermination:  
    
    def __init__(self,screen ,max_attempts):
        self.screen = screen
        self.blockRect = pygame.Rect(screen.get_width()//2 - 50, screen.get_height()//2 - 50, 100, 100)
        self.blockBroken = False
        self.failCount = 0
        
        self.attempts=0
        self.max_attempts=max_attempts
        
        self.frame_size = 500
        self.block_sprite = pygame.image.load("./assets/StoneBlock.png")
        self.block_frame = self.block_sprite.subsurface(pygame.Rect( 0 * self.frame_size, 0 * self.frame_size,
                                                                    self.frame_size,
                                                                    self.frame_size))         
    
    def draw(self):
        pygame.draw.rect(self.screen, "BROWN", self.blockRect)
        self.screen.blit(self.block_frame,  pygame.Vector2(self.blockRect.x,self.blockRect.y) - pygame.Vector2(250, 250))

    
    def dig_block(self):
        if(self.failCount >= 3):
            return self.RandomOre()
        elif random.random() < 0.5:
            self.blockBroken = True
            return self.RandomOre()
        else:
            self.blockBroken = False
            self.failCount += 1
            return None
                   
    def RandomOre(self):
        if random.random() < 0.3 or self.failCount >= 3:
            ore = random.choices(['copper', 'silver', 'gold', 'diamond'], weights=dropRate.values())[0]
            self.failCount = 0
            return ore
        else:
            self.failCount += 1
            return "No Ore"

    def attempt(self):
        self.attempts=+ 1
        if self.attempts >= self.max_attempts:
            self.attempts=0
            return self.RandomOre()
        return "Nothing"