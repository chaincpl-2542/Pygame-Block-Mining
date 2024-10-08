import pygame
import random
import time
from blockMarblebag import BlockMarblebag
from blockFixRateRandom import BlockFixRate
from blockPredetermination import BlockPredetermination
from blockProgressive import BlockProgressive


pygame.init()

WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
block_rect = pygame.Rect(WIDTH//2 - 50, HEIGHT//2 - 50, 100, 100)
block = BlockMarblebag(screen)
font = pygame.font.Font(None, 36)

dropdown_open = False
dropdown_options = ["marblebag", "progressive", "fixed_random", "predetermination"]
selected_option = "marblebag"
dropdown_rect = pygame.Rect(50, 50, 200, 40)
option_rects = [pygame.Rect(50, 90 + i * 40, 200, 40) for i in range(len(dropdown_options))]
check_selected_option = None
isBlockBroken = False

cooldown_start_time = 0
cooldown_duration = 2 

def draw_text(text, pos, color="BLACK"):
    label = font.render(text, True, color)
    screen.blit(label, pos)
    
def draw_dropdown():
    pygame.draw.rect(screen, "GRAY" if dropdown_open else "WHITE", dropdown_rect)
    draw_text(selected_option, (dropdown_rect.x + 10, dropdown_rect.y + 5))
    
    if dropdown_open:
        for i, option in enumerate(dropdown_options):
            pygame.draw.rect(screen, "WHITE", option_rects[i])
            draw_text(option, (option_rects[i].x + 10, option_rects[i].y + 5))

running = True
while running:
    screen.fill("WHITE")
    
    #pygame.draw.rect(screen, "WHITE", block_rect)
    draw_dropdown()
    
    if isBlockBroken:
        if time.time() - cooldown_start_time >= cooldown_duration: 
            isBlockBroken = False
    
    if isBlockBroken == False:
        block.draw()
        if selected_option == "marblebag" and check_selected_option != selected_option:
            check_selected_option = "marblebag"
            seed = None
            if seed is not None:
                random.seed(seed)
            block = BlockMarblebag(screen, random.seed(seed))
            
        elif selected_option == "progressive" and check_selected_option != selected_option:
            check_selected_option = "progressive"
            block = BlockProgressive(screen,50,10)
        elif selected_option == "fixed_random" and check_selected_option != selected_option:
            check_selected_option = "fixed_random"
            block = BlockFixRate(screen,50,3)
        elif selected_option == "predetermination" and check_selected_option != selected_option:
            check_selected_option = "predetermination"
            block = BlockPredetermination(screen,50)
    else:
        check_selected_option = None

    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if dropdown_rect.collidepoint(event.pos):
                dropdown_open = not dropdown_open 
            elif dropdown_open:
                for i, rect in enumerate(option_rects):
                    if rect.collidepoint(event.pos):
                        selected_option = dropdown_options[i]
                        dropdown_open = False
                        break
            elif event.button == 1:
                    if isBlockBroken == False:
                        getOre = block.dig_block()
                        if(getOre != None and getOre != "Nothing"):
                            print(getOre)
                            cooldown_start_time = time.time()
                            isBlockBroken = True
    
    pygame.display.flip()

pygame.quit()