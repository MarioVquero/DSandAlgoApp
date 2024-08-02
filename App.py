import pygame
import sys
import Buttons



class main():
    pygame.init()
    # resolution of window
    window_size = (800,900)

    # setting window res
    window = pygame.display.set_mode(window_size)

    # giving the window a caption
    pygame.display.set_caption("DSandAlgo")


    # load images if necessary
    # can be used for UI
    searchAlgo_Button_Image = pygame.image.load('').convert_alpha()
    dynamicProg_Button_Image = pygame.image.load('').convert_alpha()
    sortinAlgo_Button_Image = pygame.image.load('').convert_alpha()

    # create new button instances
    searchAlgo_Button = Buttons.button(100,400, searchAlgo_Button_Image ,0.8)
    dynamicProg_Button = Buttons.button(100,400, dynamicProg_Button_Image, 0.8)
    sortinAlgo_Button = Buttons.button(100,400, sortinAlgo_Button_Image, 0.8)

    # Start loop
    running = True
    while running:
        # handles events
        for event in pygame.event.get():
            # ends the loop
            if event.type == pygame.QUIT:
                running = False
        # Fill in the window so it is not blank
        window.fill((128,128,128))

        # "Draws" the button on the window
        # and lets them do what they need to do
        # All buttons will eventually be able to go
        # to their respecitve section and show
        #  algorithms or datastructures that are
        # associated with that section
        if searchAlgo_Button.draw(window):
            from Scripts.SearchAlgorithms.BinarySearchScripts.BinarySearchDisplay import binarySearch
            binarySearch()
        
        if dynamicProg_Button.draw(window):
            print('Dynamic programming button')
        
        if sortinAlgo_Button.draw(window):
            print('Sorting Algorithm button')
        # if b_Search.draw(window):

        #updates the entire contents of the display
        pygame.display.flip()

pygame.quit