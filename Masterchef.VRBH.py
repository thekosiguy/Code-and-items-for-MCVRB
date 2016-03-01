import pygame, sys, pygame.mixer, pygame as pg, pygbutton 
from pygame.locals import *

#initalise pygame
pygame.init()

#Globally Initalise the screen 
screen = pygame.display.set_mode((800,600),0,32)
backgroundcolour = (255, 255, 255)
pygame.display.set_caption("MASTERCHEF VRBH")

#initialise colours
black = (0, 0, 0)
white = (255, 255, 255)

#Import Images
background = pygame.image.load("backgroundimage.jpg") 
firstimage = pygame.image.load("firstimage.jpg")
firstimage = pygame.transform.scale(firstimage, (300,300))
secondimage = pygame.image.load("secondimage.jpg")
secondimage = pygame.transform.scale(secondimage, (300,300))


def mainMenu():
   #initialise the cursor
    pygame.mouse.set_visible(True)

    #Generate font objects as well as initialise and display text
    font = pg.font.SysFont("Calibri", 100, bold = True)
    newfont = pg.font.SysFont("Calibri", 45, bold = True) 
    header = font.render("MASTERCHEF VRBH", 1, black)
    text = font.render("BARGAIN HUNT", 1, black)
    groupnames = newfont.render("BY MAX, MICHAEL, NKOSILATHI, NAMAR AND ISAAC", 1, black)

    #Generate buttons
    play = pygbutton.PygButton((350, 300, 100, 30), "PLAY") 
    exitgame = pygbutton.PygButton((350, 370, 100, 30), "EXIT")
    
    #Responds to events such as pressing the escape key 
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_q:
                    sys.exit()
            if 'click' in exitgame.handleEvent(event):
                pygame.quit()
                sys.exit()
            #if 'click' in play.handleEvent(event):
                #do something once the user clicks play 
                    
        #display stuff on the screen and update it
        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, white, (60, 50, 690, 55)) #Generate a rectangle and display it on the screen
        pygame.draw.rect(screen, white, (130, 120, 530, 55))
        pygame.draw.rect(screen, white, (15, 530, 775, 35))
        screen.blit(header, (60, 40))
        screen.blit(text, (130, 110))
        screen.blit(firstimage, (5,200))
        screen.blit(secondimage, (495,200))
        screen.blit(groupnames, (15, 530))
        play.draw(screen)
        exitgame.draw(screen)
        pygame.display.update()

mainMenu()
            
    
