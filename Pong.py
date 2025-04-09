import pygame, sys
from pygame.locals import *

# Inicjalizacja Pygame
pygame.init()
clock = pygame.time.Clock()

# Ustawienia okna
screen_width = 1280
screen_height = 630
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# Obiekty gry
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
paddle_right = pygame.Rect(screen_width - 20, screen_height/2 - 60, 10, 120)
paddle_left = pygame.Rect(10, screen_height/2 - 60, 10, 120)

# Kolory
background_color = (235, 211, 234)
objects_color = (64, 6, 62)
text_color = (0, 0, 0)

# Prędkości
ball_speed_x = 7
ball_speed_y = 7
paddle_right_speed = 0
paddle_left_speed = 0

# Stan gry
game_active = False
game_over = False

# Wynik
score_left = 0
score_right = 0
max_score = 5

# Czcionki i teksty
font_large = pygame.font.Font(None, 74)
font_small = pygame.font.Font(None, 60)

start_text = font_large.render("Press SPACE to start", True, text_color)
start_rect = start_text.get_rect(center=(screen_width/2, screen_height/2))


def reset_ball():
    """Ustawia piłkę na środku i wyświetla odliczanie"""
    global ball_speed_x, ball_speed_y

    ball.center = (screen_width/2, screen_height/2)
    ball_speed_x *= -1
    ball_speed_y *= -1

    countdown()  # wywołujemy odliczanie przed wznowieniem gry



def ball_movement():
    """Obsługuje ruch piłki, odbicia i punktację"""
    global ball_speed_x, ball_speed_y, score_left, score_right, game_active, game_over

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Odbicia od góry i dołu
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    # Punkt dla prawego gracza
    if ball.left <= 0:
        score_right += 1
        check_winner()
        reset_ball()

    # Punkt dla lewego gracza
    if ball.right >= screen_width:
        score_left += 1
        check_winner()
        reset_ball()

    # Odbicia od paletek
    if ball.colliderect(paddle_right) or ball.colliderect(paddle_left):
        ball_speed_x *= -1


def paddle_right_movement():
    """Sterowanie paletką po prawej (strzałki)"""
    paddle_right.y += paddle_right_speed
    if paddle_right.top <= 0:
        paddle_right.top = 0
    if paddle_right.bottom >= screen_height:
        paddle_right.bottom = screen_height


def paddle_left_movement():
    """Sterowanie paletką po lewej (W/S)"""
    paddle_left.y += paddle_left_speed
    if paddle_left.top <= 0:
        paddle_left.top = 0
    if paddle_left.bottom >= screen_height:
        paddle_left.bottom = screen_height


def check_winner():
    """Sprawdza, czy ktoś wygrał"""
    global game_active, game_over
    if score_left >= max_score or score_right >= max_score:
        game_active = False
        game_over = True


def countdown():
    """Wyświetla odliczanie 3...2...1...GO!"""
    for i in range(3, 0, -1):
        draw_countdown(str(i))
        pygame.time.delay(1000)
    draw_countdown("GO!")
    pygame.time.delay(700)

def draw_countdown(text):
    """Pomocnicza funkcja do rysowania tekstu na środku"""
    screen.fill(background_color)
    pygame.draw.rect(screen, objects_color, paddle_right)
    pygame.draw.rect(screen, objects_color, paddle_left)
    pygame.draw.ellipse(screen, objects_color, ball)
    pygame.draw.aaline(screen, objects_color, (screen_width/2, 0), (screen_width/2, screen_height))

    score_text = font_small.render(f"{score_left} : {score_right}", True, text_color)
    score_rect = score_text.get_rect(center=(screen_width/2, 30))
    screen.blit(score_text, score_rect)

    countdown_font = pygame.font.Font(None, 100)
    countdown_surface = countdown_font.render(text, True, text_color)
    countdown_rect = countdown_surface.get_rect(center=(screen_width/2, screen_height/2))
    screen.blit(countdown_surface, countdown_rect)

    pygame.display.flip()


# Główna pętla gry
while True:
    # Obsługa zdarzeń
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Klawisze
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                if not game_active and not game_over:
                    game_active = True
                elif game_over:
                    # Restart gry
                    score_left = 0
                    score_right = 0
                    game_over = False
                    game_active = True
                    reset_ball()

            if game_active:
                if event.key == K_DOWN:
                    paddle_right_speed += 7
                if event.key == K_UP:
                    paddle_right_speed -= 7
                if event.key == K_s:
                    paddle_left_speed += 7
                if event.key == K_w:
                    paddle_left_speed -= 7

        if event.type == KEYUP and game_active:
            if event.key == K_UP:
                paddle_right_speed += 7
            if event.key == K_DOWN:
                paddle_right_speed -= 7
            if event.key == K_w:
                paddle_left_speed += 7
            if event.key == K_s:
                paddle_left_speed -= 7

    # Logika gry
    if game_active:
        ball_movement()
        paddle_right_movement()
        paddle_left_movement()

    # Rysowanie ekranu
    screen.fill(background_color)
    pygame.draw.rect(screen, objects_color, paddle_right)
    pygame.draw.rect(screen, objects_color, paddle_left)
    pygame.draw.ellipse(screen, objects_color, ball)
    pygame.draw.aaline(screen, objects_color, (screen_width/2, 0), (screen_width/2, screen_height))

    # Wyświetlanie wyniku
    score_text = font_small.render(f"{score_left} : {score_right}", True, text_color)
    score_rect = score_text.get_rect(center=(screen_width/2, 30))
    screen.blit(score_text, score_rect)

    # Ekran startowy
    if not game_active and not game_over:
        screen.blit(start_text, start_rect)

    # Ekran końca gry
    if game_over:
        winner = "LEFT WON" if score_left >= max_score else "RIGHT WON"
        win_text = font_large.render(winner, True, text_color)
        win_rect = win_text.get_rect(center=(screen_width/2, screen_height/2 - 50))

        restart_text = font_small.render("Press SPACE to restart", True, text_color)
        restart_rect = restart_text.get_rect(center=(screen_width/2, screen_height/2 + 30))

        screen.blit(win_text, win_rect)
        screen.blit(restart_text, restart_rect)

    # Aktualizacja okna
    pygame.display.flip()
    clock.tick(60)
