import pygame
from pygame.sprite import Sprite

class Attacker(Sprite):
    """对入侵者进行管理的类"""

    def __init__(self, game_settings, screen):
        # 继承Sprite
        super().__init__()
        self.screen= screen

        # 加载入侵者图像并获取其外接矩形
        self.image= pygame.image.load("images/attacker.bmp")
        self.rect = self.image.get_rect()
        self.rect.x=50
        self.rect.y=0

        # 初始化入侵者移动速度
        self.Attacker_speed = game_settings.attacker_speed

    # 绘制入侵者
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    # 控制入侵者向下以一定速度移动
    def update(self):
        self.rect.y += self.Attacker_speed
