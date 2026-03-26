import pygame
import heapq

WIDTH = 600
ROWS = 25
CELL = WIDTH // ROWS

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)   # Start
RED = (255, 0, 0)     # End
BLUE = (0, 0, 255)    # Path
YELLOW = (255, 255, 0) # Open nodes
GREY = (200, 200, 200) # Grid lines

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(draw, grid, start, end):
    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    g_score = {start: 0}
    visited = set()

    while open_list:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        _, current = heapq.heappop(open_list)

        if current in visited:
            continue
        visited.add(current)

        if current == end:
            while current in came_from:
                current = came_from[current]
                if current != start:
                    grid[current[0]][current[1]] = BLUE
                draw()
                pygame.time.delay(30)
            return True

        for d in [(0,1),(1,0),(0,-1),(-1,0)]:
            neighbor = (current[0] + d[0], current[1] + d[1])

            if 0 <= neighbor[0] < ROWS and 0 <= neighbor[1] < ROWS:
                if grid[neighbor[0]][neighbor[1]] == BLACK:
                    continue

                temp_g = g_score[current] + 1

                if neighbor not in g_score or temp_g < g_score[neighbor]:
                    g_score[neighbor] = temp_g
                    f_score = temp_g + heuristic(neighbor, end)
                    heapq.heappush(open_list, (f_score, neighbor))
                    came_from[neighbor] = current

                    if neighbor != end:
                        grid[neighbor[0]][neighbor[1]] = YELLOW

        draw()
        pygame.time.delay(15)

    return False

def draw(win, grid):
    win.fill(WHITE)

    for i in range(ROWS):
        for j in range(ROWS):
            pygame.draw.rect(win, grid[i][j],
                             (j * CELL, i * CELL, CELL, CELL))

    for i in range(ROWS):
        pygame.draw.line(win, GREY, (0, i * CELL), (WIDTH, i * CELL))
        pygame.draw.line(win, GREY, (i * CELL, 0), (i * CELL, WIDTH))

    pygame.display.update()

def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("A* Pathfinding Visualizer")

    grid = [[WHITE for _ in range(ROWS)] for _ in range(ROWS)]

    start = None
    end = None

    run = True
    while run:
        draw(win, grid)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:  # Left click → wall
                x, y = pygame.mouse.get_pos()
                r, c = y // CELL, x // CELL
                grid[r][c] = BLACK

            if pygame.mouse.get_pressed()[2]:  # Right click → erase
                x, y = pygame.mouse.get_pos()
                r, c = y // CELL, x // CELL
                grid[r][c] = WHITE

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_s:
                    x, y = pygame.mouse.get_pos()
                    r, c = y // CELL, x // CELL
                    start = (r, c)
                    grid[r][c] = GREEN

                if event.key == pygame.K_e:
                    x, y = pygame.mouse.get_pos()
                    r, c = y // CELL, x // CELL
                    end = (r, c)
                    grid[r][c] = RED

                if event.key == pygame.K_SPACE:
                    if start and end:
                        astar(lambda: draw(win, grid), grid, start, end)

                if event.key == pygame.K_c:
                    grid = [[WHITE for _ in range(ROWS)] for _ in range(ROWS)]
                    start = None
                    end = None

    pygame.quit()

if __name__ == "__main__":
    main()