# Imports
import pygame, sys
from pygame.locals import *
import random, time

# Initialize Pygame
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen settings and game variables
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5            # Base speed of enemies and coins
SCORE = 0
COINS_COLLECTED = 0
COINS_FOR_SPEEDUP = 5  # Increase enemy speed after collecting N coins

# Fonts
font_large = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over_text = font_large.render("Game Over", True, BLACK)

# Background
background = pygame.image.load("AnimatedStreet.png")

# Display setup
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer Game")

# -------------------------- SPRITE CLASSES --------------------------
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        """Move enemy down and reset when off-screen, incrementing score."""
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        """Move player left or right based on key input."""
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Random coin size / "weight" effect: bigger coins are rarer
        weight_options = [30, 40, 50, 60]  # Different coin sizes
        size = random.choice(weight_options)
        self.value = {30: 1, 40: 2, 50: 3, 60: 5}[size]  # Coin value based on size
        original_image = pygame.image.load("Coin.png")
        self.image = pygame.transform.scale(original_image, (size, size))
        self.rect = self.image.get_rect()
        self.reset_position()

    def reset_position(self):
        """Randomly place coin above screen to fall down."""
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(-150, -50))

    def move(self):
        """Move coin down and reset if it moves off-screen."""
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.reset_position()


# -------------------------- SPRITE GROUPS --------------------------
P1 = Player()
E1 = Enemy()
C1 = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# Event to gradually increase base speed
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# -------------------------- GAME LOOP --------------------------
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.3  # Gradual speed increase over time
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Draw background
    DISPLAYSURF.blit(background, (0, 0))

    # Draw score and coin info
    score_display = font_small.render(f"Score: {SCORE}", True, BLACK)
    coins_display = font_small.render(f"Coins: {COINS_COLLECTED}", True, BLACK)
    DISPLAYSURF.blit(score_display, (10, 10))
    DISPLAYSURF.blit(coins_display, (300, 10))

    # Move and draw all sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Collision: Player hits enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over_text, (30, 250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Collision: Player collects coin
    collided_coins = pygame.sprite.spritecollide(P1, coins, True)
    if collided_coins:
        for coin in collided_coins:
            COINS_COLLECTED += coin.value  # Add weighted value
        # Spawn new coin(s)
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)
        # Increase enemy speed after collecting N coins
        if COINS_COLLECTED % COINS_FOR_SPEEDUP == 0:
            SPEED += 1

    pygame.display.update()
    FramePerSec.tick(FPS)
