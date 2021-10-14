import pygame 
import os
import sys
from test import Dino
pygame.init()
win = pygame.display.set_mode((600,300))
bg = pygame.image.load(os.path.join('image','background.jpg'))
bg1 = pygame.image.load(os.path.join('image','background.jpg'))
DINO = [pygame.image.load(os.path.join('image','rex1.png')),pygame.image.load(os.path.join('image','rex2.png')),pygame.image.load(os.path.join('image','rex3.png')),pygame.image.load(os.path.join('image','rex4.png'))]
clock = pygame.time.Clock()
# class Dino():
# 	def __init__(self,x,y,width,height,jump = False):
# 		self.x = x 
# 		self.y = y 
# 		self.width = width 
# 		self.height = height
# 		self.walk_count = 0
# 		self.jump = jump
# 		self.dot = 0.50
# 		self.jump_count = 8


# 	def draw_dino(self,win):
		
# 		if self.walk_count + 1 >=4:
# 			self.walk_count = 0
# 		win.blit(pygame.transform.scale(DINO[self.walk_count],(self.width,self.height)),(self.x,self.y+5))
# 		self.walk_count +=1
# 		if self.jump:
# 			if self.jump_count >= -8:
# 				self.y -=(self.jump_count * abs(self.jump_count)) * self.dot
# 				self.jump_count -=1
# 			else:
# 				self.jump_count = 8
# 				self.jump = False

class Tree():
	def __init__(self,x,y,width,height,numOftree):
		self.x = x 
		self.y = y 
		self.width = width
		self.height = height 
		self.numOftree = numOftree

	


run = True 
dino = Dino(50,220,50,50)
X = 0
Y = 0
while run:
	clock.tick(15)
	win.blit(bg,(X,Y))
	win.blit(bg1,(X+600,Y))
	if X <-600:
		X=0
	X-=15
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run= False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				dino.jump = True
	dino.draw_dino(win)
	pygame.display.update()

