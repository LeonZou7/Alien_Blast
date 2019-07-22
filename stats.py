class GameStats:
    # 记录信息类
    def __init__(self, ab_settings):
        self.ab_settings = ab_settings
        self.game_active = False
        self.reset_states()

    def reset_states(self):
        # 初始化统计信息
        self.ship_life = self.ab_settings.ship_limit_life