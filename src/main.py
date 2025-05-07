import pygame
import sys
from src import game

def main():
    pygame.init()  # Inicializa Pygame

    # Configuración de la pantalla
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("The Quest")

    # Inicializar el juego
    game_instance = game.Game(screen)  # Crea una instancia de Game

    # Bucle principal del juego
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Manejar eventos del juego (teclas, etc.)
            game_instance.handle_event(event)  # Delega el manejo de eventos al juego

        # Actualizar el estado del juego
        game_instance.update()

        # Dibujar en la pantalla
        game_instance.draw()

        pygame.display.flip()  # Actualiza la pantalla
        pygame.time.Clock().tick(60)  # Limita el framerate a 60 FPS

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()