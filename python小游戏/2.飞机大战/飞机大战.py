import pygame
from pygame.constants import *
import time


def main():
    """完成整个程序的控制"""
    #1 创建一个窗口
    screen=pygame.display.set_mode((299,582),0,24)
    #2 创建一个图片，当做背景
    background=pygame.image.load("./plane/background.png")
    # 2 创建一个图片，玩家飞机
    player = pygame.image.load("./plane/hero1.png")
    x = 299 / 2 - 80 / 2
    y = 490
    #飞机速度
    speed=10

    while True:
        # 3 将背景图片贴到窗口中
        screen.blit(background, (0, 0))
        # 3 将背景图片贴到窗口中
        screen.blit(player, (x, y))  # 找的飞机图片可能太大

        #获取事件
        for event in pygame.event.get():
            #判断事件类型
            if event.type==QUIT:
                #执行pygame退出
                pygame.quit()
                #python程序退出
                exit()
        #监听键盘事件,键盘的连续监听
        key_pressed = pygame.key.get_pressed()

        if key_pressed[K_w] or key_pressed[K_UP]:
            print("上")
            y-=speed
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            print("下")
            y+=speed
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            print("左")
            x-=speed
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            print("右")
            x+=speed
        if key_pressed[K_SPACE]:
            print("空格")
        #4 显示窗口中的内容
        pygame.display.update()
        time.sleep(0.01)

if __name__ == '__main__':
    main()



