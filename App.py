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

    # create new button instances
    # b_Search = Buttons.button(100,400,image,0.8)

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

        # "Draws"  the button on the window
        # and lets them do what they need to

        # if b_Search.draw(window):

        #updates the entire contents of the display
        pygame.display.flip()

pygame.quit