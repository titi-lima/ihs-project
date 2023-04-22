#include "raylib.h"
#include <stdio.h>

int main()
{
	// Define as dimensões da janela
	int screenWidth = 800;
	int screenHeight = 600;

	// Inicia o raylib e cria a janela
	InitWindow(screenWidth, screenHeight, "Meu Jogo");

	// Gera um número aleatório entre 1 e 100
	int numeroAleatorio = GetRandomValue(1, 100);

	// Loop principal do jogo
	while (!WindowShouldClose())
	{
		// Desenha o número aleatório na tela
		BeginDrawing();
		ClearBackground(BLACK);

		// Cria uma fonte raylib
		Font fonte = GetFontDefault();

		// Renderiza o número aleatório como um texto
		char textoNumero[10];
		sprintf(textoNumero, "%d", numeroAleatorio);
		int larguraTexto = MeasureText(textoNumero, 36);
		int xTexto = (screenWidth - larguraTexto) / 2;
		int yTexto = screenHeight / 2;
		DrawText(textoNumero, xTexto, yTexto, 36, WHITE);

		// Atualiza a tela do jogo
		EndDrawing();
	}

	// Sai do raylib
	CloseWindow();

	return 0;
}
