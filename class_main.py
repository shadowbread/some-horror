import pygame
import config
import levels
class Game():
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((config.width, config.height))
		self.clock = pygame.time.Clock()
		self.map_x = 25
		self.map_y = 25
		self.level_num = 0
	def draw_on_map(self, color:tuple, sp:tuple, line=0):
		pygame.draw.rect(self.screen, color, ((config.width / 2) - self.map_x + sp[0], (config.height / 2) - self.map_y + sp[1], sp[2], sp[3]), line)	

	def draw_player(self):
		pygame.draw.rect(self.screen, config.player_clr, ((config.width / 2) - (20 / 2), (config.height / 2) - (20 / 2), 20, 20))

	def respawn(self):
		self.map_x, self.map_y = (25, 25)

	def wall_check(self, to):
		xw = self.map_x
		yw = self.map_y
		ret = True
		if to == "right":
			xw += self.speed
		elif to == "left":
			xw -= self.speed
		elif to == "down":
			yw += self.speed
		elif to == "up":
			yw -= self.speed
		for wall in levels.levels_list[self.level_num].get_walls():
			x, y, width, height = wall.get_par()
			if yw >= y and yw <= y + height:
				if xw >= x and xw <= x + width:
					# self.respawn()
					ret = False
		return ret

	def movement(self):
		keys = pygame.key.get_pressed()
		if keys[config.sprint_bind]:
			self.speed = 5 * 0.5
		else:
			self.speed = 5
		if keys[config.right_bind] and self.map_x < self.map_size_x and self.wall_check("right"):
			self.map_x += self.speed 
		if keys[config.down_bind] and self.map_y < self.map_size_y and self.wall_check("down"):
			self.map_y += self.speed 
		if keys[config.left_bind] and self.map_x > 0 and self.wall_check("left"):
			self.map_x -= self.speed 
		if keys[config.up_bind] and self.map_y > 0 and self.wall_check("up"):
			self.map_y -= self.speed 

	def draw_wall(self):
		for wall in levels.levels_list[self.level_num].get_walls():
			# pygame.draw.rect(self.screen, config.wall_clr, wall.get_par())
			self.draw_on_map(config.wall_clr, wall.get_par())
	def wall(self):
		self.draw_wall()

	def player(self):
		self.draw_player()
		self.movement()

	def thorns(self):
		thorns_list = levels.levels_list[self.level_num].get_thorns()
		for th in thorns_list:
			th.render()
			parameters = th.get_par()
			if parameters[2]:
				self.draw_on_map(config.thorns_clr, (parameters[0], parameters[1], 30, 30))
			else:
				self.draw_on_map(config.thorns_clr, (parameters[0], parameters[1], 30, 30), 2)
			if parameters[2]:
				if self.map_y >= parameters[1] and self.map_y <= parameters[1] + 20:
					if self.map_x >= parameters[0] and self.map_x <= parameters[0] + 20:
						self.respawn()
	
	def angry_square(self):
		squares_list = levels.levels_list[self.level_num].get_angry_squares()
		for s in squares_list:
			s.render()
			parameters = s.get_par()
			self.draw_on_map(config.angry_clr, parameters + (20, 20))

			if self.map_y >= parameters[1] and self.map_y <= parameters[1] + 20:
					if self.map_x >= parameters[0] and self.map_x <= parameters[0] + 20:
						self.respawn()

	def draw_map(self):
		self.screen.fill(config.background_clr)
		self.map_size_x, self.map_size_y = levels.levels_list[self.level_num].get_map()
		pygame.draw.rect(self.screen, config.map_clr, ((config.width / 2) - self.map_x, (config.height / 2) - self.map_y, self.map_size_x, self.map_size_y))
		self.wall()
		self.thorns()
		self.angry_square()
	def run(self):
		while True:
			self.draw_map()
			self.player()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
			pygame.display.update()
			pygame.display.set_caption(str(self.clock.get_fps()))
			self.clock.tick(50)
if __name__ == "__main__":
	app = Game()
	app.run()