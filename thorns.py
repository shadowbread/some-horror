class Thorn:
	def __init__(self, x, y, time):
		self.x = x
		self.y = y
		self.change_time = time
		self.time = self.change_time
		self.condition = True
	def render(self):
		self.time -= 1
		if self.time == 0:
			if self.condition:
				self.condition = False
			else:
				self.condition = True
			self.time = self.change_time
	def get_par(self):
		return (self.x, self.y, self.condition)