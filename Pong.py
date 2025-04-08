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
paddle_right = pygame.Rect(screen_width - 20, screen_height/2 - 60, 10, 120)
paddle_left = pygame.Rect(10, screen_height/2 - 60, 10, 120)

#kolorki:
background_color = (235, 211, 234) #tło
objects_color = (64, 6, 62) #piłka i paletki

#prędkość
ball_speed_x = 7
ball_speed_y = 7
paddle_right_speed = 0
paddle_left_speed = 0



def ball_movement():
    global ball_speed_x, ball_speed_y 
    #dałam, to do funkcji, żeby sie nie pogubić w loopie, zamiast returna użyłam global bo, 
    #nie będie dużo tych funkcji
 
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1 #zmiana kierunku piłki po uderzeniu w górną lub dolną krawędź
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1 #zmiana kierunku piłki po uderzeniu w lewą lub prawą krawędź
    if ball.colliderect(paddle_right) or ball.colliderect(paddle_left):
        ball_speed_x *= -1 
        
def paddle_right_movement():
    #tutaj nie edutujemy zmiennej wewnątrz funkcji, tylko zmieniamy jej wartość w pętli głównej, więc nie używamy global
    paddle_right.y += paddle_right_speed
    if paddle_right.top <= 0:
        paddle_right.top = 0
    if paddle_right.bottom >= screen_height:
        paddle_right.bottom = screen_height
        
def paddle_left_movement():
    #tutaj nie edutujemy zmiennej wewnątrz funkcji, tylko zmieniamy jej wartość w pętli głównej, więc nie używamy global
    paddle_left.y += paddle_left_speed
    if paddle_left.top <= 0:
        paddle_left.top = 0
    if paddle_left.bottom >= screen_height:
        paddle_left.bottom = screen_height
        
while True:
    #zamykanie okna:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    #ruch paletki prawej:
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                paddle_right_speed += 7
            if event.key == K_UP:
                paddle_right_speed -= 7
        if event.type == KEYUP:
            if event.key == K_UP:
                paddle_right_speed += 7
            if event.key == K_DOWN:
                paddle_right_speed -= 7
    #ruch paletki lewej:
        if event.type == KEYDOWN:
            if event.key == K_s:
                paddle_left_speed += 7
            if event.key == K_w:
                paddle_left_speed -= 7
        if event.type == KEYUP:
            if event.key == K_w:
                paddle_left_speed += 7
            if event.key == K_s:
                paddle_left_speed -= 7
                
                
    ball_movement() #ruch piłki
    paddle_right_movement() #ruch paletki prawej
    paddle_left_movement() #ruch paletki lewej           
            
    #obrazy dla obiektów:
    screen.fill(background_color) #tło
    pygame.draw.rect(screen, objects_color, paddle_right) #paletka prawa
    pygame.draw.rect(screen, objects_color, paddle_left) #paletka lewa
    pygame.draw.ellipse(screen, objects_color, ball) #piłka  
    pygame.draw.aaline(screen, objects_color, (screen_width/2, 0), (screen_width/2, screen_height)) #linia środkowa      
    #update okna:        
    pygame.display.flip() 
    clock.tick(60)
 