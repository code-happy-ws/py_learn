import pygame

class Defendor():
    """对防卫者进行管理的类"""

    def __init__(self, screen):
        """初始化防卫者设置"""
        self.screen = screen

        # 加载防卫者图像并获取其外接矩形
        self.image = pygame.image.load('images/defendor.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 防卫者初始位置为屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 初始不响应按键移动事件
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    # 设置按键后移动方向和距离
    def move(self):
        if self.moving_right:
            self.rect.centerx += 5
        if self.moving_left:
            self.rect.centerx -= 5
        if self.moving_up:
            self.rect.centery -= 5
        if self.moving_down:
            self.rect.centery += 5

    # 根据self.rect指定的位置将图像绘制屏幕上
    def blitme(self):
        self.screen.blit(self.image,self.rect)