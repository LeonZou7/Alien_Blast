import pygame.font


class Scoreboard:
    def __init__(self, ab_settings, screen, stats):
        self.ab_settings = ab_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats

        # 字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # 初始化图像
        self.prep_score()
        self.prep_highest_score()

    def prep_score(self):
        # 得分圆整化
        rounded_score = round(self.stats.score, -1)
        # 输出规格化 （1000 -> 1,000）
        score_str = "{:,}".format(rounded_score)

        # 渲染图像
        self.score_image = self.font.render(score_str, True, self.text_color, self.ab_settings.bg_color)

        # 放置图像
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 10
        self.score_rect.top = 10

    def prep_highest_score(self):
        # 最高分圆整化
        highest_score = round(self.stats.highest_score, -1)
        # 输出规格化
        highest_score_str = "{:,}".format(highest_score)

        # 渲染图像
        self.highest_score_image = self.font.render(highest_score_str, True, self.text_color, self.ab_settings.bg_color)

        # 放置图像
        self.highest_score_rect = self.highest_score_image.get_rect()
        self.highest_score_rect.centerx = self.screen_rect.centerx
        self.highest_score_rect.top = self.screen_rect.top

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.highest_score_image, self.screen_rect)
