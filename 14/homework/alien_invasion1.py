
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
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        """Запуск основного циклoв игры."""
        while True:
            # Отслеживание событий клавиатуры и мыши.
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Обрабатывает нажатие клавиш и события мыши"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # нажатие клавиш
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # переместить корабль вправо
                    self.ship.rect.x += 1
        
    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""
        # При каждом проходе цикла перерисовывается экран.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Отображение последнего прорисованного зкрана.
        pygame.display.flip()

if __name__ in '__main__':
    # Создание экземпляра и запуск игры.
    ai = AlienInvision()
    ai.run_game()