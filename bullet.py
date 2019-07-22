import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, ab_settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        # 在(0, 0)创建子弹矩形
        self.rect = pygame.Rect(0, 0, ab_settings.bullet_width, ab_settings.bullet_height)
        # 移动子弹到飞船顶端
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)

        self.color = ab_settings.bullet_color
        self.speed = ab_settings.bullet_speed

    def update(self):
        # 更新子弹位置
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
