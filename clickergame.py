import pygame
import random
import time


pygame.init()

width=1000
length=600
screen=pygame.display.set_mode((width,length))
pygame.display.set_caption("Whack_a_Mole")

bg=pygame.image.load("whackamole.jpg")


def bgmusic():
    a=pygame.mixer.Sound("D:\downloads\pinball.mp3")
    a.play(-1)
def clickmole():
    a=pygame.mixer.Sound("D:\downloads\coin.mp3")
    a.play()
    a.set_volume(0.5)
# def gameend():
#     a=pygame.mixer.Sound()
#     a.play()

timer=5

x=True
y=True
z=True

clicks=0
CRx=random.randint(50,950)
CRy=random.randint(50,550)

Color1=random.randint(0,255)
Color2=random.randint(0,255)
Color3=random.randint(0,255)

bgmusic()

hammer=pygame.mouse.get_pos()

hx=hammer[0]
hy=hammer[1]
while x:
    for event in pygame.event.get():

        #screen.fill((0,0,0))

        #clock=pygame.time.Clock()

        if z==True:

            screen.blit(bg,(0,0))

            pygame.mouse.set_visible(False)

            hammer=pygame.mouse.get_pos()
            hx=hammer[0]
            hy=hammer[1]

            #screen.blit(pygame.image.load("D:\desktop\hammer.png"),(hx-14,hy-10))


            clickstr=pygame.Rect((CRx,CRy,50,50))
            clickbound=pygame.Rect((CRx-1,CRy-1,31,31))

            #pygame.draw.rect(screen,(Color1,Color2,Color3),clickstr)
            screen.blit(pygame.image.load("D:\desktop\mole.png"),clickstr)
            #pygame.draw.rect(screen,(0,0,0),clickbound,width=1)

            screen.blit(pygame.image.load("D:\desktop\hammer.png"),(hx-14,hy-10))


        if event.type==pygame.QUIT:
            x=False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if y==True:
                pygame.time.set_timer(pygame.K_BACKSPACE,timer*1000)
                y=False
            elif clickstr.collidepoint(hammer):
                print("Click Made")
                clickmole()
                clicks+=1
                CRx=random.randint(50,950)
                CRy=random.randint(50,550)
                Color1=random.randint(0,255)
                Color2=random.randint(0,255)
                Color3=random.randint(0,255)
        elif event.type==pygame.K_BACKSPACE:
            pygame.display.flip()
            screen.blit(pygame.image.load("D:\desktop\gameover.jpg"),(0,0))
            endtext="Score =" + str(clicks)
            font=pygame.font.SysFont("Arial",40)
            score=font.render(endtext,True,(0,0,0))
            screen.blit(score,(450,200))
            playagain=pygame.Rect((429,328,164,174))
            screen.blit(pygame.image.load("D:\desktop\greplay.jpg"),playagain)
            hammer=pygame.mouse.get_pos()
            hx=hammer[0]
            hy=hammer[1]
            screen.blit(pygame.image.load("D:\desktop\hammer.png"),(hx-14,hy-10))


            pygame.display.flip()
        
            if playagain.collidepoint(hammer):
                z=True
            else:
                z=False
            

    
    pygame.display.flip()

print("SCORE: ",clicks)


        
pygame.quit()