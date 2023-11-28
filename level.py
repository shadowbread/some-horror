import wall
import thorns
import angry_square

class Level():
	def __init__(self, x, y):
		self.map_size_x = x
		self.map_size_y = y
		self.walls = []
		self.angry_squares = []
		self.thorns = []
	def get_map(self):
		return self.map_size_x, self.map_size_y
	def get_walls(self):
		return self.walls
	def get_thorns(self):
		return self.thorns
	def get_angry_squares(self):
		return self.angry_squares
	def add_angry_square(self, x, y, axis, fp, sp, speed):
		self.angry_squares.append(angry_square.Angry_square(x, y, axis, fp, sp, speed))
	def add_wall(self, x, y, w, h):
		self.walls.append(wall.Wall(x, y, w, h))
	def add_thorn(self, x, y, time):
		self.thorns.append(thorns.Thorn(x, y, time))
