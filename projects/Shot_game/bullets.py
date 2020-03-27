import  pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """管理子弹的类"""

    def __init__(self, game_settings, screen, defendor):
         super().__init__()
         self.screen = screen

         #子弹位置及大小设置
         self.bullet_x= defendor.rect.centerx
         self.bullet_y= defendor.rect.centery
         self.bullet_color= game_settings.bullet_color
         self.bullet_radius = 5

    def update(self):
        """子弹向上移动"""
        self.bullet_y -= 8

    def draw_bullet(self):
        """绘制子弹"""
        pygame.draw.circle(self.screen, self.bullet_color, (self.bullet_x, self.bullet_y), self.bullet_radius)

