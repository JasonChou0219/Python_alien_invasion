# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 16:27:05 2020

@author: zijie
"""

import sys
import pygame
from bullet import Bullet
from alien import Alien

def fire(game_setting, screen, ship, bullets, last_time):
    """当距离上一次开火超过设定间距时允许开火，发射子弹"""
    current_time = pygame.time.get_ticks()
    interval= current_time - last_time.value
    if interval >= 1000:
        new_bullet = Bullet(game_setting, screen, ship)
        bullets.add(new_bullet) 
        last_time.value = current_time



def check_keydown_events(event, game_setting, screen, 
                         ship, bullets, last_time):
    """按键对应的操作"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        #创建一个子弹对象，加入到编组中
        fire(game_setting, screen, 
                         ship, bullets, last_time)
    elif event.key == pygame.K_q:
        pygame.quit()
        sys.exit()

            

def check_keyup_events(event, ship):
    """松开按键对应的操作"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:          
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(game_setting, screen, ship, bullets, last_time):
    """监听捕捉鼠标键盘的操作"""
#    pygame.time.delay(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_setting, screen, 
                                 ship, bullets, last_time)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
    
def update_screen(game_setting, screen, ship, bullets, aliens):
    """更新屏幕的元素，绘制屏幕"""
    screen.fill(game_setting.bg_color)
    #优先绘制子弹，会被飞船，ufo图层遮住
    #bullets是一个group 里面成员sprites是一个精灵元素集合
    for bullet in bullets.sprites():
        bullet.draw_bullet()
                
    ship.blitme()
#    for alien in aliens.sprites():
#        alien.blitme()
    aliens.draw(screen)
    #绘制屏幕：
    pygame.display.flip()

def update_bullets(bullets):
    """更行子弹群的状态"""
    bullets.update()
    #设计删除元素时 循环需要通过拷贝进行循环
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)

#def judge_alien_valid():
#    """判断产生的外星人是否会与其他外星人冲突"""
    
    
    
    

def create_aliens(game_setting, screen, aliens):
    while len(aliens) < game_setting.max_aliens:
#    if judge_alien_valid(game_setting, aliens) and len(aliens) < game_setting.max_aliens:
        alien = Alien(game_setting, screen)
        aliens.add(alien)
            

