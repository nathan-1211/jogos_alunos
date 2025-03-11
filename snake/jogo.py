import pygame
import random

# Inicialização do Pygame
pygame.init()
pygame.display.set_caption("Jogo Snake Python")

# Configurações da tela
largura, altura = 600, 400
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

# Cores
preta = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)

# Configurações do jogo
tamanho_quadrado = 10
velocidade_jogo = 15

def gerar_comida():
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / 10.0) * 10.0
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / 10.0) * 10.0
    return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])

def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho, tamanho])

def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Helvetica", 25)
    texto = fonte.render(f"Pontos: {pontuacao}", True, vermelha)
    tela.blit(texto, [10, 10])

def selecionar_velocidade(tecla, velocidade_x, velocidade_y):
    if tecla == pygame.K_DOWN and velocidade_y == 0:
        return 0, tamanho_quadrado
    elif tecla == pygame.K_UP and velocidade_y == 0:
        return 0, -tamanho_quadrado
    elif tecla == pygame.K_RIGHT and velocidade_x == 0:
        return tamanho_quadrado, 0
    elif tecla == pygame.K_LEFT and velocidade_x == 0:
        return -tamanho_quadrado, 0
    return velocidade_x, velocidade_y

def rodar_jogo():
    fim_jogo = False
    x, y = largura // 2, altura // 2
    velocidade_x, velocidade_y = 0, 0
    tamanho_cobrinha = 1
    pixels = []
    comida_x, comida_y = gerar_comida()
    
    while not fim_jogo:
        tela.fill(preta)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key, velocidade_x, velocidade_y)
        
        x += velocidade_x
        y += velocidade_y
        
        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_jogo = True
        
        pixels.append([x, y])
        if len(pixels) > tamanho_cobrinha:
            del pixels[0]
        
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True
        
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)
        desenhar_cobra(tamanho_quadrado, pixels)
        desenhar_pontuacao(tamanho_cobrinha - 1)
        
        if x == comida_x and y == comida_y:
            tamanho_cobrinha += 1
            comida_x, comida_y = gerar_comida()
        
        pygame.display.update()
        relogio.tick(velocidade_jogo)
    
    pygame.quit()

rodar_jogo()
