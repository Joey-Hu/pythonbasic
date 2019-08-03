import pygame
import sys
import traceback
from pygame.locals import *
import myplane
import enemy
import bullet
import supply
import random

pygame.init()
# pygame module for loading and playing sounds
pygame.mixer.init()

bg_size = width, height = 480,700
# Initialize a window or screen for display
screen = pygame.display.set_mode(bg_size)
# Set the current window caption
pygame.display.set_caption("飞机大战")

# convert:
# 修改图像（Surface 对象）的像素格式
background = pygame.image.load("images/background.png").convert()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# 载入游戏音乐
pygame.mixer.music.load("sound/game_music.ogg")
pygame.mixer.music.set_volume(0.2)
bullet_sound = pygame.mixer.Sound("sound/bullet.wav")
bullet_sound.set_volume(0.2)
bomb_sound = pygame.mixer.Sound("sound/use_bomb.wav")
bomb_sound.set_volume(0.2)
supply_sound = pygame.mixer.Sound("sound/supply.wav")
supply_sound.set_volume(0.2)
get_bomb_sound = pygame.mixer.Sound("sound/get_bomb.wav")
get_bomb_sound.set_volume(0.2)
get_bullet_sound = pygame.mixer.Sound("sound/get_bullet.wav")
get_bullet_sound.set_volume(0.2)
upgrade_sound = pygame.mixer.Sound("sound/upgrade.wav")
upgrade_sound.set_volume(0.2)
enemy3_fly_sound = pygame.mixer.Sound("sound/enemy3_flying.wav")
enemy3_fly_sound.set_volume(0.2)
enemy1_down_sound = pygame.mixer.Sound("sound/enemy1_down.wav")
enemy1_down_sound.set_volume(0.2)
enemy2_down_sound = pygame.mixer.Sound("sound/enemy2_down.wav")
enemy2_down_sound.set_volume(0.2)
enemy3_down_sound = pygame.mixer.Sound("sound/enemy3_down.wav")
enemy3_down_sound.set_volume(0.5)
me_down_sound = pygame.mixer.Sound("sound/me_down.wav")
me_down_sound.set_volume(0.2)


def add_small_enemies(group1, group2, num):
    for i in range(num):
        e1 = enemy.SmallEnemy(bg_size)
        group1.add(e1)
        group2.add(e1)


def add_mid_enemies(group1, group2, num):
    for i in range(num):
        e1 = enemy.MidEnemy(bg_size)
        group1.add(e1)
        group2.add(e1)


def add_big_enemies(group1, group2, num):
    for i in range(num):
        e1 = enemy.BigEnemy(bg_size)
        group1.add(e1)
        group2.add(e1)


def inc_speed(target, inc):
    for each in target:
        each.speed += inc


def main():
    #  If the loops is -1 then the music will repeat indefinitely.
    pygame.mixer.music.play(-1)

    # create an object to help track time.
    # The clock also provides several functions to help control a game's framerate.
    clock = pygame.time.Clock()


    # 生成我方飞机
    me = myplane.Myplane(bg_size)

    # 生成敌机
    enemies = pygame.sprite.Group()

    # 生成敌方小飞机
    small_enemies = pygame.sprite.Group()
    add_small_enemies(small_enemies, enemies, 5)

    # 生成敌方中飞机
    mid_enemies = pygame.sprite.Group()
    add_mid_enemies(mid_enemies, enemies, 25)

    # 生成敌方大飞机
    big_enemies = pygame.sprite.Group()
    add_big_enemies(big_enemies, enemies, 3)

    # 生成普通子弹
    bullet1 = []
    bullet1_index = 0
    BULLET_NUM1 = 5
    for i in range(BULLET_NUM1):
        bullet1.append(bullet.Bullet1(me.rect.midtop))

    # 生成超级子弹
    bullet2 = []
    bullet2_index = 0
    BULLET_NUM2 = 16
    for i in range(BULLET_NUM2//2):
        bullet2.append(bullet.Bullet2((me.rect.centerx-33, me.rect.centery)))
        bullet2.append(bullet.Bullet2((me.rect.centerx+30, me.rect.centery)))

    # 得分
    score = 0
    score_font = pygame.font.Font("./font/font.ttf",36)

    # 难度等级
    level = 1

    # 定义全屏炸弹
    bomb_image = pygame.image.load("./images/bomb.png").convert_alpha()
    bomb_rect = bomb_image.get_rect()
    bomb_font = pygame.font.Font("./font/font.ttf", 48)
    bomb_num = 3

    # 每30s发放一个补给包
    bullet_supply = supply.BulletSupply(bg_size)
    bomb_supply = supply.BombSupply(bg_size)
    SUPPLY_TIME = USEREVENT
    pygame.time.set_timer(SUPPLY_TIME, 30 * 1000)

    # 游戏结束画面
    gameover_font = pygame.font.Font("font/font.ttf", 48)
    again_image = pygame.image.load("images/again.png").convert_alpha()
    again_rect = again_image.get_rect()
    gameover_image = pygame.image.load("images/gameover.png").convert_alpha()
    gameover_rect = gameover_image.get_rect()

    # 超级子弹定时器
    DOUBBLE_BULLET_TIME = USEREVENT + 1

    # 无敌时间计时器
    INVINCIBLE_TIME = USEREVENT + 2

    # 标志是否使用超级子弹
    is_doubble_bullet = False

    # 生命数量
    life_image = pygame.image.load("./images/life.png").convert_alpha()
    life_rect = life_image.get_rect()
    life_num = 3

    # 暂停设置
    paused = False
    pause_nor_image = pygame.image.load("./images/pause_nor.png").convert_alpha()
    pause_pressed_image = pygame.image.load("./images/pause_pressed.png").convert_alpha()
    resume_nor_image = pygame.image.load("./images/resume_nor.png").convert_alpha()
    resume_pressed_image = pygame.image.load("./images/resume_pressed.png").convert_alpha()
    pause_rect = pause_nor_image.get_rect()
    pause_rect.left, pause_rect.top = width - pause_rect.width - 10, 10
    pause_image = pause_nor_image

    # 飞机爆炸索引
    e1_destroy_index = 0
    e2_destroy_index = 0
    e3_destroy_index = 0
    me_destroy_index = 0

    # 用于切换图片
    switch_image = True

    # 用于延迟
    delay = 100
    running = True

    # 用于限制重复打开存取记录
    recorded = False

    while running:
        # get events from the queue
        for event in pygame.event.get():
            # 游戏退出事件
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # 鼠标点击事件
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and pause_rect.collidepoint(event.pos):
                    paused = not paused
                    if paused:
                        pygame.time.set_timer(SUPPLY_TIME, 0)
                        pygame.mixer.music.pause()
                        pygame.mixer.pause()
                    else:
                        pygame.time.set_timer(SUPPLY_TIME, 30 * 1000)
                        pygame.mixer.music.unpause()
                        pygame.mixer.unpause()

            # 鼠标移动事件（悬停）
            elif event.type == MOUSEMOTION:
                if pause_rect.collidepoint(event.pos):
                    if paused:
                        pause_image = resume_pressed_image
                    else:
                        pause_image = pause_pressed_image
                else:
                    if paused:
                        pause_image = resume_nor_image
                    else:
                        pause_image = pause_nor_image

            # 空格点击事件
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if bomb_num:
                        bomb_num -= 1
                        bomb_sound.play()
                        for each in enemies:
                            if each.rect.bottom > 0:
                                each.active = False

            elif event.type == SUPPLY_TIME:
                supply_sound.play()
                if random.choice([True, False]):
                    bullet_supply.reset()
                else:
                    bomb_supply.reset()

            elif event.type == DOUBBLE_BULLET_TIME:
                is_doubble_bullet = False
                pygame.time.set_timer(DOUBBLE_BULLET_TIME, 0)

            elif event.type == INVINCIBLE_TIME:
                me.invincible = False
                # 结束无敌时间计时器
                pygame.time.set_timer(INVINCIBLE_TIME, 0)

        # 根据用户的得分增加难度
        if level == 1 and score > 50000:
            level = 2
            upgrade_sound.play()
            # 增加3架小型敌机、2架中型敌机和1架大型敌机
            add_small_enemies(small_enemies, enemies, 3)
            add_mid_enemies(mid_enemies, enemies, 2)
            add_big_enemies(big_enemies, enemies, 1)
            # 提升小型敌机速度
            inc_speed(small_enemies, 1)
        elif level == 2 and score > 300000:
            level = 3
            upgrade_sound.play()
            # 增加5架小型敌机、3架中型敌机和2架大型敌机
            add_small_enemies(small_enemies, enemies, 5)
            add_mid_enemies(mid_enemies, enemies, 3)
            add_big_enemies(big_enemies, enemies, 2)
            # 提升小型敌机速度
            inc_speed(small_enemies, 1)
            # 提升中型敌机速度
            inc_speed(mid_enemies, 1)
        elif level == 3 and score > 600000:
            level = 4
            upgrade_sound.play()
            # 增加5架小型敌机、3架中型敌机和2架大型敌机
            add_small_enemies(small_enemies, enemies, 5)
            add_mid_enemies(mid_enemies, enemies, 3)
            add_big_enemies(big_enemies, enemies, 2)
            # 提升小型敌机速度
            inc_speed(small_enemies, 1)
            # 提升中型敌机速度
            inc_speed(mid_enemies, 1)
        elif level == 4 and score > 1000000:
            level = 5
            upgrade_sound.play()
            # 增加5架小型敌机、3架中型敌机和2架大型敌机
            add_small_enemies(small_enemies, enemies, 5)
            add_mid_enemies(mid_enemies, enemies, 3)
            add_big_enemies(big_enemies, enemies, 2)
            # 提升小型敌机速度
            inc_speed(small_enemies, 1)
            # 提升中型敌机速度
            inc_speed(mid_enemies, 1)

        # 绘制背景图片
        # blit: draw one image onto another
        # surface.blit(source, dest, area=None, special_flags=0) -> Rect
        screen.blit(background, (0, 0))

        if life_num > 0 and not paused:
            # 检测用户的键盘操作
            key_press = pygame.key.get_pressed()
            if key_press[K_w] or key_press[K_UP]:
                me.moveUp()
            if key_press[K_s] or key_press[K_DOWN]:
                me.moveDown()
            if key_press[K_a] or key_press[K_LEFT]:
                me.moveLeft()
            if key_press[K_d] or key_press[K_RIGHT]:
                me.moveRight()

            # 检测全屏炸弹补给并检测是否获得
            if bomb_supply.active:
                bomb_supply.move()
                screen.blit(bomb_supply.image, bomb_supply.rect)
                if pygame.sprite.collide_mask(bomb_supply, me):
                    get_bomb_sound.play()
                    if bomb_num < 3:
                        bomb_num += 1
                    bomb_supply.active = False

            # 检测超级子弹补给并检测是否获得
            if bullet_supply.active:
                bullet_supply.move()
                screen.blit(bullet_supply.image, bullet_supply.rect)
                if pygame.sprite.collide_mask(bullet_supply, me):
                    get_bullet_sound.play()
                    is_doubble_bullet = True
                    pygame.time.set_timer(DOUBBLE_BULLET_TIME, 18 * 1000)
                    bullet_supply.active = False

            # 每十帧发射一颗子弹
            if not(delay % 10):
                bullet_sound.play()
                if is_doubble_bullet:
                    bullets = bullet2
                    bullets[bullet2_index].reset((me.rect.centerx-33, me.rect.centery))
                    bullets[bullet2_index+1].reset((me.rect.centerx+30, me.rect.centery))
                    bullet2_index = (bullet2_index + 2) % BULLET_NUM2

                else:
                    bullets = bullet1
                    bullets[bullet1_index].reset(me.rect.midtop)
                    bullet1_index = (bullet1_index + 1) % BULLET_NUM1

            # 检测子弹是否击中敌机
            for b in bullets:
                if b.active:
                    # 绘制子弹
                    b.move()
                    screen.blit(b.image, b.rect)
                    # enemy_hit中存放由pygame.sprite.spritecollide返回的敌机对象
                    enemy_hit = pygame.sprite.spritecollide(b,enemies, False, pygame.sprite.collide_mask)
                    if enemy_hit:
                        b.active = False
                        for e in enemy_hit:
                            if e in big_enemies or e in mid_enemies:
                                e.hit = True
                                e.energy -= 1
                                if e.energy == 0:
                                    e.active = False
                            else:
                                e.active = False

            # 绘制大型敌机(是大型敌机在最里面，小飞机在最外面)
            for each in big_enemies:
                if each.active:
                    each.move()

                    if each.hit:
                        screen.blit(each.hit_image, each.rect)
                        each.hit = False
                    else:
                        if switch_image:
                            screen.blit(each.image1, each.rect)
                        else:
                            screen.blit(each.image2, each.rect)

                    # 绘制血槽
                    # 绘制底槽
                    pygame.draw.line(screen, BLACK, \
                                     (each.rect.left, each.rect.top -5), \
                                     (each.rect.right, each.rect.top - 5), \
                                     2)

                    # 当生命值大于20%时显示绿色，否则显示红色
                    energy_remain = each.energy / enemy.BigEnemy.energy
                    if energy_remain > 0.2:
                        energy_color = GREEN
                    else:
                        energy_color = RED

                    # 绘制血量
                    pygame.draw.line(screen, energy_color, \
                                     (each.rect.left, each.rect.top - 5), \
                                     (each.rect.left + energy_remain * each.rect.width, each.rect.top - 5), \
                                     2)

                # 即将出现在画面中，播放音效
                    if each.rect.bottom == -50:
                        enemy3_fly_sound.play(-1)
                else:
                    # 毁灭
                    if not (delay % 3):
                        if e3_destroy_index == 0:
                            enemy3_down_sound.play()
                        screen.blit(each.destroy_image[e3_destroy_index], each.rect)
                        e3_destroy_index = (e3_destroy_index+1) % 6
                        if e3_destroy_index == 0:
                            enemy3_fly_sound.stop()
                            score += 10000
                            each.reset()

            # 绘制中型敌机
            for each in mid_enemies:
                if each.active:
                    each.move()

                    if each.hit:
                        screen.blit(each.hit_image, each.rect)
                        each.hit = False
                    else:
                        screen.blit(each.image, each.rect)

                    # 绘制血槽
                    # 绘制底槽
                    pygame.draw.line(screen, BLACK, \
                                     (each.rect.left, each.rect.top - 5), \
                                     (each.rect.right, each.rect.top - 5), \
                                     2)

                    # 当生命值大于20%时显示绿色，否则显示红色
                    energy_remain = each.energy / enemy.MidEnemy.energy
                    if energy_remain > 0.2:
                        energy_color = GREEN
                    else:
                        energy_color = RED

                    # 绘制血量
                    pygame.draw.line(screen, energy_color, \
                                     (each.rect.left, each.rect.top - 5), \
                                     (each.rect.left + energy_remain * each.rect.width, each.rect.top - 5), \
                                     2)
                else:
                    # 毁灭
                    if not(delay % 3):
                        if e2_destroy_index == 0:
                            enemy2_down_sound.play()
                        screen.blit(each.destroy_image[e2_destroy_index], each.rect)
                        e2_destroy_index = (e2_destroy_index+1) % 4
                        if e2_destroy_index == 0:
                            score += 6000
                            each.reset()

            # 绘制小型敌机
            for each in small_enemies:
                if each.active:
                    each.move()
                    screen.blit(each.image, each.rect)
                else:
                    # 毁灭
                    if not (delay % 3):
                        if e1_destroy_index == 0:
                            enemy1_down_sound.play()
                        screen.blit(each.destroy_image[e1_destroy_index], each.rect)
                        e1_destroy_index = (e1_destroy_index + 1) % 4
                        if e1_destroy_index == 0:
                            score += 1000
                            each.reset()

            # 检测我方飞机是否碰撞
            enemy_down = pygame.sprite.spritecollide(me, enemies, False, pygame.sprite.collide_mask)
            if enemy_down and not me.invincible:
                me.active = False
                for e in enemy_down:
                    e.active = False

            # 绘制我方飞机(动态效果)
            if me.active:
                if switch_image:
                    screen.blit(me.image1, me.rect)
                else:
                    screen.blit(me.image2, me.rect)
            else:
                # 毁灭
                if not(delay % 3):
                    if me_destroy_index == 0:
                        me_down_sound.play()
                    screen.blit(me.destroy_image[me_destroy_index], me.rect)
                    me_destroy_index = (me_destroy_index+1) % 4
                    if me_destroy_index == 0:
                        life_num -= 1
                        me.reset()
                        # 调用无敌时间计时器
                        pygame.time.set_timer(INVINCIBLE_TIME, 3 * 1000)

            # 绘制全屏炸弹数量
            bomb_text = bomb_font.render("x %d" % bomb_num, True, WHITE)
            text_rect = bomb_text.get_rect()
            screen.blit(bomb_image, (10, height - 10 - bomb_rect.height))
            screen.blit(bomb_text, (20 + bomb_rect.width, height - 5 - bomb_rect.height))

            # 绘制生命数量
            if life_num > 0:
                for i in range(life_num):
                    screen.blit(life_image,\
                                (width - 10 - (i+1) * life_rect.width, \
                                 height - 10 - life_rect.height))

            # 绘制分数
            score_text = score_font.render("Score : %s" % str(score), True, WHITE)
            screen.blit(score_text, (10, 5))


        # 绘制游戏结束画面
        elif life_num == 0:
            # 背景音乐停止
            pygame.mixer.music.stop()
            # 停止音效
            pygame.mixer.stop()

            # 停止发放补给
            pygame.time.set_timer(SUPPLY_TIME, 0)

            if not recorded:
                recorded = True
                # 读取历史最高得分
                with open("D:\\Desktop\\python\\python_basics\\100day\\train_project\\pygame\\record.txt", "r") as f:
                    record_score = int(f.read())

                # 如果玩家分数高于历史最高峰，则存档
                if score > record_score:
                    with open("D:\\Desktop\\python\\python_basics\\100day\\train_project\\pygame\\record.txt", "w") as f:
                        f.write(str(score))

            # 绘制结束画面
            record_score_text = score_font.render("Best: %d" % record_score, True, WHITE)
            screen.blit(record_score_text, (50, 50))

            gameover_text1 = gameover_font.render("Your Score: ", True, WHITE)
            gameover_text1_rect = gameover_text1.get_rect()
            gameover_text1_rect.left, gameover_text1_rect.top = \
                (width - gameover_text1_rect.width) // 2, height // 2
            screen.blit(gameover_text1, gameover_text1_rect)

            gameover_text2 = gameover_font.render(str(score), True, WHITE)
            gameover_text2_rect = gameover_text2.get_rect()
            gameover_text2_rect.left, gameover_text2_rect.top = \
                (width - gameover_text2_rect.width) // 2, \
                gameover_text1_rect.bottom + 10
            screen.blit(gameover_text2, gameover_text2_rect)

            again_rect.left, again_rect.top = \
                (width - again_rect.width) // 2, \
                gameover_text2_rect.bottom + 50
            screen.blit(again_image, again_rect)

            gameover_rect.left, gameover_rect.top = \
                (width - again_rect.width) // 2, \
                again_rect.bottom + 10
            screen.blit(gameover_image, gameover_rect)


        # 绘制暂停按钮
        screen.blit(pause_image,pause_rect)

        # 在循环内不断切换,5帧切换一次
        if not(delay % 5):
            switch_image = not switch_image
        delay -= 1
        if not delay:
            delay = 100

        # 更新整个待显示的 Surface 对象到屏幕上
        pygame.display.flip()

        clock.tick(60)

if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
