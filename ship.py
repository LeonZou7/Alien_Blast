import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, ab_settings, screen):

        super(Ship, self).__init__()

        self.ab_settings = ab_settings
        self.screen = screen

        # 初始化飞船图像
        self.image = pygame.image.load('img/Ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 放置飞船于窗口底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        # 移动标志
        self.move_left = False
        self.move_right = False

    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += self.ab_settings.ship_speed
        elif self.move_left and self.rect.left > 0:
            self.center -= self.ab_settings.ship_speed

        self.rect.centerx = self.center

    def center_ship(self):
        self.center = self.screen_rect.centerx

    def blitme(self):

        # 在指定位置绘制飞船
        self.screen.blit(self.image, self.rect)
