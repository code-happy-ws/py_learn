import sys
import pygame as pg
from bullets import Bullet
from attacker import Attacker


def check_events(game_settings, screen, defendor, bullets,game_status,play_button):
    """响应按键和鼠标事件"""

    for event in pg.event.get():

        # 响应点击退出游戏事件
        if event.type == pg.QUIT:
            sys.exit()

        # 响应点击"play"按钮事件
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pg.mouse.get_pos()
            check_play_button(play_button,mouse_x,mouse_y,game_status)

        # 响应通过箭头按键移动位置事件
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                defendor.moving_right = True
            if event.key == pg.K_UP:
                defendor.moving_up = True
            if event.key == pg.K_DOWN:
                defendor.moving_down = True
            if event.key == pg.K_LEFT:
                defendor.moving_left = True

            # 响应通过空格发射子弹事件
            if event.key == pg.K_SPACE:
                new_bullet =Bullet(game_settings, screen, defendor)
                bullets.add(new_bullet)

            # 响应通过q键退出游戏事件
            if event.key == pg.K_q:
                sys.exit()

        # 响应松开按键停止移动事件
        elif event.type == pg.KEYUP:
            if event.key == pg.K_RIGHT:
                defendor.moving_right = False
            if event.key == pg.K_LEFT:
                defendor.moving_left = False
            if event.key == pg.K_UP:
                defendor.moving_up = False
            if event.key == pg.K_DOWN:
                defendor.moving_down = False

def check_play_button(play_button,mouse_x,mouse_y,game_status):
    """点击play按钮后激活游戏状态"""
    if play_button.rect.collidepoint(mouse_x,mouse_y):
        game_status.game_active=True

def move_screen(game_settings,defendor,screen,bullets,attackers,play_button,game_status):
    """绘制屏幕元素"""

    # 填充屏幕颜色
    screen.fill(game_settings.background_color)
    # 绘制防卫者
    defendor.blitme()
    # 绘制入侵者军队
    attackers.draw(screen)

    # 绘制子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # 绘制得分
    font = pg.font.Font(None,50)
    my_score = font.render(str(game_settings.score), False, (255, 255, 255))
    screen.blit(my_score, (212, 10))

    #绘制开始按钮
    if not game_status.game_active:
        play_button.draw_button()

    # 不断出现新屏幕，擦掉旧屏幕
    pg.display.flip()


def move_bullets(game_settings,screen,bullets,attackers):
    """子弹移动设置"""

    # 子弹发射后向上移动
    bullets.update()

    for bullet in bullets.copy():
        for attacker in attackers.copy():
            # 子弹飞出屏幕之外后消失
            if bullet.bullet_y<= 0:
                bullets.remove(bullet)
            # 子弹碰撞目标后消失
            if attacker.rect.x <= bullet.bullet_x and bullet.bullet_x < attacker.rect.x+50 \
                and bullet.bullet_y < attacker.rect.y+50 and bullet.bullet_y > attacker.rect.y:
                bullets.remove(bullet)
                attackers.remove(attacker)
                game_settings.score +=1

    # 入侵者军队全部被消灭后重新生成并加快移动速度以增加难度
    if len(attackers)==0 :
        creat_attackers(game_settings,screen, attackers)
        game_settings.attacker_speed += 0.5

def creat_attackers(game_settings,screen, attackers):
    """生成入侵者军队"""
    for row in range(3):
        for num in range(9):
            attacker=Attacker(game_settings, screen)
            attacker.rect.x= 55*  num + 10
            attacker.rect.y = 50 * row+50
            attackers.add(attacker)

def move_attackers(attackers):
    """移动入侵者军队"""
    attackers.update()



