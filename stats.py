class GameStats:
    # 记录信息类
    def __init__(self, ab_settings):
        self.ab_settings = ab_settings
        self.game_active = False
        self.score = 0
        self.level = 1

        # 读取最高分
        self.get_highest_score()

        self.reset_stats()

    def get_highest_score(self):
        filename = 'record.txt'
        with open(filename, 'r') as file_object:
            self.highest_score = file_object.read()
            if not self.highest_score:
                self.highest_score = 0
        self.highest_score = int(self.highest_score)

        file_object.close()

    def set_highest_score(self):
        filename = 'record.txt'
        with open(filename, 'w') as file_object:
            highest_score_str = str(self.highest_score)
            file_object.write(highest_score_str)

        file_object.close()

    def reset_stats(self):
        # 初始化统计信息
        self.ship_life = self.ab_settings.ship_limit_life