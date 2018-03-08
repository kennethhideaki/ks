import random
import pygame
pygame.init()

w=pygame.display.set_mode((440,440))
w.fill((0,0,0,))
#grid
block=pygame.Rect(0,0,40,40)
for i in range(12):
    pygame.draw.line(w,(255,255,255),(i*40,0),(i*40,400))
for i in range(12):
    pygame.draw.line(w,(255,255,255),(0,i*40),(400,i*40))
for i in range(12):
    if i!=0 and i%2==1 and i!=11:
        block=pygame.Rect(i*40,i*40,40,40)
        pygame.draw.rect(w,(0,0,255),block)
enemy=pygame.Rect(0,0,40,40)
main=pygame.Rect(400,400,40,40)
bomb=pygame.Rect(0,0,40,40)
bomb2=pygame.Rect(360,360,40,40)
running=True
timer=3
timer2=3
c=pygame.time.Clock()
purple_timer = 300
purple_timer2 = 300
blow=False
blow2=False
placed=False
placed2=False
wallx=False
wally=False
wallx2=False
wally2=False
color=(0,255,0)
color2 = (0,255,0)
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                if main.x<400 and main.y%80==0:
                    main.x+=40
            if pygame.key.get_pressed()[pygame.K_LEFT]:
                if main.x>0 and main.y%80==0:
                    main.x-=40
            if pygame.key.get_pressed()[pygame.K_UP]:
                if main.y>0 and main.x%80==0:
                    main.y-=40
            if pygame.key.get_pressed()[pygame.K_DOWN]:
                if main.y<400 and main.x%80==0:
                    main.y+=40
            if pygame.key.get_pressed()[pygame.K_RSHIFT]:
                if placed==False:
                    bomb.x=main.x
                    bomb.y=main.y
                    placed=True
                    print(bomb.x)
            
            if pygame.key.get_pressed()[pygame.K_d]:
                if enemy.x<400 and enemy.y%80==0:
                    enemy.x+=40
            if pygame.key.get_pressed()[pygame.K_a]:
                if enemy.x>0 and enemy.y%80==0:
                    enemy.x-=40
            if pygame.key.get_pressed()[pygame.K_w]:
                if enemy.y>0 and enemy.x%80==0:
                    enemy.y-=40
            if pygame.key.get_pressed()[pygame.K_s]:
                if enemy.y<400 and enemy.x%80==0:
                    enemy.y+=40
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                if placed2==False:
                    bomb2.x=enemy.x
                    bomb2.y=enemy.y
                    placed2=True
                    print(bomb2.x)
            
                    
                
            
    w.fill((200,200,200))
    for i in range(12):
        pygame.draw.line(w,(10,10,10),(i*40,0),(i*40,440))
    for i in range(12):
        pygame.draw.line(w,(10,10,10),(0,i*40),(440,i*40))
    
    for i in range(11):
        for x in range(11):
            if i!=0 and i%2==1 and i!=10:
                if x!=0 and x%2==1 and x!=10:
                    block=pygame.Rect(i*40,x*40,40,40)
                    pygame.draw.rect(w,(0,0,255),block)
    
    if placed:
        purple_timer -= c.get_time()
        print(purple_timer)
        if purple_timer<=0:
            if timer==3:
                color=(0,255,0)
                timer-=1
            elif timer==2:
                color=(255,255,0)
                timer-=1
            elif timer==1:
                color=(255,0,0)
                timer-=1
            elif timer==0:
                if bomb.x%80!=0:
                    
                    
                    ex=pygame.Rect(0,bomb.y,440,40)
                    ey=pygame.Rect(bomb.x,bomb.y,40,40)
                    wallx=True
                    
                elif bomb.y%80!=0:
                    ex=pygame.Rect(bomb.x,bomb.y,40,40)
                    ey=pygame.Rect(bomb.x,0,40,440)
                else:
                    ex=pygame.Rect(0,bomb.y,440,40)
                    ey=pygame.Rect(bomb.x,0,40,440)
                blow=True
                timer-=1
            elif timer==-1:
                blow=False
                placed=False
                timer=3
                color=(0,255,0)
            purple_timer=300
            
    if placed2:
        purple_timer2 -= c.get_time()
        print(purple_timer2)
        if purple_timer2<=0:
            if timer2==3:
                color2=(0,255,0)
                timer2-=1
            elif timer2==2:
                color2=(255,255,0)
                timer2-=1
            elif timer2==1:
                color2=(255,0,0)
                timer2-=1
            elif timer2==0:
                if bomb2.x%80!=0:
                    
                    
                    ex2=pygame.Rect(0,bomb2.y,440,40)
                    ey2=pygame.Rect(bomb2.x,bomb2.y,40,40)
                    wallx2=True
                    
                elif bomb2.y%80!=0:
                    ex2=pygame.Rect(bomb2.x,bomb2.y,40,40)
                    ey2=pygame.Rect(bomb2.x,0,40,440)
                else:
                    ex2=pygame.Rect(0,bomb2.y,440,40)
                    ey2=pygame.Rect(bomb2.x,0,40,440)
                    
                blow2=True
                timer2-=1
            elif timer2==-1:
                blow2=False
                placed2=False
                timer2=3
                color2=(0,255,0)
            purple_timer2=300
        
    pygame.draw.rect(w,(0,0,0),main)
    pygame.draw.rect(w,(255,255,255),enemy)
    if placed:
        pygame.draw.ellipse(w,color,bomb)
    if placed2:
        pygame.draw.ellipse(w,color2,bomb2)
    if blow:
        pygame.draw.rect(w,(255,0,0),ex)
        pygame.draw.rect(w,(255,0,0),ey)
        
        if enemy.x==bomb.x and bomb.x%80==0:
            
            running=False
            print("P2 wins")
        if enemy.y==bomb.y and bomb.y%80==0:
            running=False
            print("P2 wins")
        if main.x==bomb.x and bomb.x%80==0:
            
            running=False
            print("P1 wins")
        if main.y==bomb.y and bomb.y%80==0:
            running=False
            print("P1 wins")
    if blow2:
        pygame.draw.rect(w,(255,0,0),ex2)
        pygame.draw.rect(w,(255,0,0),ey2)
        
        if enemy.x==bomb2.x and bomb2.x%80==0:
            
            running=False
            print("P2 wins")
        if enemy.y==bomb2.y and bomb2.y%80==0:
            running=False
            print("P2 wins")
        if main.x==bomb2.x and bomb2.x%80==0:
            
            running=False
            print("P1 wins")
        if main.y==bomb2.y and bomb2.y%80==0:
            running=False
            print("P1 wins")
    
    pygame.display.flip()
    c.tick(30)

