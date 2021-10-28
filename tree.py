import pygame
import os

tree = pygame.image.load(os.path.join('image','tree.png'))
tree_night = pygame.image.load(os.path.join('image','tree_night.png'))
tree_cut = pygame.image.load(os.path.join('image','tree1.png'))

class Tree():
	def __init__(self,x,y,width,height,numOftree,isfired=False,isnight = False):
		self.x = x 
		self.y = y 
		self.width = width
		self.height = height 
		self.numOftree = numOftree
		self.dot = 1
		self.hitbox = (self.x,self.y,self.width,self.height)
		self.hit = pygame.Rect(self.x,self.y,self.width,self.height)
		self.tree = tree
		self.isfired = isfired
		self.isnight = isnight
	def draw_tree(self,win):
		if not self.isfired:
			if not self.isnight:
				self.tree = tree
			else:
				self.tree = tree_night
		else:
			self.tree = tree_cut
		for i in range(self.numOftree):
			if i %2 !=0 :

				self.hit = win.blit(pygame.transform.scale(self.tree,(self.width,self.height + i*10*self.dot)),(self.x + (i+1)*25,self.y - i*10*self.dot))
				self.hitbox = (self.x + (i+1)*25,self.y-10*i*self.dot,self.width,self.height + i*10*self.dot)
				
			else:
				self.hit = win.blit(pygame.transform.scale(self.tree,(self.width,self.height )),(self.x  + (i+1)*25,self.y ))
				self.hitbox = (self.x +(i+1)*25,self.y,self.width,self.height)