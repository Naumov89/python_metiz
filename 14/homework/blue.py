
import sys
import pygame
from foto import Foto

class Blue:
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()
        # Размер экрана
        self.screen = pygame.display.set_mode((1200, 700))
        pygame.display.set_caption("Alien")
        # Назначение цвета фона.
        self.bg_color = (0, 0, 230)

        self.foto = Foto(self)

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            # Отслеживание событий клавиатуры и мыши.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # При каждом проходе цикла перерисовывается экран.
            self.screen.fill(self.bg_color)
            self.foto.blitme()
            # Отображение последнего прорисованного зкрана.
            pygame.display.flip()

if __name__ in '__main__':
    # Создание экземпляра и запуск игры.
    b = Blue()
    b.run_game()