import pygame
import os
item = [pygame.transform.scale(pygame.image.load(os.path.join('image','collect.png')),(20,20)),pygame.transform.scale(pygame.image.load(os.path.join('image','gun.png')),(25,15))]

class Item():
	def __init__(self,x,y,choice,isappear=True):
		self.x = x
		self.y = y
		self.isappear = isappear
		self.hit = pygame.Rect(self.x,self.y,20,20)
		self.choice = choice
	def draw_item(self,win):
		if self.isappear :
		
			self.hit=win.blit(item[self.choice],(self.x,self.y))