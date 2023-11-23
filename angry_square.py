class Angry_square():
	def __init__(self, xx, yy, axiss, fp, sp, speedd):
		to = 1
		x = xx
		y = yy
		axis = axiss
		first_point = fp
		second_point = sp
		speed = speedd
	def render(self):
		if axis == "x":
			if x <= first_point:
				to = 1
			elif x >= second_point:
				to = -1
		else:
			if y <= first_point:
				to = 1
			elif y >= second_point:
				to = -1
		if axis == 'x':
			x += speed * to
		elif axis == 'y':
			y += speed * to