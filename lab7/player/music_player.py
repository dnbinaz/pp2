import pygame 
from pygame import mixer

pygame.init()
mixer.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
FPS = 50
done = False
n = 0

musics = ['newyear/DJ.mp3', 'newyear/JingleBell.mp3', 'newyear/Last-Christmas.mp3', 'newyear/Mabel.mp3', 'newyear/Queen.mp3']
plays = ['cover/DJ.jpg', 'cover/JingleBell.jpg', 'cover/Last-Christmas.jpg', 'cover/Mabel.jpg', 'cover/Queen.jpg']

pause_icon = 'pause.png'
play_icon = 'play-buttton.png'
rewind_button = 'rewind-button.png'
forward_button = 'forward-button.png'

def load_scaled(path, size):
    img = pygame.image.load(path)
    return pygame.transform.scale(img, size)

def start(n):
    mixer.music.load(musics[n])
    mixer.music.set_volume(0.2)
    mixer.music.play()
    mixer.music.pause()  # стартуем с паузы

def draw_screen(n, paused):
    screen.fill((255, 255, 255))

    cover = load_scaled(plays[n], (500, 500))     # размер обложки
    btn_prev = load_scaled(rewind_button, (30, 30))
    btn_next = load_scaled(forward_button, (30, 30))
    btn_play = load_scaled(play_icon if paused else pause_icon, (40, 40))

    screen.blit(cover, (150, 100))           # обложка
    screen.blit(btn_prev, (330, 660))        # назад
    screen.blit(btn_play, (380, 650))        # play/pause
    screen.blit(btn_next, (440, 660))        # вперёд

    pygame.display.flip()

start(n)
paused = True
draw_screen(n, paused)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if paused:
                    mixer.music.unpause()
                    paused = False
                else:
                    mixer.music.pause()
                    paused = True
                draw_screen(n, paused)

            elif event.key == pygame.K_RIGHT:
                n = (n + 1) % len(musics)
                start(n)
                paused = True
                draw_screen(n, paused)

            elif event.key == pygame.K_LEFT:
                n = (n - 1) % len(musics)
                start(n)
                paused = True
                draw_screen(n, paused)

    clock.tick(FPS)

pygame.quit()