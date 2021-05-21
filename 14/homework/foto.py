
import pygame

class Foto():
    '''Класс для управления.'''

    def __init__(self, b_game):
        '''Инициализирует ФОТО задает его начальную позицию.'''

        self.screen = b_game.screen
        self.screen_rect = b_game.screen.get_rect()

        # Загружает изображение и получает прямоугольник.
        self.image = pygame.image.load('homework/alien3.bmp')
        self.rect = self.image.get_rect()

        # Каждое новое фото появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        '''Рисует фото в текущей позиции.'''
        self.screen.blit(self.image, self.rect)