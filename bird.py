import pygame
import os
bird = pygame.image.load(os.path.join('image','bird.png'))
bird_night = pygame.image.load(os.path.join('image','bird_night.png'))
bird_cut = pygame.image.load(os.path.join('image','bird_cut.png'))


class Bird(): 
	def __init__(self,x,y,width,height,isfired = False): #Khoi tao cac thuoc tinh của Bird
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.hit = pygame.Rect(self.x,self.y,self.width,self.height)
		self.bird = bird
		self.isfired = isfired
		self.isnight = False
	def draw_bird(self,win):			#Cai dat thuoc tinh ve giao dien bird len man hinh chinh

		if not self.isfired:
			if not self.isnight:
				self.bird = bird
			else:
				self.bird = bird_night
		else:
			self.bird = bird_cut
		self.hit = win.blit(pygame.transform.scale(self.bird,(self.width,self.height)),(self.x,self.y))
