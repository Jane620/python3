import pygame
from pygame.locals import *
from sys import exit


background_image_filename= 'resource/sushiplate.jpg'
mouse_image_filename= 'resource/fugu.png'

pygame.init()
#定义窗体和显示标题
screen = pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption("Hello World")

#载入图片
background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    #画背景
    screen.blit(background,(0,0))
    
    x,y = pygame.mouse.get_pos()

    #鼠标位置置中
    x -= mouse_cursor.get_width()
    y -= mouse_cursor.get_height()

    screen.blit(mouse_cursor,(x,y))
    pygame.display.update()






