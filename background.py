
import os
bg = pygame.image.load(os.path.join('image','background.jpg'))
night_bg = pygame.image.load(os.path.join('image','night_bg.png'))

class back_ground():
	def __init__(self,x,y,isnight = False):
		self.x = x
		self.y = y
		self.isnight = isnight
		self.bg = bg
	def draw_bg(self,win):
		if not self.isnight:
			self.bg = bg
		else:
			self.bg = night_bg
		win.blit(self.bg,(self.x,self.y))