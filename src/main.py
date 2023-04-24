import pygame
import random
from controllers.hits import HitsController
from controllers.screen import ScreenController

from utils.switches import SwitchController
from utils.displays import DisplayController

switch_controller = SwitchController()

display_controller = DisplayController()

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
        elif event.type == pygame.KEYDOWN:
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
                # Aumenta a fase do jogo
                if screen_controller.phase > 13:
                    running = False
                else:
                    screen_controller.increase_phase()
    if screen_controller.phase < 4:
        display_controller.set_left_display_number(switch_controller.get_switch_number_1())
        display_controller.set_right_display_number(switch_controller.get_switch_number_2())
    if screen_controller.phase == 4:
        display_controller.set_left_display()
        display_controller.set_right_display()

    # Desenha os scores na tela
    screen_controller.draw_text(str(screen_controller.score_2), (50, screen_controller.screen_height - 50))
    screen_controller.draw_text(str(screen_controller.score_1), (screen_controller.screen_width -  50, screen_controller.screen_height - 50))

    # Atualiza a tela do jogo
    pygame.display.update()

# Sai do Pygame
pygame.quit()
