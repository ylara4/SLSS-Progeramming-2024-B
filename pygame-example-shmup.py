import pygame as pg

# --CONSTANTS--
# COLOURS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
EMERALD = (21, 219, 147)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

WIDTH = 720  # Pixels
HEIGHT = 1000
SCREEN_SIZE = (WIDTH, HEIGHT)

#todo: player class
#-player movement
#-players positions limited to the bottom part of the screen
class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image - pg.image.load("./Images/galaga_ship.png")
        self.image = pg.transform.scale()
        self.image,
        (self.image.get_widt()) // 2, self.image.get_height(); // 2)))
        self.rect = self.image.get_rect()

        def update(self):
            self.rect.center = pg.mouse.get_pos()
            if self.rect.top < HEIGHT - 200:
                self.rect.top = HEIGHT - 200

#todo: bullet class
#-image
#-spawn of the player
#-vertical movement
class Bullet(pg.sprite.Sprite):
    def __init__(self):
     super().__init__()
    self.image = pg.Surface((10,25))
    self.image.fill(GREEN)
    self.rect = self.image.get_rect()
    self.rect.centerx = Player [0]
    self.rect.bottom = Player [1]
    all_sprites.add(Bullet(Player))

#todo: enemy class
#-side to side movement
#-keep it inside the screen


def start():
    """Environment Setup and Game Loop"""

    pg.init()

    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    # All sprites go in this sprite Group
    all_sprites = pg.sprite.Group()

    pg.display.set_caption("<SHMUP>")

    # --Main Loop--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        # --- Update the world state

        # --- Draw items
        screen.fill(BLACK)

        # Update the screen with anything new
        pg.display.flip()
        all_sprites = pg.sprite.Group()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps


def main():
    start()


if __name__ == "__main__":
    main()