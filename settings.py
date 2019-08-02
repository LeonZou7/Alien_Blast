class Settings:

    def __init__(self):
        """静态全局设置"""

        # 窗口大小
        self.screen_width = 1200
        self.screen_height = 800

        # 背景色
        self.bg_color = (230, 230, 230)

        # 飞船设定
        self.ship_limit_life = 3

        # Alien设定
        self.alien_drop_speed = 5

        # 子弹设定
        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 12
        self.bullet_color = 60, 60, 60
        self.bullet_max = 5

        # 回合数记录
        self.round = 1

        # Level up
        self.speedup_scale = 1.2
        self.score_scale = 1.5
        self.init_dynamic_settings()

    def init_dynamic_settings(self):
        """初始化游戏速率"""
        self.ship_speed = 1.5
        self.bullet_speed = 2
        self.alien_speed = 1
        # 1 -> 右移， -1 -> 左移
        self.alien_fleet_direction = 1

        # Alien分数
        self.alien_points = 10

    def increase_speed(self):
        """速度提升"""
        self.round += 1
        self.alien_speed *= self.speedup_scale
        bullet_speedup = self.round % 2
        if bullet_speedup:
            self.bullet_speed *= self.speedup_scale
            self.ship_speed *= self.speedup_scale

        # 增加分数
        self.alien_points  = int(self.alien_points * self.score_scale)
