import pygame


class Button():
    """管理按钮的类"""
    def __init__(self,game_settings,screen,txt):
        """初始参数设置"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width, self.height = 200,50
        self.button_color = (0,255,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)

        #创建按钮的rect对象
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.toimage(txt)

    def toimage(self, txt):
        """将字符串内容渲染成图片"""
        self.txt_image = self.font.render(txt,True,self.text_color,self.button_color)
        self.txt_image_rect = self.txt_image.get_rect()
        self.txt_image_rect.center = self.rect.center

    def draw_button(self):
        """先绘制按钮，再绘制文本"""
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.txt_image,self.txt_image_rect)

