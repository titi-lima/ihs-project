import pygame

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

        # Define as posições dos círculos
        self.circles_1 = [{'x': 50 + i * 25, 'y': self.screen_height - 100, 'color': (128, 128, 128)} for i in range(9)]
        self.circles_2 = [{'x': self.screen_width - 50 - 8 * 25 + i * 25, 'y': self.screen_height - 100, 'color': (128, 128, 128)} for i in range(9)]

        self.draw_circles(self.circles_1)
        self.draw_circles(self.circles_2)

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

    def draw_circles(self, circle_array):
        # Desenha os círculos na tela
        for circle in circle_array:
            pygame.draw.circle(self.screen, circle['color'], (circle['x'], circle['y']), 10)

    def set_circle_color(self,circle_index, color):
        # Define a cor de um círculo específico
        circle = self.circles_1[circle_index]
        pygame.draw.circle(self.screen, color, (circle['x'], circle['y']), 10)
    
    def reset_screen(self):
        # Define a cor de fundo da tela
        self.screen.fill((0, 0, 0))
        pass

    def update_screen(self):
        # Atualiza a tela do jogo
        pygame.display.update()
        pass
