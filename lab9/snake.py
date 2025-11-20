import pygame
import random
import time

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
GRID_SIZE = 20
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
FOOD_COLORS = [(255, 0, 0), (0, 0, 255), (255, 165, 0)]  # Red, Blue, Orange

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

# Function to generate a random position not overlapping with snake
def random_pos(snake):
    while True:
        x = random.randrange(0, SCREEN_WIDTH, GRID_SIZE)
        y = random.randrange(0, SCREEN_HEIGHT, GRID_SIZE)
        if (x, y) not in snake:
            return (x, y)

# Function to generate a new food with random weight and lifetime
def generate_food(snake):
    pos = random_pos(snake)
    weight = random.randint(1, 3)  # Weight: 1, 2, or 3 points
    color = FOOD_COLORS[weight - 1]  # Different color for weight
    lifetime = random.randint(5, 10)  # Food disappears after 5-10 seconds
    spawn_time = time.time()
    return {"pos": pos, "weight": weight, "color": color, "lifetime": lifetime, "spawn_time": spawn_time}

def main():
    snake = [(100, 100)]
    direction = (1, 0)
    foods = [generate_food(snake)]  # Start with one food
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

        # Check for collision with itself
        if head in snake[1:]:
            break  # Game over

        snake.insert(0, head)

        # Check if snake eats any food
        eaten_food = None
        for food in foods:
            if head == food["pos"]:
                score += food["weight"]  # Increase score by food weight
                eaten_food = food
                if score % 3 == 0:  # Level up
                    level += 1
                    speed += 1
                break

        if eaten_food:
            foods.remove(eaten_food)
            foods.append(generate_food(snake))  # Spawn new food
        else:
            snake.pop()  # Move forward by removing tail

        # Remove foods that exceeded their lifetime
        current_time = time.time()
        foods = [f for f in foods if current_time - f["spawn_time"] <= f["lifetime"]]
        # Ensure at least one food exists
        if len(foods) == 0:
            foods.append(generate_food(snake))

        # Draw everything
        screen.fill(WHITE)
        for x, y in snake:
            pygame.draw.rect(screen, GREEN, (x, y, GRID_SIZE, GRID_SIZE))
        for food in foods:
            pygame.draw.rect(screen, food["color"], (*food["pos"], GRID_SIZE, GRID_SIZE))

        # Display score and level
        font = pygame.font.Font(None, 36)
        screen.blit(font.render(f"Score: {score}", True, BLACK), (10, 10))
        screen.blit(font.render(f"Level: {level}", True, BLACK), (10, 40))

        pygame.display.flip()
        clock.tick(speed)

    # Game over screen
    screen.fill(WHITE)
    font = pygame.font.Font(None, 48)
    text = font.render("Game Over!", True, BLACK)
    screen.blit(text, (100, 270))
    pygame.display.flip()

    # Wait for ESC to exit
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return

main()