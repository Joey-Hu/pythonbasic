import pygame
import sys
import traceback
from pygame.locals import *
import myplane
import enemy
import bullet

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


def main():
    #  If the loops is -1 then the music will repeat indefinitely.
    pygame.mixer.music.play(-1)

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
    BULLET_NUM = 5
    for i in range(BULLET_NUM):
        bullet1.append(bullet.Bullet1(me.rect.midtop))

    # an object to track time
    clock = pygame.time.Clock()

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

    while running:
        # get events from the queue
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

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

        screen.blit(background, (0,0))

        # 每十帧发射一颗子弹
        if not(delay % 10):
            bullet1[bullet1_index].reset(me.rect.midtop)
            bullet1_index = (bullet1_index + 1) % BULLET_NUM

        # 检测子弹是否击中敌机
        for b in bullet1:
            if b.active:
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
                        each.reset()

        # 检测我方飞机是否碰撞
        enemy_down = pygame.sprite.spritecollide(me, enemies, False, pygame.sprite.collide_mask)
        if enemy_down:
            # me.active = False
            for e in enemy_down:
                e.active = False

        # 绘制我方飞机
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
                    # 游戏结束
                    print("GAME OVER!")
                    running = False

        # 在循环内不断切换,5帧切换一次
        if not(delay % 5):
            switch_image = not switch_image
        delay -= 1
        if not delay:
            delay = 100

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