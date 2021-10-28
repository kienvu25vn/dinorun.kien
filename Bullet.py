import pygame
import os

class bullet():
	def __init__(self,x,y,width,height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.hit = pygame.Rect(self.x,self.y,self.width,self.height)
	def draw_bullet(self,win):
		pygame.draw.rect(win,(255,0,0),(self.x,self.y,self.width,self.height))