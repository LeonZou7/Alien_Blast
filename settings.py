class Settings:

    def __init__(self):

        # 窗口大小
        self.screen_width = 1200
        self.screen_height = 800

        # 背景色
        self.bg_color = (230, 230, 230)

        # 飞船设定
        self.ship_speed = 1.5
        self.ship_limit_life = 3

        # Alien设定
        self.alien_speed = 1
        self.alien_drop_speed = 5
        # 1 -> 右移， -1 -> 左移
        self.alien_fleet_direction = 1

        # 子弹
        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 12
        self.bullet_color = 60, 60, 60
        self.bullet_max = 5
