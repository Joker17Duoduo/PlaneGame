import random
import pygame
from pygame.constants import *
import time
import self
import sys


class HeroPlane(object):#玩家飞机类
    def __init__(self, screen):  # 飞机属性类,窗口也变成飞机类的一个属性
        # 2 创建一个图片，玩家飞机
        self.player = pygame.image.load("./plane/hero1.png")
        self.x = 299 / 2 - 80 / 2
        self.y = 490
        # 飞机速度
        self.speed = 10
        # 记录当前的窗口对象
        self.screen = screen
        # 装子弹的列表
        self.bullets = []

    def key_control(self):
        # 监听键盘事件,键盘的连续监听
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_w] or key_pressed[K_UP]:
            self.y -= self.speed
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            self.y += self.speed
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            self.x -= self.speed
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            self.x += self.speed
        if key_pressed[K_SPACE]:
            # 按空格键发射子弹
            bullet = Bullet(self.screen, self.x, self.y)
            # 把子弹放到列表里
            self.bullets.append(bullet)

    def display(self):
        # 3 将背景图片贴到窗口中
        # self.screen.blit(self.player, (self.x, self.y))  # 找的飞机图片可能太大
        # 将飞机图片贴到窗口中
        self.screen.blit(self.player, (self.x, self.y))
        # 遍历所有子弹
        for bullet in self.bullets:
            # 让子弹飞 修改子弹y坐标
            bullet.auto_move()
            # 子弹显示在窗口
            bullet.display()


class EnemyPlane(object):#敌机类
    def __init__(self, screen):  # 飞机属性类,窗口也变成飞机类的一个属性
        # 2 创建一个图片，玩家飞机
        self.player = pygame.image.load("./plane/enemy0.png")  # 56×39
        self.x = 0
        self.y = 0
        # 飞机速度
        self.speed = 2
        # 记录当前的窗口对象
        self.screen = screen
        # 装子弹的列表
        self.bullets = []
        # 敌机移动方向
        self.direction = 'right'

    def display(self):
        # 3 将背景图片贴到窗口中
        self.screen.blit(self.player, (self.x, self.y))  # 找的飞机图片可能太大
        # 遍历所有子弹
        for bullet in self.bullets:
            # 让子弹飞 修改子弹y坐标
            bullet.auto_move()
            # 子弹显示在窗口
            bullet.display()  # 快捷键ctrl+/可以快捷注释

    def auto_move(self):
        if self.direction == 'right':
            self.x += self.speed
        elif self.direction == 'left':
            self.x -= self.speed
        if self.x > 299 - 56:
            self.direction = 'left'
        elif self.x < 0:
            self.direction = 'right'

    def auto_fire(self):
        """子弹开火 创建子弹对象 添加进列表"""
        random_num = random.randint(1, 30)  # Alt+回车可以快捷键导入下载模块
        if random_num == 8:  # 发射子弹的概率是1到20的随机数中取到8的概率，即20分之一
            bullet = EnemyBullet(self.screen, self.x, self.y)
            self.bullets.append(bullet)


# 子弹类
# 属性
class Bullet(object):#玩家子弹类
    def __init__(self, screen, x, y):
        # 坐标
        self.x = x + 80 / 2 - 45 / 2
        self.y = y - 44
        # 图片
        self.image = pygame.image.load('./plane/bullet.png')
        # 窗口
        self.screen = screen
        # 子弹速度
        self.speed = 4

    def display(self):
        """显示子弹到窗口"""
        self.screen.blit(self.image, (self.x, self.y))

    def auto_move(self):
        """让子弹飞 修改子弹y坐标"""
        self.y -= self.speed


# 敌方子弹类
# 属性
class EnemyBullet(object):#敌机子弹类
    def __init__(self, screen, x, y):
        # 坐标
        self.x = x + 56 / 2 - 32 / 2  # 不支持小数，尽量改成可整除
        self.y = y + 60
        # 图片
        self.image = pygame.image.load('./plane/bullet1.png')  # 32×60
        # 窗口
        self.screen = screen
        # 子弹速度
        self.speed = 4

    def display(self):
        """显示子弹到窗口"""
        self.screen.blit(self.image, (self.x, self.y))

    def auto_move(self):
        """让子弹飞 修改子弹y坐标"""
        self.y += self.speed


class GameSound(object):
    def __init__(self):#这里下短横线是2个，不是1个，1个会报错，当时到处搜索解决方法，有人说是没有插耳机，我还去插耳机了也没用...
        pygame.init()
        pygame.mixer.init()  # 音乐模块初始化
        pygame.mixer.music.load('.\plane\communication.wav')
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.5)  # 声音大小

    def playBackgroundMusic(self):
        pygame.init()
        pygame.mixer.init()  # 音乐模块初始化
        pygame.mixer.music.play(-1)  # 开始播放音乐


def main():
    """完成整个程序的控制"""
    sound = GameSound()
    sound.playBackgroundMusic()
    # 1 创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((299, 582), 0, 24)
    # 2 创建一个窗口大小的图片，当做背景
    background = pygame.image.load("./plane/background.png")
    # 创建一个玩家飞机的对象，注意不要忘记传窗口
    player = HeroPlane(screen)
    # 创建一个敌方飞机的对象，注意不要忘记传窗口
    enemyplane = EnemyPlane(screen)
    # 设定需要显示的背景图
    while True:
        # 3 将背景图片贴到窗口中
        screen.blit(background, (0, 0))
        # 获取事件
        for event in pygame.event.get():
            # 判断事件类型，如果是pygame就退出
            if event.type == QUIT:
                # 执行pygame退出
                pygame.quit()
                # python程序退出
                exit()
            elif event.type == pygame.KEYDOWN:
                # 检验，神奇的是这一段也不能被注释掉
                if event.key == K_a or event.key == K_LEFT:
                    print('左')
                elif event.key == K_d or event.key == K_RIGHT:
                    print('右')
                elif event.key == K_SPACE:
                    print('空格')
        # 执行飞机的按键监听
        player.key_control()  # 当时一片黑屏，找了一个小时的错，原来是代码没与for对齐，放到while true外面去了，当然就不会被执行了。
        # 飞机的显示
        player.display()
        # 敌方飞机的显示
        enemyplane.display()
        # 敌机自动移动
        enemyplane.auto_move()
        # 敌机自动开火
        enemyplane.auto_fire()
        # 更新显示内容
        pygame.display.update()
        time.sleep(0.01)


if __name__ == '__main__':
    main()
