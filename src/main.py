import pygame
import random

# Gera o número aleatório
numero_aleatorio = random.randint(1, 100)

pygame.init()

# Define as dimensões da janela
screen_width = 800
screen_height = 600

# Cria a janela
screen = pygame.display.set_mode((screen_width, screen_height))

# Define o título da janela
pygame.display.set_caption("Meu Jogo")

# Cria uma fonte Pygame
fonte = pygame.font.Font(None, 36)

# Renderiza o número aleatório como um texto
texto_numero = fonte.render(str(numero_aleatorio), True, (255, 255, 255))

# Desenha o texto na tela
posicao_texto = (screen_width // 2, screen_height // 2)
screen.blit(texto_numero, posicao_texto)

# Atualiza a tela do jogo
pygame.display.update()

running = True
while running:
    # Verifica se o jogador quer sair do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualiza a tela do jogo
    pygame.display.update()

# Sai do Pygame
pygame.quit()
