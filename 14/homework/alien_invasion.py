
import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvision:
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height
                ))

        # self.screen = pygame.display.set_mode((1200, 700))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        # Назначение цвета фона.
        # self.bg_color = (230, 230,230)

    def run_game(self):
        """Запуск основного циклв игры."""
        while True:
            # Отслеживание событий клавиатуры и мыши.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # При каждом проходе цикла перерисовывается экран.
            self.screen.fill(self.settings.bg_color)
            # self.screen.fill(self.bg_color)

            self.ship.blitme()

            # Отображение последнего прорисованного зкрана.
            pygame.display.flip()

if __name__ in '__main__':
    # Создание экземпляра и запуск игры.
    ai = AlienInvision()
    ai.run_game()