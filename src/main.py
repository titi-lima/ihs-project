import pygame
import random
from controllers.hits import HitsController
from controllers.screen import ScreenController

from mock.switches import SwitchController

switch_controller = SwitchController("000000001000000110")

# Função para gerar um novo número aleatório
def gerar_numero_aleatorio():
    global numero_aleatorio
    numero_aleatorio = random.randint(1, 100)
    # Renderiza e desenha o número aleatório na tela
    screen_controller.draw_text_center(str(numero_aleatorio))
    # Atualiza toda a tela
    pygame.display.flip()

# Gera o número aleatório
numero_aleatorio = random.randint(1, 100)

pygame.init()

screen_controller = ScreenController()

hits_controller = HitsController(screen_controller)

# Cria uma caixa de texto
caixa_retangulo = pygame.Rect(50, 150, 200, 50)
texto_digitado = ""
caixa_foco = False

# Renderiza e desenha o número aleatório na tela
screen_controller.draw_text_center(str(numero_aleatorio))

# Desenha os scores na tela
screen_controller.draw_text(str(screen_controller.score_1), (50, screen_controller.screen_height - 50))
screen_controller.draw_text(str(screen_controller.score_2), (screen_controller.screen_width -  50, screen_controller.screen_height - 50))

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
                screen_controller.reset_screen()
                # Converte o número aleatório para binário com 9 bits
                numero = "{0:b}".format(numero_aleatorio).zfill(9)
                hits_controller.check_hits(switch_controller, numero)
                # Verifica se o número digitado é igual ao número aleatório
                number_1 = switch_controller.get_switch_number_1()
                number_2 = switch_controller.get_switch_number_2()
                if number_1 == numero_aleatorio:
                    screen_controller.score_1 += 1
                if number_2 == numero_aleatorio:
                    screen_controller.score_2 += 1
                # Gerar um novo número aleatório quando o usuário pressiona Enter
                gerar_numero_aleatorio()
    
    # Desenha os scores na tela
    screen_controller.draw_text(str(screen_controller.score_1), (50, screen_controller.screen_height - 50))
    screen_controller.draw_text(str(screen_controller.score_2), (screen_controller.screen_width -  50, screen_controller.screen_height - 50))

    # Desenha a caixa de texto
    pygame.draw.rect(screen_controller.screen, (255, 255, 255), caixa_retangulo)
    if caixa_foco:
        pygame.draw.rect(screen_controller.screen, (0, 0, 255), caixa_retangulo, 2)
        texto_caixa = screen_controller.fonte.render(texto_digitado, True, (0, 0, 0))
        screen_controller.screen.blit(texto_caixa, (caixa_retangulo.x + 10, caixa_retangulo.y + 10))

    # Atualiza a tela do jogo
    pygame.display.update()

# Sai do Pygame
pygame.quit()
