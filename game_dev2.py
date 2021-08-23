#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
# -*- coding: utf-8 -*-

import pygame
import random
import time
from datetime import datetime


# 1 게임 초기화
pygame.init()

#2 게임창 옵션 설정
size = [500,700]
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

# a.x-b.sx <= b.x <= a.x+a.sx
# a.y-b.sy <= b.y <= a.y+a.sy

def crash(a,b):
    if (a.x-b.img_x <= b.x) and (b.x <= a.x+a.img_x):
        if (a.y-b.img_y <= b.y) and (b.y <= a.y+a.img_y):
            return True
        else:
            return False
    else:
        return False


imge=obj()
imge.put_img("/Applications/DEV/images/ima2.png")
imge.chsize(35,55)
imge.x = round(size[0]/2-imge.img_x/2) #round : 반올림
imge.y = round(size[1]-imge.img_y-15)
imge.move=10


shoot=False

bg=(0,0,0)
white = (255,255,255)
k=0

kill = 0
miss = 0
comm_time=datetime.now()

#4-0 메인 화면
SB=0
while SB==0:
    clock.tick(60)
    for event in pygame.event.get():
    #     if event.type==pygame.KEYDOWN:
    #         if event.key==pygame.K_q:
    #             SB=2
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                SB=1
    screen.fill(bg)
    font = pygame.font.Font("/library/fonts/Chalkduster.ttf",20)
    text = font.render("PRESS ENTER TO START".format(kill,miss),True,(255,255,255))
    screen.blit(text,(100,round(size[1]/2-50)))
    pygame.display.flip()

# if SB==2:
    # pygame.quit()
#4 메인 이벤트
laser_list=[]
enemy_list=[]
to_x=0
to_y=0
SB = 0

while SB==0:

    #4-1 FPS 설정
    clock.tick(60)

    #4-2 각종 입력 감지
    for event in pygame.event.get():
        shoot=True
        if event.type==pygame.QUIT:
            SB=1
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                to_x -= 6
            elif event.key==pygame.K_RIGHT:
                to_x += 6
            elif event.key==pygame.K_UP:
                to_y -= 6
            elif event.key==pygame.K_DOWN:
                to_y += 6
            # elif event.key==pygame.K_SPACE:
                # shoot=True
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                to_x = 0
            elif event.key==pygame.K_RIGHT:
                to_x = 0
            elif event.key==pygame.K_UP:
                to_y = 0
            elif event.key==pygame.K_DOWN:
                to_y = 0
            # elif event.key==pygame.K_SPACE:
                # shoot=False
    imge.x += to_x
    imge.y += to_y


    #4-3 입력,시간에 따른 변화
    presnt_time=datetime.now()
    delta_time=(presnt_time-comm_time).total_seconds()
    #delta_time=round(presnt_time-comm_time).total_seconds()

    if imge.x<=0:
            imge.x=0
    if imge.x>=size[0]-imge.img_x:
            imge.x=size[0]-imge.img_x
    if imge.y<=0:
            imge.y=0
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
        miss += 1

    dci_list=[]
    dji_list=[]
    for i in range(len(laser_list)):
        for j in range(len(enemy_list)):
            l = laser_list[i]
            e = enemy_list[j]
            if crash(l,e) == True:
                dci_list.append(i)
                dji_list.append(j)

    dci_list = list(set(dci_list))
    dji_list = list(set(dji_list))
    dci_list.reverse()
    dji_list.reverse()
    for dci in dci_list:
        del laser_list[dci]
    for dji in dji_list:
        del enemy_list[dji]
        kill += 1

    for i in range(len(enemy_list)):
        a = enemy_list[i]
        if crash(a,imge) == True:
            SB=1
            GO=1


    #4-4 그리기
    screen.fill(bg)
    imge.show()
    for l in laser_list:
        l.show()
    imge.show()
    for e in enemy_list:
        e.show()
    font = pygame.font.Font("/library/fonts/Chalkduster.ttf",15)
    text_battle = font.render("Killed : {}    Missed : {}".format(kill,miss),True,(255,255,255))
    screen.blit(text_battle,(10,5))
    text_time = font.render("{}".format(delta_time),True,(255,255,90))
    screen.blit(text_time,(size[0]/2,5))



    #4-5 화면 업데이트
    pygame.display.flip()
#5 게임 종료
while GO==1:
    clock.tick(60)
    for event in pygame.event.get():
    #     if event.type==pygame.KEYDOWN:
    #         if event.key==pygame.K_q:
    #             SB=2
        if event.type==pygame.QUIT:
            GO=0
    font = pygame.font.Font("/library/fonts/Chalkduster.ttf",25)
    text = font.render("MISSION FAILED".format(kill,miss),True,(255,0,0))
    screen.blit(text,(150,round(size[1]/2-50)))
    pygame.display.flip()

pygame.quit()
