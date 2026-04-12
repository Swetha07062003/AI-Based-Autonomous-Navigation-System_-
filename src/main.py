import pygame
from path_planning import astar
from simulation import draw, WIDTH, ROWS

pygame.init()

win = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("AI Autonomous Navigation")

grid = [[0 for _ in range(ROWS)] for _ in range(ROWS)]

start = None
end = None
path = []
robot_pos = None

mode = None
moving = False

clock = pygame.time.Clock()


def get_clicked_pos(pos):
    gap = WIDTH // ROWS
    x, y = pos
    row = y // gap
    col = x // gap
    return row, col


running = True
while running:
    clock.tick(5)

    # ✅ MOVE ROBOT (CORRECT)
    if moving and path:
        if len(path) > 0:
            robot_pos = path.pop(0)
        else:
            moving = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_s:
                mode = "start"

            elif event.key == pygame.K_e:
                mode = "end"

            elif event.key == pygame.K_SPACE:
                if start and end:
                    path = astar(grid, start, end)
                    robot_pos = start
                    moving = True

            elif event.key == pygame.K_r:
                grid = [[0 for _ in range(ROWS)] for _ in range(ROWS)]
                start = None
                end = None
                path = []
                robot_pos = None
                moving = False
                mode = None

    left, _, right = pygame.mouse.get_pressed()

    if left:
        pos = pygame.mouse.get_pos()
        row, col = get_clicked_pos(pos)

        if mode == "start":
            start = (row, col)
            robot_pos = start
            mode = None

        elif mode == "end":
            end = (row, col)
            mode = None

        else:
            grid[row][col] = 1

    if right:
        pos = pygame.mouse.get_pos()
        row, col = get_clicked_pos(pos)
        grid[row][col] = 0

    draw(win, grid, path, robot_pos, end)

pygame.quit()