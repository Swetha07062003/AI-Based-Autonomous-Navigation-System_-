import pygame

WIDTH = 600
ROWS = 20

WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (200,200,200)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

def draw(win, grid, path, robot_pos, end):
    win.fill(WHITE)
    gap = WIDTH // ROWS

    for i in range(ROWS):
        for j in range(ROWS):
            x = j * gap
            y = i * gap

            if grid[i][j] == 1:
                pygame.draw.rect(win, BLACK, (x, y, gap, gap))

            pygame.draw.rect(win, GREY, (x, y, gap, gap), 1)

    for p in path:
        pygame.draw.rect(win, GREEN, (p[1]*gap, p[0]*gap, gap, gap))

    if end:
        pygame.draw.rect(win, RED, (end[1]*gap, end[0]*gap, gap, gap))

    if robot_pos:
        pygame.draw.rect(win, BLUE, (robot_pos[1]*gap, robot_pos[0]*gap, gap, gap))

    pygame.display.update()