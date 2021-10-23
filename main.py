# 1 - Import library
import pygame
from pygame.locals import *
from multiprocessing import Process

# 2 - Initialize the game and import graphics
pygame.init()
window = pygame.display.set_mode((600, 600))

A = pygame.mixer.sound.load("audio/a.wav")
B = pygame.mixer.sound.load("audio/b.wav")
C = pygame.mixer.sound.load("audio/c.wav")
D = pygame.mixer.sound.load("audio/d.wav")
E = pygame.mixer.sound.load("audio/e.wav")
F = pygame.mixer.sound.load("audio/f.wav")
G = pygame.mixer.sound.load("audio/g.wav")

#Import graphics
radiyuA = [pygame.image.load("images/a1.png"), pygame.image.load("images/a2.png"), pygame.image.load("images/a3.png")]
radiyuB = [pygame.image.load("images/b1.png"), pygame.image.load("images/b2.png"), pygame.image.load("images/b3.png")]
radiyuC = [pygame.image.load("images/c1.png"), pygame.image.load("images/c2.png"), pygame.image.load("images/c3.png")]
radiyuD = [pygame.image.load("images/d1.png"), pygame.image.load("images/d2.png"), pygame.image.load("images/d3.png")]
radiyuE = [pygame.image.load("images/e1.png"), pygame.image.load("images/e2.png"), pygame.image.load("images/e3.png")]
radiyuF = [pygame.image.load("images/f1.png"), pygame.image.load("images/f2.png"), pygame.image.load("images/f3.png")]
radiyuG = [pygame.image.load("images/g1.png"), pygame.image.load("images/g2.png"), pygame.image.load("images/g3.png")]
window.blit(radiyuA[0], (x, y))
window.blit(radiyuB[0], (x, y))
window.blit(radiyuC[0], (x, y))
window.blit(radiyuD[0], (x, y))
window.blit(radiyuE[0], (x, y))
window.blit(radiyuF[0], (x, y))
window.blit(radiyuG[0], (x, y))

# 3 define functions for each note
def playA():
    window.blit(radiyuA[1], (x, y))
    pygame.mixer.sound.play(A, loops = -1)
    window.blit(radiyuA[2], (x, y))
def playB():
    window.blit(radiyuB[1], (x, y))
    pygame.mixer.sound.play(B, loops = -1)
    window.blit(radiyuB[2], (x, y))
def playC():
    window.blit(radiyuC[1], (x, y))
    pygame.mixer.sound.play(C, loops = -1)
    window.blit(radiyuC[2], (x, y))
def playD():
    window.blit(radiyuD[1], (x, y))
    pygame.mixer.sound.play(D, loops = -1)
    window.blit(radiyuD[2], (x, y))
def playE():
    window.blit(radiyuE[1], (x, y))
    pygame.mixer.sound.play(E, loops = -1)
    window.blit(radiyuE[2], (x, y))
def playF():
    window.blit(radiyuF[1], (x, y))
    pygame.mixer.sound.play(F, loops = -1)
    window.blit(radiyuF[2], (x, y))
def playG():
    window.blit(radiyuG[1], (x, y))
    pygame.mixer.sound.play(G, loops = -1)
    window.blit(radiyuG[2], (x, y))

# 4 always loop
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_1]:
                processes.append(Process(target = playC))
            if keys[pygame.K_2]:
                processes.append(Process(target = playD))
            if keys[pygame.K_3]:
                processes.append(Process(target = playE))
            if keys[pygame.K_4]:
                processes.append(Process(target = playF))
            if keys[pygame.K_5]:
                processes.append(Process(target = playG))
            if keys[pygame.K_6]:
                processes.append(Process(target = playA))
            if keys[pygame.K_7]:
                processes.append(Process(target = playB))

            for process in processes:
                process.start()
            for process in processes:
                process.join()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_1:
                window.blit(radiyuC[1], (x, y))
                pygame.mixer.sound.stop(C)
                window.blit(radiyuC[0], (x, y))
            if event.key == pygame.K_2:
                window.blit(radiyuD[1], (x, y))
                pygame.mixer.sound.stop(D)
                window.blit(radiyuD[0], (x, y))
            if event.key == pygame.K_3:
                window.blit(radiyuE[1], (x, y))
                pygame.mixer.sound.stop(E)
                window.blit(radiyuE[0], (x, y))
            if event.key == pygame.K_4:
                window.blit(radiyuF[1], (x, y))
                pygame.mixer.sound.stop(F)
                window.blit(radiyuF[0], (x, y))
            if event.key == pygame.K_5:
                window.blit(radiyuG[1], (x, y))
                pygame.mixer.sound.stop(G)
                window.blit(radiyuG[0], (x, y))
            if event.key == pygame.K_6:
                window.blit(radiyuA[1], (x, y))
                pygame.mixer.sound.stop(A)
                window.blit(radiyuA[0], (x, y))
            if event.key == pygame.K_7:
                window.blit(radiyuB[1], (x, y))
                pygame.mixer.sound.stop(B)
                window.blit(radiyuB[0], (x, y))

    pygame.display.update()


