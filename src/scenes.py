import pygame

class Scene:
    def __init__(self, game):
        self.game = game

    def handle_event(self, event):
        pass

    def update(self):
        pass

    def draw(self, screen):
        pass

class MainMenuScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        # Inicializar elementos del menú principal (título, botones, etc.)
        self.font = pygame.font.Font(None, 36)
        self.title_text = self.font.render("The Quest", True, (255, 255, 255))
        self.start_button = self.font.render("Press SPACE to Start", True, (255, 255, 0))
        self.instructions_button = self.font.render("Press I for Instructions", True, (255, 255, 0))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.game.change_scene(GameScene(self.game))  # Cambiar a la escena del juego
            if event.key == pygame.K_i:
                self.game.change_scene(InstructionsScene(self.game)) # Cambiar a la escena de instrucciones

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((0, 0, 0))  # Fondo negro
        screen.blit(self.title_text, (100, 50))
        screen.blit(self.start_button, (100, 150))
        screen.blit(self.instructions_button, (100, 200))

class GameScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        # Inicializar elementos del juego (nave, obstáculos, etc.)
        self.player = Player()
        self.obstacles = []
        self.score = 0
        self.font = pygame.font.Font(None, 36)

    def handle_event(self, event):
        self.player.handle_event(event)

    def update(self):
        self.player.update()
        # Actualizar obstáculos, colisiones, etc.
        for obstacle in self.obstacles:
            obstacle.update()
            if self.player.collides_with(obstacle):
                self.game.exit_game() # Por ahora, salir al colisionar
        self.score += 1 # Incrementar la puntuación (ejemplo)

    def draw(self, screen):
        screen.fill((0, 0, 0))
        self.player.draw(screen)
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, (0, 255, 0), [(0, 25), (50, 0), (30, 25), (50, 50)])
        self.rect = self.image.get_rect(midleft=(50, 300))
        self.speed_y = 0

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.speed_y = -5
            elif event.key == pygame.K_DOWN:
                self.speed_y = 5
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                self.speed_y = 0

    def update(self):
        self.rect.y += self.speed_y
        self.rect.y = max(0, min(self.rect.y, 550)) # Mantener en pantalla

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def collides_with(self, obstacle):
        return self.rect.colliderect(obstacle.rect)

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.draw.rect(self.image, (255, 0, 0), (0, 0, 30, 30))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed_x = -3

    def update(self):
        self.rect.x += self.speed_x

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class InstructionsScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.font = pygame.font.Font(None, 36)
        self.instructions_text = [
            "Instructions:",
            "Use UP/DOWN arrows to move.",
            "Avoid the obstacles!",
            "Press SPACE to return to Main Menu"
        ]

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.game.change_scene(MainMenuScene(self.game))

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((0, 0, 0))
        y_offset = 50
        for line in self.instructions_text:
            text_surface = self.font.render(line, True, (255, 255, 255))
            screen.blit(text_surface, (50, y_offset))
            y_offset += 40