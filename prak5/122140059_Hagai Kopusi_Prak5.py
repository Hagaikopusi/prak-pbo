import pygame
import sys
import time
import random

# Inisialisasi Pygame
pygame.init()

# Dimensi layar
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Balapan Mobil")

# Warna
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Mobil
PLAYER_WIDTH, PLAYER_HEIGHT = 100, 50
PLAYER_COLOR = (0, 255, 0)
player_speed = 5

# Garis finish
FINISH_LINE = WIDTH - 100

# Mobil musuh
ENEMY_COLOR = (255, 0, 0)
ENEMY_SPEED = 4

# Kelas mobil
class Car:
    def __init__(self, color, x, y):
        """Inisialisasi objek mobil."""
        self.color = color
        self.x = x
        self.y = y
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        self.speed = player_speed

    def draw(self):
        """Menggambar mobil."""
        pygame.draw.rect(SCREEN, self.color, (self.x, self.y, self.width, self.height))

    def move(self, direction):
        """Menggerakkan mobil."""
        if direction == "up" and self.y > 0:
            self.y -= self.speed
        elif direction == "down" and self.y < HEIGHT - self.height:
            self.y += self.speed
        elif direction == "right" and self.x < FINISH_LINE - self.width + 100:
            self.x += self.speed
        elif direction == "left" and self.x > 0:
            self.x -= self.speed

# Kelas musuh
class EnemyCar(Car):
    def __init__(self, color, x, y):
        """Inisialisasi objek mobil musuh."""
        super().__init__(color, x, y)
        self.speed = ENEMY_SPEED

# Kelas permainan
class Game:
    def __init__(self):
        """Inisialisasi objek permainan."""
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Car(PLAYER_COLOR, 50, HEIGHT // 2 - PLAYER_HEIGHT // 2)
        self.enemy = EnemyCar(ENEMY_COLOR, 100, HEIGHT // 2 - PLAYER_HEIGHT // 2 + 50)
        self.font = pygame.font.SysFont(None, 100)

    def draw_countdown(self):
        """Menampilkan countdown sebelum permainan dimulai."""
        for i in range(3, 0, -1):
            SCREEN.fill(WHITE)
            text = self.font.render(str(i), True, RED)
            SCREEN.blit(text, (WIDTH//2 - 25, HEIGHT//2 - 50))
            pygame.display.update()
            time.sleep(1)
        SCREEN.fill(WHITE)
        text = self.font.render("Go!", True, GREEN)
        SCREEN.blit(text, (WIDTH//2 - 50, HEIGHT//2 - 50))
        pygame.display.update()
        time.sleep(1)

    def draw_finish_line(self):
        """Menggambar garis finish."""
        pygame.draw.line(SCREEN, BLACK, (FINISH_LINE, 0), (FINISH_LINE, HEIGHT), 5)

    def game_over(self, message="You Win!"):
        """Menampilkan pesan akhir permainan."""
        text = self.font.render(message, True, GREEN)
        SCREEN.blit(text, (WIDTH//2 - 100, HEIGHT//2 - 25))
        pygame.display.update()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()

    def check_win(self):
        """Memeriksa apakah pemain atau musuh telah mencapai garis finish."""
        if self.player.x >= FINISH_LINE:
            self.game_over()
        elif self.enemy.x >= FINISH_LINE:
            self.game_over("You Lose!")

    def handle_events(self):
        """Menangani peristiwa."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def run(self):
        """Memulai permainan."""
        self.draw_countdown()
        while self.running:
            self.handle_events()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.player.move("right")
            elif keys[pygame.K_s]:
                self.player.move("left")

            self.enemy.move("right")

            SCREEN.fill(WHITE)
            self.draw_finish_line()
            self.player.draw()
            self.enemy.draw()
            self.check_win()
            pygame.display.update()
            self.clock.tick(30)

if __name__ == "__main__":
    game = Game()
    game.run()
