import pygame

WIDTH = 600
ROWS = 20


def draw_grid(win):
    gap = WIDTH // ROWS
    for i in range(ROWS):
        pygame.draw.line(win, (200, 200, 200), (0, i * gap), (WIDTH, i * gap))
        pygame.draw.line(win, (200, 200, 200), (i * gap, 0), (i * gap, WIDTH))


def draw(win, grid, path, robot_pos, end):
    win.fill((255, 255, 255))

    gap = WIDTH // ROWS

    # 🔲 Obstacles
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                pygame.draw.rect(win, (0, 0, 0), (j * gap, i * gap, gap, gap))

    # 🟢 Path
    if path:
        for (r, c) in path:
            pygame.draw.rect(win, (0, 255, 0), (c * gap, r * gap, gap, gap))

    # 🔵 Robot (slightly improved color)
    if robot_pos:
        pygame.draw.rect(win, (0, 100, 255), (robot_pos[1] * gap, robot_pos[0] * gap, gap, gap))

    # 🔴 End
    if end:
        pygame.draw.rect(win, (255, 0, 0), (end[1] * gap, end[0] * gap, gap, gap))

    draw_grid(win)

    pygame.display.update()