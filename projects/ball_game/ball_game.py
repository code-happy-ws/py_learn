import pygame as pg
import sys
import random
import time
# TODO definite game
def run_game():
    pg.init()
    pg.display.set_caption("送文爽的小游戏")
    game_window = pg.display.set_mode((600, 500))
    window_color = (100, 184, 221)
    ball_color = (30, 105, 46)
    rect_color = (30, 105, 46)
    ball_x = random.randint(20, 580)
    ball_y = random.randint(20, 100)
    move_x = 1
    move_y = 1
    score = 0
    point = 1
    count = 0
    font = pg.font.Font(None, 70)
    # todo
    while True:
        game_window.fill(window_color)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        mouse_x, mouse_y = pg.mouse.get_pos()
        pg.draw.circle(game_window, ball_color, (ball_x, ball_y), 20)
        pg.draw.rect(game_window, rect_color, (mouse_x, 490, 100, 10))
        ball_x += move_x
        ball_y += move_y
        my_text = font.render(str(score), False, (255, 255, 255))
        game_window.blit(my_text, (500, 30))

        if ball_x <= 20 or ball_x >= 580:
            move_x = -move_x
        if ball_y <= 20:
            move_y = -move_y
        if mouse_x - 20 <= ball_x <= mouse_x + 100 + 20 and ball_y > 470:
            move_y = -move_y
            score += point
            count += 1
            if count == 3:
                count = 0
                point += point
                if move_x > 0:
                    move_x += 1
                else:
                    move_x -= 1
                move_y -= 1
        if ball_y > 480 and (mouse_x - 20 > ball_x or ball_x > mouse_x + 100 + 20):
                break

        pg.display.update()

        time.sleep(0.005)
        # todo

run_game()