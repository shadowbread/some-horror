class Wall:
	def __init__(self, xx, yy, w, h):
		self.x = xx
		self.y = yy
		self.width = w
		self.height = h

	def get_par(self):
		return (self.x, self.y, self.width, self.height)

	def check(mx, my, to):
		xw, yw = 0, 0
		if to == "right":
			xw = mx + 5
		elif to == "left":
			xw = mx - 5
		elif to == "down":
			yw = my + 5
		elif to == "up":
			yw = my -5
		if yw >= y and yw <= y + height:
			if xw >= y and xw <= x + width:
				return False
			else:
				return True
		else:
			return True