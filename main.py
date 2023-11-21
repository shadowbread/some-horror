import pygame
pygame.init()

width = 400
height = 400

screen = pygame.display.set_mode((width, height))
fpsclck = pygame.time.Clock()
sprint = 1
map_x, map_y = 0, 0
map_size_x, map_size_y = 600, 600
# min_x = 0
# max_x = 800
# min_y, max_y = 0, 800 
walls = [
	{'x': 50, 'y': 50, 'width': 50, 'height':100},
	{'x': 200, 'y': 50, 'width': 50, 'height':100}
	]

def draw_walls():
	global screen, walls, width, height
	for wall in walls:
		pygame.draw.rect(screen, (255, 255, 255), ((width / 2 ) - map_x + wall['x'], (height / 2) - map_y + wall['y'], wall['width'], wall['height']))

def check_walls(to):
	global walls, map_x, map_y
	i = True
	map_xx = map_x
	map_yy = map_y
	if to == 'right':
		map_xx = map_x + 5
	elif to == 'left':
		map_xx = map_x - 5
	elif to == 'down':
		map_yy = map_y + 5
	elif to == 'up':
		map_yy = map_y - 5
	for wall in walls:
		if map_yy > wall['y'] and map_yy < wall['y'] + wall['height']:
			if map_xx > wall['x'] and map_xx < wall['x'] + wall['width']:
				i = False
	return i

def draw_map():
	global screen, width, height, map_x, map_y, map_size_x, map_size_y
	screen.fill('black')
	pygame.draw.rect(screen, (0, 0, 255), ((width / 2 ) - map_x, (height / 2) - map_y, map_size_x, map_size_y))

def keyboard():
	global map_x, map_y, min_x, map_y, sprint
	keys = pygame.key.get_pressed()
	if keys[pygame.K_SPACE]:
		sprint = 2
	else:
		sprint = 1
	if keys[pygame.K_RIGHT] and map_x < map_size_x and check_walls('right'):
		map_x += 5 * sprint
	if keys[pygame.K_LEFT] and map_x > 0 and check_walls('left'):
		map_x -= 5 * sprint
	if keys[pygame.K_DOWN] and map_y < map_size_y and check_walls('down'):
		map_y += 5 * sprint
	if keys[pygame.K_UP] and map_y > 0 and check_walls('up'):
		map_y -= 5 * sprint

def draw_player():
	global screen, width, height
	player_size = 20
	x = (width / 2) - (player_size / 2)
	y = (height / 2) - (player_size / 2)
	pygame.draw.rect(screen, (255, 255, 0), (x, y, player_size, player_size))

def game():
	keyboard()
	draw_map()
	draw_walls()
	draw_player()

while True:
    game()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
    fpsclck.tick(50)
