# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 17:48:07 2020

@author: zijie
"""

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """对飞船子弹进行管理的类"""
    def __init__(self, game_setting, screen, ship):
        """飞船处创建子弹"""
        super().__init__()
        self.screen = screen
        
        #在默认位置创建子弹的矩形
        self.rect = pygame.Rect(0, 0, game_setting.bullet_width, 
                                game_setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        #self.bottom = ship.rect.top 
        self.rect.top = ship.rect.top
        #???????
        self.y = float(self.rect.y)
        
        self.color = game_setting.bullet_color
        self.speed = game_setting.bullet_speed
        
    def update(self):
        """控制子弹的移动"""
        self.y -= self.speed
        self.rect.y = self.y
    
    def draw_bullet(self):
        """绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
        
        