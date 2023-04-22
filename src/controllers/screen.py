import pygame
import random

class ScreenController:
    def __init__(self):
        # Define o score dos jogadores
        self.score_1 = 0
        self.score_2 = 0

        # Define as dimensões da janela
        self.screen_width = 800
        self.screen_height = 600

        # Cria a janela
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        # Define o título da janela
        pygame.display.set_caption("Meu Jogo")

        # Cria uma fonte Pygame
        self.fonte = pygame.font.Font(None, 36)
        pass

    def draw_text_center(self, text):
        # Renderiza o texto
        texto = self.fonte.render(text, True, (255, 255, 255))
        # Desenha o texto na tela
        self.screen.blit(texto, (self.screen_width // 2, self.screen_height // 2))
        pass

    def draw_text(self, text, position):
        # Renderiza o texto
        texto = self.fonte.render(text, True, (255, 255, 255))
        # Desenha o texto na tela
        self.screen.blit(texto, position)
        pass
    
    def reset_screen(self):
        # Define a cor de fundo da tela
        self.screen.fill((0, 0, 0))
        pass

    def update_screen(self):
        # Atualiza a tela do jogo
        pygame.display.update()
        pass
