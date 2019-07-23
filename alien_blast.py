import pygame
import functions as func

from settings import Settings
from ship import Ship
from stats import GameStats
from button import Button
from score_board import Scoreboard
from pygame.sprite import Group


def run_game():

    # 初始化窗口
    pygame.init()
    ab_settings = Settings()

    # 设置分辨率
    screen = pygame.display.set_mode((ab_settings.screen_width, ab_settings.screen_height))

    # 设置标题
    pygame.display.set_caption("Alien Blast")

    # 创建按钮
    play_button = Button(ab_settings, screen, "Play")

    # 设置统计信息
    stats = GameStats(ab_settings)

    # 创建计分器
    scoreboard = Scoreboard(ab_settings, screen, stats)

    # 放置飞船
    ship = Ship(ab_settings, screen)

    # Alien编组
    aliens = Group()
    func.create_fleet(ab_settings, screen, ship, aliens)

    # 子弹编组
    bullets = Group()

    while True:
        # 检查事件
        func.check_events(ab_settings, screen, stats, play_button, ship, aliens, bullets)

        if stats.game_active:
            # 飞船事件
            ship.update()

            # Alien事件
            func.update_aliens(ab_settings, stats, screen, ship, aliens, bullets)

            # 子弹事件
            func.update_bullets(ab_settings, screen, ship, aliens, bullets)

        # 重绘屏幕
        func.update_screen(ab_settings, screen, stats, scoreboard, ship, aliens, bullets, play_button)


run_game()
