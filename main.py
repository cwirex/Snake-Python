import pygame
from pygame.locals import *

def draw_block(x, y, size):
    block = pygame.Rect(x, y, size, size)
    block_color = (30, 240, 10, 200)
    pygame.draw.rect(surface, block_color, block)

if __name__ == '__main__':
    # Initialise screen
    pygame.init()
    pygame.display.set_caption('Snake - Python 3.8')
    surface = pygame.display.set_mode((900, 600))
    surface.fill((250, 250, 250))

    # Display score
    score = 0
    font_size = 42
    font = pygame.font.Font(None, font_size)
    text = font.render(f'Score: {score}', False, (10, 10, 10))
    text_pos = text.get_rect()
    text_pos.x = surface.get_width() - text.get_rect().width - font_size / 2
    text_pos.y = font_size / 2
    surface.blit(text, text_pos)

    block_size = 30
    pos = [0, 0]

    running = True
    # Event loop
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    pos[1] -= block_size
                elif event.key == K_RIGHT:
                    pos[0] += block_size
                elif event.key == K_LEFT:
                    pos[0] -= block_size
                elif event.key == K_DOWN:
                    pos[1] += block_size
                elif event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False

        surface.fill((250, 250, 250))
        draw_block(pos[0], pos[1], block_size)
        surface.blit(text, text_pos)
        pygame.display.flip()
