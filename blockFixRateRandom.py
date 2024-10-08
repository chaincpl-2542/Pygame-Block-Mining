import pygame
import random

dropRate = {
    'copper': 50,
    'silver': 35,
    'gold': 10,
    'diamond': 5
} 
class BlockFixRate:  
    
    def __init__(self,screen,prob, fixed_rate):
        self.screen = screen
        self.blockRect = pygame.Rect(screen.get_width()//2 - 50, screen.get_height()//2 - 50, 100, 100)
        self.blockBroken = False
        
        self.attempt_count=0
        self.fixed_success=fixed_rate
        self.base_prob=prob
        
        self.frame_size = 500
        self.block_sprite = pygame.image.load("./assets/StoneBlock.png")
        self.block_frame = self.block_sprite.subsurface(pygame.Rect( 0 * self.frame_size, 0 * self.frame_size,
                                                                    self.frame_size,
                                                                    self.frame_size))
    
        
    
    def draw(self):
        pygame.draw.rect(self.screen, "BROWN", self.blockRect)       
        self.screen.blit(self.block_frame,  pygame.Vector2(self.blockRect.x,self.blockRect.y) - pygame.Vector2(250, 250))

    def dig_block(self):
        if self.attempt_count >= self.fixed_success:
            self.attempt_count=0
            return self.RandomOre()
        roll = random.uniform(0,100)
        if roll<self.base_prob:
            return self.RandomOre()
        else:
            self.attempt_count += 1
            return "Nothing"

    def RandomOre(self):
        if random.random() < 0.3 or self.attempt_count >= self.fixed_success:
            ore = random.choices(['copper', 'silver', 'gold', 'diamond'], weights=dropRate.values())[0]
            self.attempt_count = 0
            return ore
        else:
            self.attempt_count += 1
            return "No Ore"
    
    
        
        