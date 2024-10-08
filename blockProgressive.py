import pygame
import random

dropRate = {
    'copper': 50,
    'silver': 35,
    'gold': 10,
    'diamond': 5
} 
class BlockProgressive:  
    
    def __init__(self,screen,success_rate,increment):
        self.screen = screen
        self.blockRect = pygame.Rect(screen.get_width()//2 - 50, screen.get_height()//2 - 50, 100, 100)
        self.blockBroken = False
        self.failCount = 0
        
        self.base_success=success_rate
        self.current_success=self.base_success
        self.increment=increment
    
        self.frame_size = 500
        self.block_sprite = pygame.image.load("./assets/StoneBlock.png")
        self.block_frame = self.block_sprite.subsurface(pygame.Rect( 0 * self.frame_size, 0 * self.frame_size,
                                                                    self.frame_size,
                                                                    self.frame_size))
    
    
    def draw(self):
        pygame.draw.rect(self.screen, "BROWN", self.blockRect)
        self.screen.blit(self.block_frame,  pygame.Vector2(self.blockRect.x,self.blockRect.y) - pygame.Vector2(250, 250))

          
    def dig_block(self):

        p=random.uniform(0,100)
        if p< self.current_success:
            self.reset_prob()
            return self.RandomOre()
        else:
            self.current_success += self.increment
            self.failCount += 1
            return "Nothing"
                 
    def RandomOre(self):
        if random.random() < 0.3 or self.failCount >= 3:
            ore = random.choices(['copper', 'silver', 'gold', 'diamond'], weights=dropRate.values())[0]
            self.failCount = 0
            return ore
        else:
            self.failCount += 1
            return "No Ore"

    def reset_prob(self):
        self.current_success=self.base_success

    
