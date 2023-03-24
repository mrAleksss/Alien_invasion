import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion():
    # Загальний клас для керування об'єктами та ресурсами в грі
    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Вторгнення прибульців")

        self.ship = Ship(self)


    def run_game(self):
        # start main loop for the game
        while True:
            # whatch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Зробити видимим останній намальваний екран
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()