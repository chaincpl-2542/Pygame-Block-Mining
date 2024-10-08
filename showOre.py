import pygame

class ShowOres:
    def __init__(self,screen,font):
        self.font = font
        self.screen = screen
        self.blockRect = pygame.Rect(screen.get_width()//2 - 50, screen.get_height()//2 - 50, 100, 100)
        self.frame_size = 500
        self.ore_sprite = pygame.image.load("./assets/Copper.png")
        self.block_frame = self.ore_sprite.subsurface(pygame.Rect( 0 * self.frame_size, 0 * self.frame_size,
                                                                    self.frame_size,
                                                                    self.frame_size))
        
    def draw(self,ore):
        if(ore == "copper"):
            self.ore_sprite = pygame.image.load("./assets/Copper.png")
            label =  self.font.render("Copper", True, "Black")
            self.screen.blit(label, pygame.Vector2(self.blockRect.x,self.blockRect.y) + pygame.Vector2(0, 200))
        elif(ore == "silver"):
            self.ore_sprite = pygame.image.load("./assets/Silver.png")
            label =  self.font.render("Silver", True, "Black")
            self.screen.blit(label, pygame.Vector2(self.blockRect.x,self.blockRect.y) + pygame.Vector2(0, 200))
        elif(ore == "gold"):
            self.ore_sprite = pygame.image.load("./assets/gold.png")
            label =  self.font.render("Gold", True, "Black")
            self.screen.blit(label, pygame.Vector2(self.blockRect.x,self.blockRect.y) + pygame.Vector2(0, 200))
        elif(ore == "diamond"):
            self.ore_sprite = pygame.image.load("./assets/Diamond.png")
            label =  self.font.render("Diamond", True, "Black")
            self.screen.blit(label, pygame.Vector2(self.blockRect.x,self.blockRect.y) + pygame.Vector2(0, 200))
        else:
            self.ore_sprite = pygame.image.load("./assets/StoneDust.png")
            label =  self.font.render("Nothing", True, "Black")
            self.screen.blit(label, pygame.Vector2(self.blockRect.x,self.blockRect.y) + pygame.Vector2(0, 200))
            
        self.screen.blit(self.ore_sprite,  pygame.Vector2(self.blockRect.x,self.blockRect.y) - pygame.Vector2(250, 250))
