import pygame
import random
import time
from block import Block

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mining Game")


block_rect = pygame.Rect(WIDTH//2 - 50, HEIGHT//2 - 50, 100, 100)
block_broken = False
failCount = 0
inventory = {'gold': 0, 'silver': 0, 'diamond': 0}
hideBlobk = False
cooldownTime = 0
cooldownDuration = 2

mineral_rates = {
    'gold': 40,
    'silver': 30,
    'diamond': 30
}

def dig_block():
    global block_broken, failCount
    if random.random() < 0.5:  
        block_broken = True
        return check_for_minerals()
    else:
        block_broken = False
        return None

def check_for_minerals():
    global failCount
    if failCount == 3:
        mineral = guaranteed_mineral_drop()
        failCount = 0
    elif random.random() < 0.3:
        mineral = random_mineral()
        failCount = 0
    else:
        failCount += 1
        mineral = None
    return mineral

def random_mineral():
    choice = random.choices(['gold', 'silver', 'diamond'], weights=mineral_rates.values())[0]
    inventory[choice] += 1
    return choice

def guaranteed_mineral_drop():
    mineral = random_mineral()
    return mineral

running = True
while running:
    screen.fill("WHITE")
    
    pygame.draw.rect(screen, "WHITE", block_rect)
    
    if hideBlobk:
        if time.time() - cooldownTime >= cooldownDuration:
            hideBlobk = False

    if not hideBlobk:
        pygame.draw.rect(screen, "BROWN", block_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if block_rect.collidepoint(event.pos) and not hideBlobk:
                    mineral = dig_block()
                    if block_broken:
                        print("Block broken!")
                        if mineral:
                            print(f"Found {mineral}!")
                        else:
                            print("No mineral found.")
                        hideBlobk = True
                        cooldownTime = time.time()
                    else:
                        print("Block not broken.")

    pygame.display.flip()

pygame.quit()