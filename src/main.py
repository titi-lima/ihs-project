import pygame
import random

# Função para gerar um novo número aleatório
def gerar_numero_aleatorio():
    global numero_aleatorio
    # Define a cor do retângulo a ser desenhado para apagar o número anterior
    cor_fundo = (0, 0, 0)
    # Desenha um retângulo preenchido na posição do número anterior
    pygame.draw.rect(screen, cor_fundo, (posicao_texto[0] - 50, posicao_texto[1] - 50, 100, 100))
    numero_aleatorio = random.randint(1, 100)
    # Renderiza o novo número aleatório como um texto
    texto_numero = fonte.render(str(numero_aleatorio), True, (255, 255, 255))
    # Desenha o novo número na tela
    screen.blit(texto_numero, posicao_texto)
    # Atualiza toda a tela
    pygame.display.flip()

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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Gerar um novo número aleatório quando o usuário pressiona Enter
                gerar_numero_aleatorio()



    # Atualiza a tela do jogo
    pygame.display.update()

# Sai do Pygame
pygame.quit()
