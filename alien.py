import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, ab_settings, screen):

        super(Alien, self).__init__()
        self.ab_settings = ab_settings
        self.screen = screen

        # 初始化Alien
        self.image = pygame.image.load('img/Alien.bmp')
        self.rect = self.image.get_rect()

        # 放置Alien于屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def check_edge(self):
        screnn_rect = self.screen.get_rect()
        if self.rect.right >= screnn_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        self.x += self.ab_settings.alien_speed * self.ab_settings.alien_fleet_direction
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)