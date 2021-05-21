
import sys
import pygame

class AlienInvision:
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()
        # Размер экрана
        self.screen = pygame.display.set_mode((1200, 700))
        pygame.display.set_caption("Raketa")
        # Назначение цвета фона.
        self.bg_color = (0, 0, 230)

        self.image = pygame.image.load('homework/raketa.bmp')
        self.rect = self.image.get_rect()
        self.screen.blit(self.image, self.rect)

                
    def run_game(self):
        """Запуск основного циклoв игры."""
        while True:
            # Отслеживание событий клавиатуры и мыши.
            self._check_events()
            # self.ship.update()
            self._update_screen()


            # При каждом проходе цикла перерисовывается экран.
            self.screen.fill(self.bg_color)
            self.foto.blitme()
            # Отображение последнего прорисованного зкрана.
            pygame.display.flip()

    def _check_events(self):
        """Обрабатывает нажатие клавиш и события мыши"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        # нажатие клавиш
        if event.key == pygame.K_RIGHT:
            # переместить корабль вправо
            self.ship.moving_right = True
            # перемещает влево
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        # Реагирует на отпускание клавиш.
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

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





