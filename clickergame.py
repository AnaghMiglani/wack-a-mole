import pygame
import random

pygame.init()

width = 1000
length = 600
screen = pygame.display.set_mode((width, length))
pygame.display.set_caption("Whack_a_Mole")

bg = pygame.image.load("whackamole.jpg")

def bgmusic():
    a = pygame.mixer.Sound("D:\downloads\pinball.mp3")
    a.play(-1)

def clickmole():
    a = pygame.mixer.Sound("D:\downloads\coin.mp3")
    a.play()
    a.set_volume(0.5)

timer=int(input("Enter how many seconds should round last: "))
timer_duration = timer*1000
pygame.time.set_timer(pygame.USEREVENT, timer_duration)

running = True
game_active = True
clicks = 0
CRx = random.randint(50, 950)
CRy = random.randint(50, 550)

bgmusic()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_active:
            screen.blit(bg, (0, 0))
            pygame.mouse.set_visible(False)

            hammer = pygame.mouse.get_pos()
            hx, hy = hammer[0], hammer[1]

            clickstr = pygame.Rect((CRx, CRy, 50, 50))
            screen.blit(pygame.image.load("D:\desktop\mole.png"), clickstr)
            screen.blit(pygame.image.load("D:\desktop\hammer.png"), (hx - 14, hy - 10))

            if event.type == pygame.MOUSEBUTTONDOWN:
                if clickstr.collidepoint(hammer):
                    clickmole()
                    clicks += 1
                    CRx = random.randint(50, 950)
                    CRy = random.randint(50, 550)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                game_active = False

            if event.type == pygame.USEREVENT:
                game_active = False

        else:
            screen.blit(pygame.image.load("D:\desktop\gameover.jpg"), (0, 0))
            pygame.mouse.set_visible(True)
            endtext = "Score = " + str(clicks)
            font = pygame.font.SysFont("Arial", 40)
            score = font.render(endtext, True, (0, 0, 0))
            screen.blit(score, (450, 200))
            playagain = pygame.Rect((429, 328, 164, 174))
            screen.blit(pygame.image.load("D:\desktop\greplay.jpg"), playagain)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if playagain.collidepoint(pygame.mouse.get_pos()):
                    clicks = 0
                    CRx = random.randint(50, 950)
                    CRy = random.randint(50, 550)
                    game_active = True
                    pygame.time.set_timer(pygame.USEREVENT, timer_duration)

    pygame.display.flip()

print("SCORE: ", clicks)
pygame.quit()
