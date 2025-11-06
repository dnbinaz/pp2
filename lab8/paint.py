import pygame
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Drawing App")
    clock = pygame.time.Clock()

    # Default parameters
    radius = 10
    drawing_mode = 'free'  # free, rect, circle, eraser
    color = (0, 0, 255)
    start_pos = None
    drawing = False
    points = []

    while True:
        for event in pygame.event.get():
            # exit option
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                # color shortcuts
                if event.key == pygame.K_r:
                    color = (255, 0, 0)
                    drawing_mode = 'free'
                elif event.key == pygame.K_g:
                    color = (0, 255, 0)
                    drawing_mode = 'free'
                elif event.key == pygame.K_b:
                    color = (0, 0, 255)
                    drawing_mode = 'free'
                elif event.key == pygame.K_y:
                    color = (255, 255, 0)
                    drawing_mode = 'free'

                # change modes
                if event.key == pygame.K_1:
                    drawing_mode = 'free'
                elif event.key == pygame.K_2:
                    drawing_mode = 'rect'
                elif event.key == pygame.K_3:
                    drawing_mode = 'circle'
                elif event.key == pygame.K_BACKSPACE:
                    drawing_mode = 'eraser'

                # brush size
                if event.key == pygame.K_UP:
                    radius = min(100, radius + 1)
                elif event.key == pygame.K_DOWN:
                    radius = max(1, radius - 1)

            # mouse input
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    drawing = True
                    start_pos = event.pos
                    if drawing_mode == 'free':
                        points = [event.pos]

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and drawing:
                    end_pos = event.pos
                    if drawing_mode == 'rect':
                        draw_rectangle(screen, start_pos, end_pos, color, radius)
                    elif drawing_mode == 'circle':
                        draw_circle_shape(screen, start_pos, end_pos, color, radius)
                    drawing = False

            elif event.type == pygame.MOUSEMOTION:
                if drawing and drawing_mode == 'free':
                    pos = event.pos
                    points.append(pos)
                    if len(points) > 1:
                        pygame.draw.line(screen, color, points[-2], points[-1], radius)
                elif drawing and drawing_mode == 'eraser':
                    pos = event.pos
                    pygame.draw.circle(screen, (0, 0, 0), pos, radius)

        pygame.display.flip()
        clock.tick(60)


def draw_rectangle(screen, start, end, color, width):
    rect = pygame.Rect(start, (end[0] - start[0], end[1] - start[1]))
    pygame.draw.rect(screen, color, rect, width if width < 10 else 0)


def draw_circle_shape(screen, start, end, color, width):
    radius = int(((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2) ** 0.5)
    pygame.draw.circle(screen, color, start, radius, width if width < 10 else 0)


if __name__ == "__main__":
    main()