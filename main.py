# 1 - Import library
import pygame
from multiprocessing import Process

# 2 - Initialize the game and import graphics
pygame.init()
window = pygame.display.set_mode((1280, 720))

lowC = pygame.mixer.Sound("audio/1.wav")
lowD = pygame.mixer.Sound("audio/2.wav")
E = pygame.mixer.Sound("audio/3.wav")
F = pygame.mixer.Sound("audio/4.wav")
G = pygame.mixer.Sound("audio/5.wav")
A = pygame.mixer.Sound("audio/6.wav")
B = pygame.mixer.Sound("audio/7.wav")
highC = pygame.mixer.Sound("audio/8.wav")
highD = pygame.mixer.Sound("audio/9.wav")
Special = pygame.mixer.Sound("audio/0.wav")

# Import graphics
radiyubase = pygame.image.load("images/base/0.png")
radiyulowC = [pygame.image.load("images/1/0.png"), pygame.image.load("images/1/1.png"),
              pygame.image.load("images/1/2.png")]
radiyulowD = [pygame.image.load("images/2/0.png"), pygame.image.load("images/2/1.png"),
              pygame.image.load("images/2/2.png")]
radiyuE = [pygame.image.load("images/3/0.png"), pygame.image.load("images/3/1.png"),
           pygame.image.load("images/3/2.png")]
radiyuF = [pygame.image.load("images/4/0.png"), pygame.image.load("images/4/1.png")]
radiyuG = [pygame.image.load("images/5/0.png"), pygame.image.load("images/5/1.png")]
radiyuA = [pygame.image.load("images/6/0.png"), pygame.image.load("images/6/1.png"),
           pygame.image.load("images/6/2.png")]
radiyuB = [pygame.image.load("images/7/0.png"), pygame.image.load("images/7/1.png")]
radiyuhighC = [pygame.image.load("images/8/0.png"), pygame.image.load("images/8/1.png"),
               pygame.image.load("images/8/2.png")]
radiyuhighD = [pygame.image.load("images/9/0.png")]
# radiyuSpecial = #gif_link
window.blit(radiyubase, (0, 0))


# 3 define functions for each note
def playA():
    window.blit(radiyuA[1], (0, 0))
    pygame.mixer.Sound.play(A, loops=-1)
    window.blit(radiyuA[2], (0, 0))


def playB():
    window.blit(radiyuB[0], (0, 0))
    pygame.mixer.Sound.play(B, loops=-1)
    window.blit(radiyuB[1], (0, 0))


def playlowC():
    window.blit(radiyulowC[1], (0, 0))
    pygame.mixer.Sound.play(lowC, loops=-1)
    window.blit(radiyulowC[2], (0, 0))


def playlowD():
    window.blit(radiyulowD[1], (0, 0))
    pygame.mixer.Sound.play(lowD, loops=-1)
    window.blit(radiyulowD[2], (0, 0))


def playE():
    window.blit(radiyuE[1], (0, 0))
    pygame.mixer.Sound.play(E, loops=-1)
    window.blit(radiyuE[2], (0, 0))


def playF():
    window.blit(radiyuF[0], (0, 0))
    pygame.mixer.Sound.play(F, loops=-1)
    window.blit(radiyuF[1], (0, 0))


def playG():
    window.blit(radiyuG[0], (0, 0))
    pygame.mixer.Sound.play(G, loops=-1)
    window.blit(radiyuG[1], (0, 0))


def playhighC():
    window.blit(radiyuhighC[1], (0, 0))
    pygame.mixer.Sound.play(highC, loops=-1)
    window.blit(radiyuhighC[2], (0, 0))


def playhighD():
    window.blit(radiyuhighD[0], (0, 0))
    pygame.mixer.Sound.play(highD, loops=-1)


def playSpecial():
    pygame.mixer.Sound.play(Special, loops=-1)


# 4 always loop
if __name__ == "__main__":
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_1]:
                    playlowC()
                if keys[pygame.K_2]:
                    playlowD()
                if keys[pygame.K_3]:
                    playE()
                if keys[pygame.K_4]:
                    playF()
                if keys[pygame.K_5]:
                    playG()
                if keys[pygame.K_6]:
                    playA()
                if keys[pygame.K_7]:
                    playB()
                if keys[pygame.K_8]:
                    playhighC()
                if keys[pygame.K_9]:
                    playhighD()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_1:
                    window.blit(radiyulowC[2], (0, 0))
                    pygame.mixer.Sound.stop(lowC)
                    window.blit(radiyubase, (0, 0))
                if event.key == pygame.K_2:
                    window.blit(radiyulowD[2], (0, 0))
                    pygame.mixer.Sound.stop(lowD)
                    window.blit(radiyubase, (0, 0))
                if event.key == pygame.K_3:
                    window.blit(radiyuE[2], (0, 0))
                    pygame.mixer.Sound.stop(E)
                    window.blit(radiyubase, (0, 0))
                if event.key == pygame.K_4:
                    window.blit(radiyuF[0], (0, 0))
                    pygame.mixer.Sound.stop(F)
                    window.blit(radiyubase, (0, 0))
                if event.key == pygame.K_5:
                    window.blit(radiyuG[0], (0, 0))
                    pygame.mixer.Sound.stop(G)
                    window.blit(radiyubase, (0, 0))
                if event.key == pygame.K_6:
                    window.blit(radiyuA[2], (0, 0))
                    pygame.mixer.Sound.stop(A)
                    window.blit(radiyubase, (0, 0))
                if event.key == pygame.K_7:
                    window.blit(radiyuB[0], (0, 0))
                    pygame.mixer.Sound.stop(B)
                    window.blit(radiyubase, (0, 0))
                if event.key == pygame.K_8:
                    window.blit(radiyuhighC[2], (0, 0))
                    pygame.mixer.Sound.stop(highC)
                    window.blit(radiyubase, (0, 0))
                if event.key == pygame.K_9:
                    pygame.mixer.Sound.stop(highD)
                    window.blit(radiyubase, (0, 0))
        pygame.display.update()
