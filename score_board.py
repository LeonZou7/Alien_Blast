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

    def prep_score(self):
        score_str = str(self.stats.score)

        # 渲染图像
        self.score_image = self.font.render(score_str, True, self.text_color, self.ab_settings.bg_color)

        # 放置图像
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 10
        self.score_rect.top = 10

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
