import pygame
import os
DINO = [pygame.image.load(os.path.join('image','rex1.png')),pygame.image.load(os.path.join('image','rex2.png')),pygame.image.load(os.path.join('image','rex3.png')),pygame.image.load(os.path.join('image','rex4.png'))]
class Dino():
	def __init__(self,x,y,width,height,jump = False):
		self.x = x 
		self.y = y 
		self.width = width 
		self.height = height
		self.walk_count = 0
		self.jump = jump
		self.dot = 0.50
		self.jump_count = 8


	def draw_dino(self,win):
		
		if self.walk_count + 1 >=4:
			self.walk_count = 0
		win.blit(pygame.transform.scale(DINO[self.walk_count],(self.width,self.height)),(self.x,self.y+5))
		self.walk_count +=1
		if self.jump:
			if self.jump_count >= -8:
				self.y -=(self.jump_count * abs(self.jump_count)) * self.dot
				self.jump_count -=1
			else:
				self.jump_count = 8
				self.jump = False