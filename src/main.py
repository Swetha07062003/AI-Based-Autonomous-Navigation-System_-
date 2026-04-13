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

step_delay = 200
last_move_time = 0

def get_clicked_pos(pos):
    gap = WIDTH // ROWS
    x, y = pos
    return y // gap, x // gap

# 🔥 GENERATE OBSTACLES WITH VALID PATH
def generate_valid_obstacles():
    global grid

    if not start or not end:
        print("❌ Set START and END first!")
        return

    while True:
        grid = [[0 for _ in range(ROWS)] for _ in range(ROWS)]

        for i in range(ROWS):
            for j in range(ROWS):
                if random.random() < 0.25:
                    grid[i][j] = 1

        grid[start[0]][start[1]] = 0
        grid[end[0]][end[1]] = 0

        temp_path = astar(grid, start, end)

        if temp_path:
            print("✅ Valid obstacles generated")
            return

running = True

while running:
    clock.tick(60)
    current_time = pygame.time.get_ticks()

    # 🔥 MOVEMENT
    if moving and current_time - last_move_time > step_delay:
        last_move_time = current_time

        if len(path) > 0:
            robot_pos = path.pop(0)
            print("Moving to:", robot_pos)
        else:
            print("Reached Goal")
            moving = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_s:
                mode = "start"
                print("Select START")

            elif event.key == pygame.K_e:
                mode = "end"
                print("Select END")

            elif event.key == pygame.K_g:
                generate_valid_obstacles()
                path = []
                robot_pos = start
                moving = False

            elif event.key == pygame.K_SPACE:
                if start and end:
                    path = astar(grid, start, end)

                    if path:
                        robot_pos = start
                        moving = True
                        print("🚀 Movement started")
                    else:
                        print("❌ No path!")

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
        row, col = get_clicked_pos(pygame.mouse.get_pos())

        if mode == "start":
            start = (row, col)
            robot_pos = start
            mode = None
            print("Start:", start)

        elif mode == "end":
            end = (row, col)
            mode = None
            print("End:", end)

        else:
            if (row, col) != start and (row, col) != end:
                grid[row][col] = 1

    if right:
        row, col = get_clicked_pos(pygame.mouse.get_pos())
        grid[row][col] = 0

    draw(win, grid, path, robot_pos, end)

pygame.quit()