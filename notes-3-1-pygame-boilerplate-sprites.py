# intro to pygame
# - boilerplate
# - sprite class

import pygame

# child class of Sprite
# -represent the dvd logo
class Dvdlogo(pygame.sprite.Sprite):
    """represents the DVD logo"""
    def __init__(self): 
        super().__init__()
        self.image = pygame.image.load("./Images/dvd.png")

        self.rect = self.image.get_rect()
        
         # first position of the image in top right
        
        self.vel_x = 3
        self.vel_y = 0

        def update(self): 
            self.rect.x += self.vel_x
            self.rect.y += self.vel_y

            if self.rect.right >= 1280:
                self.vel_x *= -self.vel_x
            print(self.rect.x, self.rect.y)

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

    dvdlogo = Dvdlogo()
    dvdlogo.rect.centerx = WIDTH // 640
    dvdlogo.rect.centery = HEIGHT // 360

    all_sprites = pygame.sprite.Group()
    all_sprites.add(dvdlogo)

    pygame.display.set_caption("<DVD SCREEN SAVER>")

    # --MAIN LOOP--
    while not done:
        # --- Event Listener
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

		# --- Update the world state
            dvdlogo.rect.x = dvdlogo.rect.x + dvdlogo.vel_x
            dvdlogo.rect.y += dvdlogo.vel_y 

        

        # --- Draw items
        screen.fill(BLACK)

        all_sprites.draw(screen)

        
      
        # Update the screen with anything new
        pygame.display.flip()

        # --- Tick the Clock
        clock.tick(60)    # 60 fps


def main():
    start()

if __name__ == "__main__":
    main()