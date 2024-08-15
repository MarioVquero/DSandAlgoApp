# this script is used to display everything not actually
# perform the algorithm

import pygame
import sys
from BinarySearch import binary_search

class binarySearch():

    pygame.init()
    window_size = (800,900)

    window = pygame.display.set_mode(window_size)

    pygame.display.set_caption("Binary Search")

    running = True

    

    # when first opening the window ask the user
    # to set a range and their target number
    # after the window will update and run 
    # and show circles which turn red if the number
    # it chose is incorrect and stay red
    # if the option is incorrect and is larger than target
    # the numbers larger than it will be turned red
    # and vice versa
    # else if its "checking" it will turn orange
    # and green if its the correct number

    


    while running:

        window.fill((120,120,120))
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

print('I should quit now')
pygame.quit
sys.exit()