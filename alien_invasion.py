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
            self._check_events()
            self._update_screen()
            self.clock.tick(60)
            self.ship.update()


    def _check_events(self):
            # whatch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                     if event.key == pygame.K_RIGHT:
                          self.ship.moving_right = True
                elif event.type == pygame.KEYUP:
                     if event.key == pygame.K_RIGHT:
                          self.ship.moving_right = False
                          


    def _update_screen(self):
            """Update images on the screen, and fleep to the new screen"""
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Зробити видимим останній намальваний екран
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()