class Angry_square():
	def __init__(self, xx, yy, axiss, fp, sp, speedd):
		self.to = 1
		self.x = xx
		self.y = yy
		self.axis = axiss
		self.first_point = fp
		self.second_point = sp
		self.speed = speedd
	def render(self):
		if self.axis == "x":
			if self.x <= self.first_point:
				self.to = 1
			elif self.x >= self.second_point:
				self.to = -1
		else:
			if self.y <= self.first_point:
				self.to = 1
			elif self.y >= self.second_point:
				self.to = -1
		if self.axis == 'x':
			self.x += self.speed * self.to
		elif axis == 'y':
			self.y += self.speed * self.to
	def get_par(self):
		return (self.x, self.y)