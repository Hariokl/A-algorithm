from random import randint, random

import pygame as pg
from star import A_star


def from_pos_to_tiles(pos):
    return pos[0] // TILE, pos[1] // TILE


def draw_grid(grd, scr):
    scr.fill((100, 100, 100))
    for y in range(len(grd)):
        for x in range(len(grd[0])):
            pg.draw.rect(scr, (0, 0, 0), (x * TILE + TILE // 20, y * TILE + TILE // 20, TILE - TILE // 10, TILE - TILE // 10), 0)
            if grid[y][x] == 100:
                pg.draw.rect(scr, (255, 150, 50), (x * TILE + TILE // 6, y * TILE + TILE // 6, TILE - TILE // 3, TILE - TILE // 3), 0, border_radius=TILE//15)


def draw_astar(dts, scr):
    scr.fill((0, 0, 0, 0))
    for dote in dts:
        pg.draw.rect(scr, (255, 255, 255), (dote[0] * TILE + TILE // 6, dote[1] * TILE + TILE // 6, TILE - TILE // 3, TILE - TILE // 3), 0, border_radius=TILE//15)


FPS = 60
WIDTH, HEIGHT = 960, int(960 // 1.5)
TILE = WIDTH // 20

display = pg.display.set_mode((WIDTH, HEIGHT))
main_display = pg.Surface((WIDTH, HEIGHT))
aditional_display = pg.Surface((WIDTH, HEIGHT), pg.SRCALPHA, 32).convert_alpha()
aditional_display.fill((0, 0, 0, 0))
clock = pg.time.Clock()
grid = [[100 if random() < 0.3 else 0 for _ in range(WIDTH // TILE)] for _ in range(HEIGHT // TILE)]
running = True
dotes = None
last_dotes = None

start = (0, 0)
goal = None
mouse_mode = 1

draw_grid(grid, main_display)
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.MOUSEBUTTONUP:
            if mouse_mode:
                goal = from_pos_to_tiles(pg.mouse.get_pos())
            else:
                start = from_pos_to_tiles(pg.mouse.get_pos())
            dotes, cost = A_star(grid, start, goal)
            if cost > 0:
                dotes = last_dotes
        if event.type == pg.KEYUP and event.key == pg.K_c:
            mouse_mode = 1 - mouse_mode

    if dotes is not None and last_dotes != dotes:
        draw_astar(dotes, aditional_display)
    display.blit(main_display, (0, 0))
    display.blit(aditional_display, (0, 0))
    pg.display.flip()
    pg.display.set_caption("Goal" if mouse_mode else "Start")
    clock.tick(FPS)
    last_dotes = dotes
