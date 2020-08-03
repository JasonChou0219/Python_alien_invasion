# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 01:17:19 2020

@author: zijie
"""
import pygame
from pygame.sprite import Sprite
import random

class Alien(Sprite):
    """管理外星人的类"""
    
    def __init__(self, game_setting, screen):
        super().__init__()
        self.screen = screen
        self.game_setting = game_setting
        
        #加载图像
        self.image = pygame.image.load("images/ufoooo.png")
        #rect对象获取图片对应的矩形
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #位置的初始化
        self.rect.x = random.randint(0, 
                                     self.screen_rect.right - self.rect.width)
        self.rect.y = -self.rect.height
#        self.rect.x = self.rect.width
#        self.rect.y = self.rect.height
        
        #存储外星人准确的位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    
    def update(self):
        self.y += self.game_setting.alien_speed
        self.rect.y = self.y
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        