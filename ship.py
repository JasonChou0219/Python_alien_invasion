# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 14:32:56 2020

@author: zijie
"""
import pygame

class Ship():
    """创建飞船对象，包括飞船的显示，飞船的控制移动等"""
    def __init__(self, game_setting, screen):
        """screen为surface类型"""
        #主画板
        #为什么要有这个赋值？ ->构造函数进行赋值，每次调用方法就不不要要进行传参了
        self.screen = screen
        self.setting = game_setting
        #加载飞船获取其外接矩形
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #初始化飞船位置
        self.rect.centerx =self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
#        self.rect.midbottom = self.screen.midbottom
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        """飞船的移动"""
        if self.moving_right and self.rect.right + self.setting.ship_speed \
        < self.screen_rect.right:   
            self.rect.centerx += self.setting.ship_speed
        if self.moving_left and self.rect.left - self.setting.ship_speed > 0:
            self.rect.centerx -= self.setting.ship_speed
        if self.moving_up and self.rect.top - self.setting.ship_speed > 0:
            self.rect.centery -= self.setting.ship_speed
        if self.moving_down and self.rect.bottom  + self.setting.ship_speed\
        < self.screen_rect.bottom:
            self.rect.centery += self.setting.ship_speed
    
    def blitme(self):
        """在主画板绘制飞船图案"""
        self.screen.blit(self.image, self.rect)
        