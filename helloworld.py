
import pygame
pygame.init()
w=pygame.display.set_mode((440,440))
start=False
while start==False:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            start=True
            running=False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            x,y=pygame.mouse.get_pos()
            if x>20 and x<410 and y>120 and y<270:
                start=True
    w.fill((140,140,140))
    recta=pygame.Rect(20,120,390,150)
    pygame.draw.rect(w,(20,150,20),recta)
    pygame.draw.line(w,(255,255,255),(40,140),(112,140),4)
    pygame.draw.line(w,(255,255,255),(40,140),(40,200),4)
    pygame.draw.line(w,(255,255,255),(40,200),(112,200),4)
    pygame.draw.line(w,(255,255,255),(112,200),(112,260),4)
    pygame.draw.line(w,(255,255,255),(112,260),(40,260),4)
    
    pygame.draw.line(w,(255,255,255),(130,140),(184,140),4)
    pygame.draw.line(w,(255,255,255),(157,140),(157,260),4)
    
    pygame.draw.line(w,(255,255,255),(184,260),(220,140),4)
    pygame.draw.line(w,(255,255,255),(220,140),(256,260),4)
    pygame.draw.line(w,(255,255,255),(202,200),(238,200),4)
    
    pygame.draw.line(w,(255,255,255),(270,140),(270,260),4)
    pygame.draw.line(w,(255,255,255),(270,140),(320,140),4)
    pygame.draw.line(w,(255,255,255),(320,140),(320,180),4)
    pygame.draw.line(w,(255,255,255),(320,180),(270,180),4)
    pygame.draw.line(w,(255,255,255),(270,180),(320,260),4)
    
    pygame.draw.line(w,(255,255,255),(346,140),(400,140),4)
    pygame.draw.line(w,(255,255,255),(372,140),(372,260),4)
    
    pygame.display.flip()
