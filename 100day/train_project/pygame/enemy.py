# @author: huhao
# @file: enemies.py
# @time: 2019/7/31 8:16
# @Document：https://www.python.org/doc/
# @desc:
'''
敌机分为大中小三种类型（定义3个class），
越大速度越慢
'''

import pygame
import random
from random import *

class SmallEnemy(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("./images/enemy1.png").convert_alpha()

        self.destroy_image = []
        self.destroy_image.extend([\
            pygame.image.load("./images/enemy1_down1.png"), \
            pygame.image.load("./images/enemy1_down2.png"), \
            pygame.image.load("./images/enemy1_down3.png"), \
            pygame.image.load("./images/enemy1_down4.png"), \
            ])

        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 2

        self.active = True

        # 返回图片非透明部分，用于碰撞检测
        self.mask = pygame.mask.from_surface(self.image)

        # 随机在-5个高度到0的位置生成敌机
        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), \
            randint(-5 * self.height, 0)

    def move(self):
        if self.rect.bottom < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), \
            randint(-5 * self.height, 0)


class MidEnemy(pygame.sprite.Sprite):
    energy = 8

    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("./images/enemy2.png").convert_alpha()

        self.hit_image = pygame.image.load("./images/enemy2_hit.png").convert_alpha()

        self.destroy_image = []
        self.destroy_image.extend([\
            pygame.image.load("./images/enemy2_down1.png"), \
            pygame.image.load("./images/enemy2_down2.png"), \
            pygame.image.load("./images/enemy2_down3.png"), \
            pygame.image.load("./images/enemy2_down4.png"), \
            ])

        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 1

        self.energy = MidEnemy.energy

        self.hit = False

        self.active = True

        # 返回图片非透明部分，用于碰撞检测
        self.mask = pygame.mask.from_surface(self.image)

        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), \
            randint(-10 * self.height, -self.height)

    def move(self):
        if self.rect.bottom < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.energy = MidEnemy.energy
        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), \
            randint(-10 * self.height, -self.height)


class BigEnemy(pygame.sprite.Sprite):
    energy = 20

    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        # 大型敌机存在飞行特效
        self.image1 = pygame.image.load("./images/enemy3_n1.png").convert_alpha()
        self.image2 = pygame.image.load("./images/enemy3_n2.png").convert_alpha()

        self.hit_image = pygame.image.load("./images/enemy3_hit.png").convert_alpha()


        self.destroy_image = []
        self.destroy_image.extend([ \
            pygame.image.load("./images/enemy3_down1.png"), \
            pygame.image.load("./images/enemy3_down2.png"), \
            pygame.image.load("./images/enemy3_down3.png"), \
            pygame.image.load("./images/enemy3_down4.png"), \
            pygame.image.load("./images/enemy3_down5.png"), \
            pygame.image.load("./images/enemy3_down6.png"), \
            ])

        self.rect = self.image1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 1
        self.energy = BigEnemy.energy

        self.hit = False

        self.active = True

        # 返回图片非透明部分，用于碰撞检测
        self.mask = pygame.mask.from_surface(self.image1)

        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), \
            randint(-13 * self.height, -5 * self.height)

    def move(self):
        if self.rect.bottom < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.energy = BigEnemy.energy
        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), \
            randint(-13 * self.height, -5 * self.height)