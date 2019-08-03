# @author: huhao
# @file: myplane.py
# @time: 2019/7/30 18:19
# @Document：https://www.python.org/doc/
# @desc:

import pygame

# fuction:
# __init__,
# moveUp,
# moveDown,
# moveLeft,
# moveRight,
# reset
class Myplane(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        # convert_alpha：
        # 修改图像（Surface 对象）的像素格式，包含 alpha 通道
        # 加载两张己方飞机图片
        self.image1 = pygame.image.load("./images/me1.png").convert_alpha()
        self.image2 = pygame.image.load("./images/me2.png").convert_alpha()

        self.destroy_image = []
        self.destroy_image.extend([\
            pygame.image.load("./images/me_destroy_1.png").convert_alpha(), \
            pygame.image.load("./images/me_destroy_2.png").convert_alpha(), \
            pygame.image.load("./images/me_destroy_3.png").convert_alpha(), \
            pygame.image.load("./images/me_destroy_4.png").convert_alpha()
        ])

        self.rect = self.image1.get_rect()
        # 规定游戏区域边界就是背景图片的宽高
        self.width, self.height = bg_size[0], bg_size[1]
        # 使飞机一出场就在中间区域
        self.rect.left, self.rect.top = \
            (self.width - self.rect.width) // 2, \
            self.height - self.rect.height -60
        # 规定飞机的速度，按键按一下移动10格
        self.speed = 10

        self.active = True

        # 无敌属性
        self.invincible = False

        # 返回图片非透明部分，用于碰撞检测
        self.mask = pygame.mask.from_surface(self.image1)

    def moveUp(self):
        # 判断是否越界
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0

    def moveDown(self):
        if self.rect.bottom < self.height - 60:
           self.rect.bottom += self.speed
        else:
            self.rect.bottom = self.height - 60

    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.left -=self.speed
        else:
            self.rect.left = 0

    def moveRight(self):
        if self.rect.right < self.width:
            self.rect.right += self.speed
        else:
            self.rect.right = self.width

    # 复活
    def reset(self):
        self.rect.left, self.rect.top = \
            (self.width - self.rect.width) // 2, \
            self.height - self.rect.height - 60
        self.active = True
        self.invincible = True





