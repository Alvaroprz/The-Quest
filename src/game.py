import pygame
from src import scenes  # Importa el módulo scenes

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.current_scene = scenes.MainMenuScene(self)  # Escena inicial: Menú principal
        self.running = True

    def handle_event(self, event):
        self.current_scene.handle_event(event)

    def update(self):
        self.current_scene.update()

    def draw(self):
        self.current_scene.draw(self.screen)

    def change_scene(self, scene):
        self.current_scene = scene

    def exit_game(self):
        self.running = False