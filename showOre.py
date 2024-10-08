import pygame

class ShowOres:
    def __init__(self,screen):
        self.frame_size = 500
        self.block_sprite = pygame.image.load("./assets/StoneBlock.png")
        self.block_frame = self.block_sprite.subsurface(pygame.Rect( 0 * self.frame_size, 0 * self.frame_size,
                                                                    self.frame_size,
                                                                    self.frame_size))