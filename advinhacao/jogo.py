import pygame
import random

# Inicialização do Pygame
pygame.init()

# Definição das cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (173, 216, 230)
LIGHT_BLUE = (173, 216, 230)
BUTTON_COLOR = (70, 130, 180)
BUTTON_HOVER_COLOR = (100, 149, 237)

# Configurações da tela
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo de Adivinhação")

# Fonte
font = pygame.font.Font(None, 50)
small_font = pygame.font.Font(None, 36)

# Número a ser adivinhado
numero_secreto = random.randint(1, 10)

# Variáveis do jogo
tentativas = 0
max_tentativas = 5
mensagem = "Adivinhe um número entre 1 e 10"
input_text = ''
game_over = False

# Função para desenhar o texto na tela
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, textrect)

# Função para desenhar uma caixa de entrada
def draw_input_box(text, font, color, surface, x, y, w, h):
    pygame.draw.rect(surface, color, (x, y, w, h), 2)
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x + 5, y + 5))

# Função para desenhar um botão
def draw_button(surface, color, rect, text, text_color, font):
    pygame.draw.rect(surface, color, rect)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(rect[0] + rect[2] // 2, rect[1] + rect[3] // 2))
    surface.blit(text_surface, text_rect)

# Função para reiniciar o jogo
def reset_game():
    global numero_secreto, tentativas, mensagem, input_text, game_over
    numero_secreto = random.randint(1, 10)
    tentativas = 0
    mensagem = "Adivinhe um número entre 1 e 10"
    input_text = ''
    game_over = False

# Loop principal do jogo
running = True
while running:
    screen.fill(LIGHT_BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and not game_over:
                tentativas += 1
                try:
                    guess = int(input_text)
                    if guess < numero_secreto:
                        mensagem = f"Mais alto! Você usou {tentativas} tentativas."
                    elif guess > numero_secreto:
                        mensagem = f"Mais baixo! Você usou {tentativas} tentativas."
                    else:
                        mensagem = f"Você acertou em {tentativas} tentativas!"
                        game_over = True
                except ValueError:
                    mensagem = "Por favor, insira um número válido."
                
                # Limpa a caixa de texto após cada tentativa
                input_text = ''

            if tentativas >= max_tentativas and not game_over:
                mensagem = f"Fim de jogo! O número era {numero_secreto}."
                game_over = True

            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]

            elif event.key == pygame.K_ESCAPE:
                running = False

            else:
                if event.unicode.isdigit():
                    input_text += event.unicode

        if event.type == pygame.MOUSEBUTTONDOWN and game_over:
            mouse_pos = event.pos
            button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50)
            if button_rect.collidepoint(mouse_pos):
                reset_game()

    draw_text(mensagem, font, BLACK, screen, WIDTH // 2, HEIGHT // 4)
    draw_input_box(input_text, small_font, BLACK, screen, WIDTH // 4, HEIGHT // 2, WIDTH // 2, 50)

    if game_over:
        button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50)
        mouse_pos = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse_pos):
            draw_button(screen, BUTTON_HOVER_COLOR, button_rect, "Recomeçar", WHITE, small_font)
        else:
            draw_button(screen, BUTTON_COLOR, button_rect, "Recomeçar", WHITE, small_font)

    pygame.display.flip()

pygame.quit()