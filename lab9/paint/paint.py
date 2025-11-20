import pygame
import sys

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (34, 139, 34)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((640, 600))
pygame.display.set_caption("Drawing App")
clock = pygame.time.Clock()
screen.fill(WHITE)

# Load toolbar images
menu_img = pygame.image.load("menu.png")
line_img = pygame.image.load("drawline.png")
rect_img = pygame.image.load("rect.png")
square_img = pygame.image.load("square.png")
circle_img = pygame.image.load("circle.png")
etrien_img = pygame.image.load("etrien.png")
trien_img = pygame.image.load("trien.png")
rhombus_img = pygame.image.load("rhombus.png")
eraser_img = pygame.image.load("eraser.png")

# Scale images
line_img = pygame.transform.scale(line_img, (20, 20))
rect_img = pygame.transform.scale(rect_img, (30, 30))
square_img = pygame.transform.scale(square_img, (30, 30))
circle_img = pygame.transform.scale(circle_img, (25, 25))
etrien_img = pygame.transform.scale(etrien_img, (30, 30))
trien_img = pygame.transform.scale(trien_img, (30, 30))
rhombus_img = pygame.transform.scale(rhombus_img, (30, 30))
eraser_img = pygame.transform.scale(eraser_img, (30, 30))

# Drawing functions
def draw_rectangle(screen, start, end, color, width):
    rect = pygame.Rect(start, (end[0]-start[0], end[1]-start[1]))
    pygame.draw.rect(screen, color, rect, width)

def draw_circle(screen, start, end, color, width):
    radius = int(((end[0]-start[0])**2 + (end[1]-start[1])**2)**0.5)
    pygame.draw.circle(screen, color, start, radius, width)

def draw_square(screen, start, size, color, width):
    rect = pygame.Rect(start, (size, size))
    pygame.draw.rect(screen, color, rect, width)

def draw_right_triangle(screen, start, size, color):
    x, y = start
    points = [(x, y - size), (x - size, y + size), (x + size, y + size)]
    pygame.draw.polygon(screen, color, points)

def draw_equilateral_triangle(screen, start, size, color):
    x, y = start
    points = [(x, y - size), (x - size, y + size), (x + size, y + size)]
    pygame.draw.polygon(screen, color, points)

def draw_rhombus(screen, start, size, color):
    x, y = start
    points = [(x, y - size), (x + size, y), (x, y + size), (x - size, y)]
    pygame.draw.polygon(screen, color, points)

# Toolbar
def draw_toolbar():
    screen.blit(menu_img, (0, 0))
    # Draw color boxes
    pygame.draw.rect(screen, BLACK, (10, 5, 20, 20))
    pygame.draw.rect(screen, GREEN, (30, 5, 20, 20))
    pygame.draw.rect(screen, BLUE, (50, 5, 20, 20))
    pygame.draw.rect(screen, YELLOW, (70, 5, 20, 20))
    pygame.draw.rect(screen, RED, (90, 5, 20, 20))
    # Draw tools
    screen.blit(line_img, (150, 5))
    screen.blit(rect_img, (170, 0))
    screen.blit(square_img, (200, 0))
    screen.blit(circle_img, (230, 3))
    screen.blit(etrien_img, (255, 0))
    screen.blit(trien_img, (285, 0))
    screen.blit(rhombus_img, (315, 0))
    screen.blit(eraser_img, (600, 0))

# Toolbar click detection
def check_toolbar_click(mouseX, mouseY, color, drawing_mode):
    if 0 <= mouseY <= 30:
        # Color buttons
        if 10 <= mouseX <= 30:
            return BLACK, drawing_mode
        elif 30 <= mouseX <= 50:
            return GREEN, drawing_mode
        elif 50 <= mouseX <= 70:
            return BLUE, drawing_mode
        elif 70 <= mouseX <= 90:
            return YELLOW, drawing_mode
        elif 90 <= mouseX <= 110:
            return RED, drawing_mode
        # Eraser
        elif 600 <= mouseX <= 630:
            return WHITE, 'eraser'
        # Tools
        elif 150 <= mouseX <= 170:
            return color, 'free'
        elif 170 <= mouseX <= 200:
            return color, 'rect'
        elif 200 <= mouseX <= 230:
            return color, 'square'
        elif 230 <= mouseX <= 255:
            return color, 'circle'
        elif 255 <= mouseX <= 285:
            return color, 'etrien'
        elif 285 <= mouseX <= 315:
            return color, 'trien'
        elif 315 <= mouseX <= 345:
            return color, 'rhombus'
    return color, drawing_mode

# Main loop
def main():
    running = True
    drawing_mode = "free"
    color = BLUE
    radius = 10
    start_pos = None
    drawing = False
    points = []

    while running:
        mouseX, mouseY = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_UP:
                    radius = min(100, radius + 1)
                elif event.key == pygame.K_DOWN:
                    radius = max(1, radius - 1)
                elif event.key == pygame.K_r:
                    color = RED
                    drawing_mode = "free"
                elif event.key == pygame.K_g:
                    color = GREEN
                    drawing_mode = "free"
                elif event.key == pygame.K_b:
                    color = BLUE
                    drawing_mode = "free"
                elif event.key == pygame.K_y:
                    color = YELLOW
                    drawing_mode = "free"

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    color, drawing_mode = check_toolbar_click(mouseX, mouseY, color, drawing_mode)
                    if mouseY > 30:
                        start_pos = event.pos
                        drawing = True
                        if drawing_mode == "free":
                            points = [event.pos]

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and drawing:
                    end_pos = event.pos
                    if drawing_mode == "rect":
                        draw_rectangle(screen, start_pos, end_pos, color, radius)
                    elif drawing_mode == "circle":
                        draw_circle(screen, start_pos, end_pos, color, radius)
                    elif drawing_mode == "square":
                        draw_square(screen, start_pos, 100, color, radius)
                    elif drawing_mode == "etrien":
                        draw_right_triangle(screen, start_pos, 50, color)
                    elif drawing_mode == "trien":
                        draw_equilateral_triangle(screen, start_pos, 50, color)
                    elif drawing_mode == "rhombus":
                        draw_rhombus(screen, start_pos, 50, color)
                    drawing = False

            elif event.type == pygame.MOUSEMOTION:
                if drawing:
                    if drawing_mode == "free":
                        points.append(event.pos)
                        if len(points) > 1:
                            pygame.draw.line(screen, color, points[-2], points[-1], radius)
                    elif drawing_mode == "eraser":
                        pygame.draw.circle(screen, WHITE, event.pos, radius)

        draw_toolbar()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
