import pygame as pg
from settings import Settings
from defendor import Defendor
import function as func
from pygame.sprite import Group
from time import sleep
from status import gamestatus
from button import Button


def run_game():
    """启动游戏"""
    # 初始化游戏
    pg.init()

    # 创建Settings实例，进行游戏参数设置
    game_settings = Settings()
    screen = pg.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    play_button = Button(game_settings,screen ,"Play")
    pg.display.set_caption("Shot game")

    # 创建gamestatus实例以访问游戏状态设置
    game_status= gamestatus()

    # 在screen上绘制防御者
    defendor= Defendor(screen)

    # 创建存储子弹的编组
    bullets = Group()

    # 创建存储入侵者的编组
    attackers= Group()

    # 创建入侵者军队
    func.creat_attackers(game_settings,screen,attackers)

    # 开始游戏主循环
    while True:

        # 响应键盘或者鼠标事件
        func.check_events(game_settings, screen, defendor, bullets, game_status, play_button)

        # 屏幕元素画面显示
        func.move_screen(game_settings, defendor, screen, bullets, attackers, play_button, game_status)
        sleep(0.02)

        # 激活游戏状态后，各种游戏元素按照参数移动响应
        if game_status.game_active == True:
            # 移动防卫者
            defendor.move()
            # 移动子弹
            func.move_bullets(game_settings, screen, bullets, attackers)
            # 移动入侵者
            func.move_attackers(attackers)


# 启动游戏
run_game()
