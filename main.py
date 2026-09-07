import pygame
import math
import sys

pygame.init()

# Constantes
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Office FPS")

clock = pygame.time.Clock()
FONT = pygame.font.SysFont("Arial", 20)

TILE_SIZE = 64
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 120
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 3 * DIST * TILE_SIZE
SCALE = WIDTH // NUM_RAYS

# Map bureau : W = mur, D = porte, C = ordinateur, 0 = vide
game_map = [
    "WWWWWW",
    "W0C0DW",
    "W0000W",
    "WWWWWW",
]

map_width = len(game_map[0])
map_height = len(game_map)

# Position de départ safe (au centre de la pièce)
player_x = TILE_SIZE * 2.5
player_y = TILE_SIZE * 2.5
player_angle = 0

# Variables interaction
computer_open = False
door_open = False

# Inventaire lunettes
has_glasses = True
glasses_on = False

# Fichiers PC simulés
fs_items = ["Projet.py", "Notes.txt", "README.md"]
fs_selected = 0
fs_scroll = 0

def draw_minimap():
    mini_map_scale = 5
    for y in range(map_height):
        for x in range(map_width):
            rect = pygame.Rect(x * TILE_SIZE // mini_map_scale, y * TILE_SIZE // mini_map_scale,
                               TILE_SIZE // mini_map_scale, TILE_SIZE // mini_map_scale)
            if game_map[y][x] == 'W':
                pygame.draw.rect(screen, (100, 100, 100), rect)
            elif game_map[y][x] == 'D':
                pygame.draw.rect(screen, (150, 75, 0), rect)
            elif game_map[y][x] == 'C':
                pygame.draw.rect(screen, (0, 0, 255), rect)
            else:
                pygame.draw.rect(screen, (30, 30, 30), rect)
    # Joueur sur minimap
    px = int(player_x / mini_map_scale)
    py = int(player_y / mini_map_scale)
    pygame.draw.circle(screen, (255, 0, 0), (px, py), 5)
    # Ligne direction joueur
    dx = math.cos(player_angle) * 20
    dy = math.sin(player_angle) * 20
    pygame.draw.line(screen, (255, 255, 0), (px, py), (px + dx, py + dy), 2)

def mapping(x, y):
    return int(x // TILE_SIZE), int(y // TILE_SIZE)

def ray_casting():
    start_angle = player_angle - HALF_FOV
    cur_angle = start_angle
    walls = []

    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)

        for depth in range(1, MAX_DEPTH):
            x = player_x + depth * cos_a
            y = player_y + depth * sin_a

            map_x, map_y = mapping(x, y)
            if 0 <= map_x < map_width and 0 <= map_y < map_height:
                if game_map[map_y][map_x] in ['W', 'D', 'C']:
                    depth_corrected = depth * math.cos(player_angle - cur_angle)
                    walls.append((depth_corrected, ray, game_map[map_y][map_x]))
                    break
            else:
                break
        else:
            walls.append((MAX_DEPTH, ray, '0'))

        cur_angle += DELTA_ANGLE
    return walls

def draw_3d(walls):
    for depth, ray, tile in walls:
        if depth == 0:
            depth = 0.0001
        proj_height = int(PROJ_COEFF / depth)
        color = (255, 255, 255)
        if tile == 'W':
            color = (160, 160, 160)
        elif tile == 'D':
            color = (150, 75, 0)
        elif tile == 'C':
            color = (0, 0, 255)
        shade = 255 / (1 + depth * depth * 0.0001)
        shade = max(min(shade, 255), 30)
        wall_color = tuple(min(int(c * shade / 255), 255) for c in color)
        pygame.draw.rect(screen, wall_color, (ray * SCALE, HEIGHT // 2 - proj_height // 2, SCALE, proj_height))

def draw_lunettes_ui(selected, scroll):
    font = pygame.font.SysFont("Arial", 20)
    y = 50 - scroll
    for i, item in enumerate(fs_items):
        color = (255, 255, 0) if i == selected else (255, 255, 255)
        txt = font.render(item, True, color)
        screen.blit(txt, (20, y))
        y += 30

def check_interaction():
    global computer_open, door_open
    interact_dist = 50
    interact_x = player_x + math.cos(player_angle) * interact_dist
    interact_y = player_y + math.sin(player_angle) * interact_dist
    map_x, map_y = mapping(interact_x, interact_y)

    if 0 <= map_x < map_width and 0 <= map_y < map_height:
        tile = game_map[map_y][map_x]
        if tile == 'C':  # ordinateur
            if not glasses_on:  # si les lunettes ne sont pas sur le joueur
                computer_open = not computer_open

        elif tile == 'D':
            door_open = not door_open
            row = list(game_map[map_y])
            row[map_x] = '0' if door_open else 'D'
            game_map[map_y] = "".join(row)

def move_player(dx, dy):
    global player_x, player_y
    next_x = player_x + dx
    next_y = player_y + dy
    map_x, map_y = mapping(next_x, next_y)
    if 0 <= map_x < map_width and 0 <= map_y < map_height:
        if game_map[map_y][map_x] == '0':
            player_x = next_x
            player_y = next_y

# Main loop
running = True
mouse_sensitivity = 0.003
pygame.event.set_grab(True)
pygame.mouse.set_visible(False)

while running:
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if computer_open:
                    computer_open = False
                else:
                    running = False
            elif event.key == pygame.K_e:
                check_interaction()
            elif event.key == pygame.K_l and has_glasses:
                glasses_on = not glasses_on
            if glasses_on or computer_open:
                if event.key == pygame.K_UP:
                    fs_selected = (fs_selected - 1) % len(fs_items)
                elif event.key == pygame.K_DOWN:
                    fs_selected = (fs_selected + 1) % len(fs_items)

    # Mouvements clavier
    keys = pygame.key.get_pressed()
    speed = 120 * dt
    if not computer_open or glasses_on:
        if keys[pygame.K_z]:
            move_player(math.cos(player_angle) * speed, math.sin(player_angle) * speed)
        if keys[pygame.K_s]:
            move_player(-math.cos(player_angle) * speed, -math.sin(player_angle) * speed)
        if keys[pygame.K_q]:
            move_player(math.cos(player_angle - math.pi / 2) * speed, math.sin(player_angle - math.pi / 2) * speed)
        if keys[pygame.K_d]:
            move_player(math.cos(player_angle + math.pi / 2) * speed, math.sin(player_angle + math.pi / 2) * speed)

        mx, my = pygame.mouse.get_rel()
        player_angle += mx * mouse_sensitivity
        player_angle %= 2 * math.pi
    else:
        pygame.mouse.get_rel()

    screen.fill((0, 0, 0))
    walls = ray_casting()
    draw_3d(walls)
    draw_minimap()

    if glasses_on:
        draw_lunettes_ui(fs_selected, fs_scroll)
        # Filtre violet discret
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((128, 0, 128, 30))  # violet avec transparence
        screen.blit(overlay, (0, 0))
    elif computer_open:
        # Affiche l'ordi physique normal
        font = pygame.font.SysFont("Arial", 24)
        title = font.render("Ordinateur virtuel", True, (255, 255, 255))
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 120))
        y = 160 - fs_scroll
        for i, item in enumerate(fs_items):
            color = (255, 255, 0) if i == fs_selected else (255, 255, 255)
            txt = font.render(item, True, color)
            screen.blit(txt, (150, y))
            y += 40

    pygame.display.flip()

pygame.quit()
sys.exit()
