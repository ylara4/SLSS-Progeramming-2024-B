# intro to pygame
# - boilerplate
# - sprite class

import pygame
from pygame.sprite import _Group

# child class of Sprite
# -represent the dvd logo
class DVdlogo(pygame.sprite.Sprite):
    """represents the DVD logo"""
    def __init__(self): 
        self.image = pygame.image.load("./Images/dvd-logo.png")

        self.rect = self.image.get_rect() # first position of the image in top right

def start():
    """Environment Setup and Game Loop"""

    pygame.init()

    # --CONSTANTS--
    # COLOURS
    WHITE   = (255, 255, 255)
    BLACK   = (  0,   0,   0)
    EMERALD = ( 21, 219, 147)
    RED     = (255,   0,   0)
    GREEN   = (  0, 255,   0)
    BLUE    = (  0,   0, 255)
    GRAY    = (128, 128, 128)

    WIDTH   = 1280    # Pixels
    HEIGHT  =  720
    SCREEN_SIZE = (WIDTH, HEIGHT)

    # --VARIABLES--
    screen = pygame.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pygame.time.Clock()

    pygame.display.set_caption("<WINDOW TITLE HERE>")

    # --MAIN LOOP--
    while not done:
        # --- Event Listener
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

		# --- Update the world state

        # --- Draw items
        screen.fill(BLACK)
      
        # Update the screen with anything new
        pygame.display.flip()

        # --- Tick the Clock
        clock.tick(60)    # 60 fps


def main():
    start()

if __name__ == "__main__":
    main()