import pygame
import random

# --- Constants ---
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
GRID_SIZE = 20
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
PINK = (231, 129, 235)
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

def random_pos(snake):
    while True:
        x = random.randrange(0, SCREEN_WIDTH, GRID_SIZE)
        y = random.randrange(0, SCREEN_HEIGHT, GRID_SIZE)
        if (x, y) not in snake:
            return (x, y)

def main():
    snake = [(100, 100)]
    direction = (1, 0)
    food = random_pos(snake)
    score, level, speed = 0, 1, 5

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                elif event.key == pygame.K_UP and direction != (0, 1):
                    direction = (0, -1)
                elif event.key == pygame.K_DOWN and direction != (0, -1):
                    direction = (0, 1)
                elif event.key == pygame.K_LEFT and direction != (1, 0):
                    direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                    direction = (1, 0)

        # Move snake
        head = ((snake[0][0] + direction[0] * GRID_SIZE) % SCREEN_WIDTH,
                (snake[0][1] + direction[1] * GRID_SIZE) % SCREEN_HEIGHT)

        if head in snake[1:]:
            break  # Game over

        snake.insert(0, head)
        if head == food:
            score += 1
            if score % 3 == 0:
                level += 1
                speed += 1
            food = random_pos(snake)
        else:
            snake.pop()

        # Draw everything
        screen.fill(WHITE)
        for x, y in snake:
            pygame.draw.rect(screen, GREEN, (x, y, GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, PINK, (*food, GRID_SIZE, GRID_SIZE))

        font = pygame.font.Font(None, 36)
        screen.blit(font.render(f"Score: {score}", True, BLACK), (10, 10))
        screen.blit(font.render(f"Level: {level}", True, BLACK), (10, 40))

        pygame.display.flip()
        clock.tick(speed)

    # Game over screen
    screen.fill(WHITE)
    font = pygame.font.Font(None, 48)
    text = font.render("Game Over! ESC to exit", True, BLACK)
    screen.blit(text, (100, 270))
    pygame.display.flip()

    # Wait for ESC
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return

main()
