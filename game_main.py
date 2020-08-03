# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pygame
from setting import Settings
from ship import Ship
from pygame.sprite import Group
import game_function as gf
from pass_by_refernce import PassByReference


def run_game():
    #初始化屏幕对象
    pygame.init()
    game_setting = Settings()
    screen = pygame.display.set_mode(
            (game_setting.screen_width, game_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    #要素
    ship = Ship(game_setting, screen)
#    alien = Alien(game_setting, screen)
    
    bullets = Group()
    aliens = Group() 
    gf.create_aliens(game_setting, screen, aliens)
    
    last_time = PassByReference(pygame.time.get_ticks())
    #游戏循环
    while True:
        #捕捉键盘鼠标事件
        gf.check_events(game_setting, screen, 
                                    ship, bullets, last_time)
        ship.update()    
        gf.update_bullets(bullets)
        aliens.update()
        gf.update_screen(game_setting, screen, ship, bullets, aliens)
        
        
        
run_game()