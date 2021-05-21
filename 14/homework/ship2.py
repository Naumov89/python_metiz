
import pygame

class Ship():
    '''Класс для управления кораблем.'''

    def __init__(self, ai_game):
        '''Инициализирует корабль и задает его начальную позицию.'''

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Загружает изображение корабля и получает прямоугольник.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom
        # сохранение вещественнойкоординаты центра корабля.
        self.x = float(self.rect.x)
        # флаг перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''Обновляет позицию корабля с учетом флага.'''
        # Обновляется атрибут x, не rect.
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed
        
        # Обновление атрибута rect на основании self.x.
        self.rect.x = self.x

    def blitme(self):
        '''Рисует корабль в текущей позиции.'''
        self.screen.blit(self.image, self.rect)