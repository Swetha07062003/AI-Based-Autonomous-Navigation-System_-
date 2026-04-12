import pygame
import random
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


# ✅ AUTO OBSTACLE GENERATION
def generate_random_obstacles(grid, count=40):
    rows = len(grid)
    for _ in range(count):
        r = random.randint(0, rows - 1)
        c = random.randint(0, rows - 1)
        grid[r][c] = 1


running = True
while running:
    clock.tick(5)

    # ✅ REAL-TIME REPLANNING
    if moving:
        if robot_pos == end:
            moving = False
        else:
            new_path = astar(grid, robot_pos, end)

            if new_path:
                path = new_path
                if len(path) > 1:
                    robot_pos = path[1]
                else:
                    robot_pos = end
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

            # ✅ GENERATE OBSTACLES
            elif event.key == pygame.K_g:
                generate_random_obstacles(grid)

            # ✅ SAVE OUTPUT IMAGE
            elif event.key == pygame.K_p:
                pygame.image.save(win, "output.png")
                print("Screenshot saved!")

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