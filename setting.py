# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 14:06:35 2020

@author: zijie
"""

class Settings():
    """储存游戏设置数据的类"""
    #一般关于关于配置的数据都可以设置成类
    def __init__(self):
        #窗口主画板设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        #飞船设置
        self.ship_speed = 1
        #子弹设置
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (240, 65, 85)
        self.alien_speed = 0.05
        self.max_aliens = 5
        