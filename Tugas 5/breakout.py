import pygame
import random

# Definisi warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Kelas dasar GameObject
class GameObject:
    def __init__(self, x, y, width, height, color=WHITE):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

# Kelas Ball (subclass dari GameObject)
class Ball(GameObject):
    def __init__(self, x, y, radius, color=WHITE):
        super().__init__(x, y, radius * 2, radius * 2, color)
        self.radius = radius
        self.dx = random.choice([-1, 1])  # Randomize arah horizontal
        self.dy = -1  # Arah vertikal default

    def move(self, speed):
        self.rect.x += self.dx * speed
        self.rect.y += self.dy * speed

    def collide_with_paddle(self, paddle):
        if self.rect.colliderect(paddle.rect) and self.dy > 0:
            self.dy = -1

    def collide_with_wall(self, width, height):
        if self.rect.left <= 0 or self.rect.right >= width:
            self.dx *= -1
        if self.rect.top <= 0:
            self.dy = 1

# Kelas Paddle (subclass dari GameObject)
class Paddle(GameObject):
    def __init__(self, x, y, width, height, color=WHITE, speed=5):
        super().__init__(x, y, width, height, color)
        self.speed = speed

    def move(self, dx):
        self.rect.x += dx * self.speed
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 800:
            self.rect.right = 800

# Kelas Block (subclass dari GameObject)
class Block(GameObject):
    def __init__(self, x, y, width, height, color=RED):
        super().__init__(x, y, width, height, color)

# Kelas Game
class Game:
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Simple Game")
        self.clock = pygame.time.Clock()
        self.game_over = False
        self.background = pygame.image.load("1.jpg")  # Memuat gambar latar belakang
        self.ball = Ball(400, 300, 10)
        self.paddle = Paddle(350, 550, 100, 10)
        self.blocks = []
        for i in range(10):
            for j in range(5):
                self.blocks.append(Block(50 + i * 70, 50 + j * 30, 60, 20))

    def run(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.paddle.move(-1)
            if keys[pygame.K_RIGHT]:
                self.paddle.move(1)

            self.ball.move(3)
            self.ball.collide_with_paddle(self.paddle)
            self.ball.collide_with_wall(self.width, self.height)

            for block in self.blocks:
                if self.ball.rect.colliderect(block.rect):
                    self.ball.dy *= -1
                    self.blocks.remove(block)
                    break

            # Menutup permainan jika bola melewati papan bawah
            if self.ball.rect.top > self.height:
                self.game_over = True

            self.screen.blit(self.background, (0, 0))  # Menampilkan latar belakang
            self.paddle.draw(self.screen)
            self.ball.draw(self.screen)
            for block in self.blocks:
                block.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

# Main
if __name__ == "__main__":
    game = Game()
    game.run()
