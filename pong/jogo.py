import pygame

# Inicialização do Pygame
pygame.init()

# Configuração da janela
WIDTH, HEIGHT = 1000, 700
wn = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# Cores
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Fonte para a pontuação
font = pygame.font.Font(None, 74)

# Bola
radius = 15
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_vel_x, ball_vel_y = 5, 5

# Paddles
paddle_width, paddle_height = 20, 100
left_paddle_x, left_paddle_y = 50, HEIGHT // 2 - paddle_height // 2
right_paddle_x, right_paddle_y = WIDTH - 50 - paddle_width, HEIGHT // 2 - paddle_height // 2
left_paddle_vel, right_paddle_vel = 0, 0
paddle_speed = 7

# Pontuação
left_score = 0
right_score = 0

# Loop do jogo
run = True
clock = pygame.time.Clock()

while run:
    clock.tick(60)  # Define o FPS para 60
    wn.fill(BLACK)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                right_paddle_vel = -paddle_speed
            elif event.key == pygame.K_DOWN:
                right_paddle_vel = paddle_speed
            elif event.key == pygame.K_w:
                left_paddle_vel = -paddle_speed
            elif event.key == pygame.K_s:
                left_paddle_vel = paddle_speed
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_UP, pygame.K_DOWN]:
                right_paddle_vel = 0
            if event.key in [pygame.K_w, pygame.K_s]:
                left_paddle_vel = 0

    # Movimento da bola
    ball_x += ball_vel_x
    ball_y += ball_vel_y

    # Colisão com paredes superior e inferior
    if ball_y - radius <= 0 or ball_y + radius >= HEIGHT:
        ball_vel_y *= -1

    # Verifica se a bola saiu pelos lados e atualiza a pontuação
    if ball_x + radius >= WIDTH:
        left_score += 1
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_vel_x *= -1
    elif ball_x - radius <= 0:
        right_score += 1
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_vel_x *= -1

    # Movimento dos paddles
    left_paddle_y += left_paddle_vel
    right_paddle_y += right_paddle_vel

    # Limites dos paddles
    left_paddle_y = max(0, min(HEIGHT - paddle_height, left_paddle_y))
    right_paddle_y = max(0, min(HEIGHT - paddle_height, right_paddle_y))

    # Colisão da bola com os paddles
    if left_paddle_x <= ball_x - radius <= left_paddle_x + paddle_width and left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
        ball_vel_x *= -1
        ball_x = left_paddle_x + paddle_width + radius

    if right_paddle_x <= ball_x + radius <= right_paddle_x + paddle_width and right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
        ball_vel_x *= -1
        ball_x = right_paddle_x - radius

    # Desenha os objetos
    pygame.draw.circle(wn, BLUE, (int(ball_x), int(ball_y)), radius)
    pygame.draw.rect(wn, RED, (left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(wn, RED, (right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    
    # Renderiza a pontuação
    left_text = font.render(str(left_score), True, WHITE)
    right_text = font.render(str(right_score), True, WHITE)
    wn.blit(left_text, (WIDTH // 4, 20))
    wn.blit(right_text, (WIDTH * 3 // 4, 20))

    # Atualiza a tela
    pygame.display.update()

# Encerra o Pygame
pygame.quit()
