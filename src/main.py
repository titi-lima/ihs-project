import pygame
import random

from mock.switches import SwitchController

switch_controller = SwitchController("000000001000000110")

# Função para gerar um novo número aleatório
def gerar_numero_aleatorio():
    global numero_aleatorio
    screen.fill((0, 0, 0))
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

# Define o score dos jogadores
score_1 = 0
score_2 = 0

# Define as dimensões da janela
screen_width = 800
screen_height = 600

# Cria a janela
screen = pygame.display.set_mode((screen_width, screen_height))

# Define o título da janela
pygame.display.set_caption("Meu Jogo")

# Cria uma fonte Pygame
fonte = pygame.font.Font(None, 36)

# Cria uma caixa de texto
caixa_retangulo = pygame.Rect(50, 150, 200, 50)
texto_digitado = ""
caixa_foco = False

# Renderiza o número aleatório como um texto
texto_numero = fonte.render(str(numero_aleatorio), True, (255, 255, 255))

# Desenha o texto na tela
posicao_texto = (screen_width // 2, screen_height // 2)
screen.blit(texto_numero, posicao_texto)

# Desenha os scores na tela
texto_score_1 = fonte.render(str(score_1), True, (255, 255, 255))
screen.blit(texto_score_1, (50, screen_height - 50))

texto_score_2 = fonte.render(str(score_2), True, (255, 255, 255))
screen.blit(texto_score_2, (screen_width -  50, screen_height - 50))

# Atualiza a tela do jogo
pygame.display.update()

running = True
while running:
    # Verifica se o jogador quer sair do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if caixa_retangulo.collidepoint(event.pos):
                caixa_foco = True
            else:
                caixa_foco = False
        elif event.type == pygame.KEYDOWN:
            if caixa_foco:
                if event.key == pygame.K_BACKSPACE:
                    texto_digitado = texto_digitado[:-1]
                elif event.key == pygame.K_RETURN:
                    print(texto_digitado)
                    # Define o valor dos switches
                    switch_controller.set_switch_array_value("{0:b}".format(int(texto_digitado, 2)).zfill(18))
                    print(switch_controller.get_switch_array())
                    texto_digitado = ""
                else:
                    texto_digitado += event.unicode
            if event.key == pygame.K_RETURN:
                # Gerar um novo número aleatório quando o usuário pressiona Enter
                number_1 = switch_controller.get_switch_number_1()
                number_2 = switch_controller.get_switch_number_2()
                if number_1 == numero_aleatorio:
                    score_1 += 1
                if number_2 == numero_aleatorio:
                    score_2 += 1
                gerar_numero_aleatorio()
                print("Score 1: " + str(score_1))
                print("Score 2: " + str(score_2))
    
    # Desenha os scores na tela
    texto_score_1 = fonte.render(str(score_1), True, (255, 255, 255))
    screen.blit(texto_score_1, (50, screen_height - 50))

    texto_score_2 = fonte.render(str(score_2), True, (255, 255, 255))
    screen.blit(texto_score_2, (screen_width - 50, screen_height - 50))

    # Desenha a caixa de texto
    pygame.draw.rect(screen, (255, 255, 255), caixa_retangulo)
    if caixa_foco:
        pygame.draw.rect(screen, (0, 0, 255), caixa_retangulo, 2)
        texto_caixa = fonte.render(texto_digitado, True, (0, 0, 0))
        screen.blit(texto_caixa, (caixa_retangulo.x + 10, caixa_retangulo.y + 10))

    # Atualiza a tela do jogo
    pygame.display.update()

# Sai do Pygame
pygame.quit()
