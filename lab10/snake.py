import pygame
import random
import time
import psycopg2

# --- PostgreSQL setup ---
DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "postgres",
    "user": "ihlasova75icloud.com",
    "password": "20022009"
}

def init_db():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id SERIAL PRIMARY KEY,
            username TEXT UNIQUE NOT NULL
        );
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS user_score (
            score_id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL REFERENCES users(user_id),
            score INTEGER NOT NULL,
            level INTEGER NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    ''')
    conn.commit()
    conn.close()

def get_or_create_user(username):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("SELECT user_id FROM users WHERE username = %s", (username,))
    row = cur.fetchone()
    if row:
        user_id = row[0]
    else:
        cur.execute("INSERT INTO users(username) VALUES (%s) RETURNING user_id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()
    conn.close()
    return user_id

def get_last_score(user_id):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute(
        "SELECT score, level FROM user_score WHERE user_id = %s ORDER BY timestamp DESC LIMIT 1",
        (user_id,)
    )
    row = cur.fetchone()
    conn.close()
    if row:
        return row[0], row[1]
    else:
        return 0, 1  # default score and level

def save_score(user_id, score, level):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO user_score(user_id, score, level) VALUES (%s, %s, %s)",
        (user_id, score, level)
    )
    conn.commit()
    conn.close()


# --- Pygame Snake setup ---
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
GRID_SIZE = 20
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
FOOD_COLORS = [(255, 0, 0), (0, 0, 255), (255, 165, 0)]

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# --- Functions for game ---
def random_pos(snake):
    while True:
        x = random.randrange(0, SCREEN_WIDTH, GRID_SIZE)
        y = random.randrange(0, SCREEN_HEIGHT, GRID_SIZE)
        if (x, y) not in snake:
            return (x, y)

def generate_food(snake):
    pos = random_pos(snake)
    weight = random.randint(1, 3)
    color = FOOD_COLORS[weight - 1]
    lifetime = random.randint(5, 10)
    spawn_time = time.time()
    return {"pos": pos, "weight": weight, "color": color, "lifetime": lifetime, "spawn_time": spawn_time}

def get_username_pygame():
    username = ""
    active = True
    while active:
        screen.fill(WHITE)
        txt_surface = font.render("Enter Username: " + username, True, BLACK)
        screen.blit(txt_surface, (50, 250))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    active = False
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    username += event.unicode
    return username.strip()


def main():
    init_db()
    username = get_username_pygame()
    if not username:
        return
    user_id = get_or_create_user(username)
    score, level = get_last_score(user_id)
    speed = 5 + (level - 1)

    snake = [(100, 100)]
    direction = (1, 0)
    foods = [generate_food(snake)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_score(user_id, score, level)
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    save_score(user_id, score, level)
                    return
                elif event.key == pygame.K_p:
                    save_score(user_id, score, level)
                elif event.key == pygame.K_UP and direction != (0, 1):
                    direction = (0, -1)
                elif event.key == pygame.K_DOWN and direction != (0, -1):
                    direction = (0, 1)
                elif event.key == pygame.K_LEFT and direction != (1, 0):
                    direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                    direction = (1, 0)

        head = ((snake[0][0] + direction[0] * GRID_SIZE) % SCREEN_WIDTH,
                (snake[0][1] + direction[1] * GRID_SIZE) % SCREEN_HEIGHT)

        if head in snake[1:]:
            save_score(user_id, score, level)
            running = False
            break

        snake.insert(0, head)

        eaten_food = None
        LEVEL_SCORE = 10  

        for food in foods:
            if head == food["pos"]:
                score += food["weight"]
                eaten_food = food

                new_level = score // LEVEL_SCORE + 1

                if new_level > level:  
                    level = new_level
                    speed += 1  
                    print(f"LEVEL UP → {level}")  

                break  

        if eaten_food:
            foods.remove(eaten_food)
            foods.append(generate_food(snake))
        else:
            snake.pop()

        current_time = time.time()
        foods = [f for f in foods if current_time - f["spawn_time"] <= f["lifetime"]]
        if len(foods) == 0:
            foods.append(generate_food(snake))

        screen.fill(WHITE)
        for x, y in snake:
            pygame.draw.rect(screen, GREEN, (x, y, GRID_SIZE, GRID_SIZE))
        for food in foods:
            pygame.draw.rect(screen, food["color"], (*food["pos"], GRID_SIZE, GRID_SIZE))

        screen.blit(font.render(f"Score: {score}", True, BLACK), (10, 10))
        screen.blit(font.render(f"Level: {level}", True, BLACK), (10, 40))

        pygame.display.flip()
        clock.tick(speed)

    # Game over screen
    screen.fill(WHITE)
    text = font.render("Game Over! ESC to exit", True, BLACK)
    screen.blit(text, (100, 270))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return

if __name__ == "__main__":
    main()