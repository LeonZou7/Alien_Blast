class GameStats:
    # 记录信息类
    def __init__(self, ab_settings):
        self.ab_settings = ab_settings
        self.game_active = False
        self.score = 0
        self.reset_stats()

    def reset_stats(self):
        # 初始化统计信息
        self.ship_life = self.ab_settings.ship_limit_life