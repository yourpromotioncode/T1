#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
# -*- coding: utf-8 -*-

import pygame
import random
# 1 게임 초기화
pygame.init()

#2 게임창 옵션 설정
size = [400,600]
screen = pygame.display.set_mode(size)

title = "Wings"
pygame.display.set_caption(title)

#3 게임 내 필요한 설정
clock = pygame.time.Clock()

class obj:
    def __init__(self):
        self.x=0
        self.y=0
        self.move=0
    def put_img(self,address):
        if address [-3:]=="png":
            self.img = pygame.image.load(address).convert_alpha()
        else:
            self.img = pygame.image.load(address)
        self.img_x,self.img_y = self.img.get_size()
    def chsize(self,img_x,img_y):
        self.img = pygame.transform.scale(self.img,(img_x,img_y))
        self.img_x,self.img_y = self.img.get_size()
    def show(self):
        screen.blit(self.img, (self.x,self.y))

imge=obj()
imge.put_img("/Applications/DEV/images/ima2.png")
imge.chsize(35,55)
imge.x = round(size[0]/2-imge.img_x/2) #round : 반올림
imge.y = round(size[1]-imge.img_y-15)
imge.move=10

left_move=False
right_move=False
up_move=False
down_move=False
shoot=False

bg=(0,0,0)
white = (255,255,255)
k=0

#4 메인 이벤트
laser_list=[]
enemy_list=[]
SB = 0
while SB==0:

    #4-1 FPS 설정
    clock.tick(60)
    #4-2 각종 입력 감지
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            SB=1
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                left_move=True
            elif event.key==pygame.K_RIGHT:
                right_move=True
            elif event.key==pygame.K_UP:
                up_move=True
            elif event.key==pygame.K_DOWN:
                down_move=True
            elif event.key==pygame.K_SPACE:
                shoot=True
                k=0
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                left_move=False
            elif event.key==pygame.K_RIGHT:
                right_move=False
            elif event.key==pygame.K_UP:
                up_move=False
            elif event.key==pygame.K_DOWN:
                down_move=False
            elif event.key==pygame.K_SPACE:
                shoot=False


    #4-3 입력,시간에 따른 변화
    if left_move==True:
        imge.x-=imge.move
        if imge.x<=0:
            imge.x=0
    elif right_move==True:
        imge.x+=imge.move
        if imge.x>=size[0]-imge.img_x:
            imge.x=size[0]-imge.img_x
    elif up_move==True:
        imge.y-=imge.move
        if imge.y<=0:
            imge.y=0
    elif down_move==True:
        imge.y+=imge.move
        if imge.y>=size[1]-imge.img_y-15:
            imge.y=size[1]-imge.img_y-15
    elif left_move and up_move==True:
        imge.x-=imge.move
        imge.y-=imge.move
        if imge.x<=0:
            imge.x=0

        if imge.y<=0:
            imge.y=0
    elif left_move and down_move==True:
        imge.x-=imge.move
        imge.y+=imge.move
        if imge.x<=0:
            imge.x=0

        if imge.y>=size[1]-imge.img_y-15:
            imge.y=size[1]-imge.img_y-15
    elif right_move and up_move==True:
        imge.x+=imge.move
        imge.y-=imge.move
        if imge.x>=size[0]-imge.img_x:
            imge.x=size[0]-imge.img_x

        if imge.y<=0:
            imge.y=0
    elif right_move and down_move == True:
        imge.x+=imge.move
        imge.y+=imge.move
        if imge.x>=size[0]-imge.img_x:
            imge.x=size[0]-imge.img_x

        if imge.y>=size[1]-imge.img_y-15:
            imge.y=size[1]-imge.img_y-15


    if shoot==True and k%6==0:
        laser=obj()
        laser.put_img("/Applications/DEV/images/laser.png")
        laser.chsize(35,50)
        laser.x = round(imge.x + imge.img_x/2 - laser.img_x/2)
        laser.y = imge.y - 10
        laser.move=30
        laser_list.append(laser)
    k += 1
    d_list=[]
    for ls in range(len(laser_list)):
        l=laser_list[ls]
        l.y -= l.move
        if l.y<= -l.img_y:
            d_list.append(ls)
    for d in d_list:
        del laser_list[d]

    if random.random() > 0.97:
        enemy=obj()
        enemy.put_img("/Applications/DEV/images/enemy.png")
        enemy.chsize(50,50)
        enemy.x = random.randrange(0,size[0]-enemy.img_x-round(imge.img_x/2))
        enemy.y = -5
        enemy.move=2
        enemy_list.append(enemy)
    d_list=[]
    for en in range(len(enemy_list)):
        e=enemy_list[en]
        e.y += e.move
        if e.y>= size[1]:
            d_list.append(en)
    for d in d_list:
        del enemy_list[d]

    #4-4 그리기
    screen.fill(bg)
    imge.show()
    for l in laser_list:
        l.show()
    imge.show()
    for e in enemy_list:
        e.show()

    #4-5 화면 업데이트
    pygame.display.flip()
#5 게임 종료
pygame.quit()
