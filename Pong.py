#Importuje framework Pygame:
import pygame, sys
#skraca pygame.locals do pygame (można by np dodać jeszcze "as pl", 
# ale "l" za bardzo myli mi się z "I" i "1" xD):
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

#rozmiar okna:
screen_width = 1280
screen_height = 630
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

#deklaracja ramek dla obiektów (hitboxy):
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
paddle1 = pygame.Rect(screen_width - 20, screen_height/2 - 60, 10, 120)
paddle2 = pygame.Rect(10, screen_height/2 - 60, 10, 120)

#kolorki:
background_color = (235, 211, 234) #tło
objects_color = (64, 6, 62) #piłka i paletki

#prędkość
ball_speed_x = 7
ball_speed_y = 7

while True:
    #zamykanie okna:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    #ruch piłki:
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1 #zmiana kierunku piłki po uderzeniu w górną lub dolną krawędź
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1 #zmiana kierunku piłki po uderzeniu w lewą lub prawą krawędź
            
    #obrazy dla obiektów:
    screen.fill(background_color) #tło
    pygame.draw.rect(screen, objects_color, paddle1) #paletka 1
    pygame.draw.rect(screen, objects_color, paddle2) #paletka 2
    pygame.draw.ellipse(screen, objects_color, ball) #piłka  
    pygame.draw.aaline(screen, objects_color, (screen_width/2, 0), (screen_width/2, screen_height)) #linia środkowa      
    #update okna:        
    pygame.display.flip() 
    clock.tick(60)
 