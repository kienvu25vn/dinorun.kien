import pygame 
import os
import sys
import random
DINO = [pygame.image.load(os.path.join('image','rex1.png')),pygame.image.load(os.path.join('image','rex2.png')),pygame.image.load(os.path.join('image','rex3.png')),pygame.image.load(os.path.join('image','rex4.png'))]
DINO_NIGHT = [pygame.image.load(os.path.join('image','b1.png')),pygame.image.load(os.path.join('image','b2.png')),pygame.image.load(os.path.join('image','b3.png')),pygame.image.load(os.path.join('image','b4.png'))]
dino_lie = [pygame.image.load(os.path.join('image','rexlie1.png')),pygame.image.load(os.path.join('image','rexlie2.png'))]
dino_lie_night = [pygame.image.load(os.path.join('image','a1.png')),pygame.image.load(os.path.join('image','a2.png'))]
dino_power_lie = [pygame.image.load(os.path.join('image','dino_power_lie1.png')),pygame.image.load(os.path.join('image','dino_power_lie2.png'))]
dino_power = [pygame.image.load(os.path.join('image','dino_power1.png')),pygame.image.load(os.path.join('image','dino_power2.png')),pygame.image.load(os.path.join('image','dino_power3.png')),pygame.image.load(os.path.join('image','dino_power4.png'))]
dino_gun = [pygame.image.load(os.path.join('image','dino_gun1.png')),pygame.image.load(os.path.join('image','dino_gun2.png')),pygame.image.load(os.path.join('image','dino_gun3.png')),pygame.image.load(os.path.join('image','dino_gun4.png'))]
dino_gun_night = [pygame.image.load(os.path.join('image','dino_gun1_night.png')),pygame.image.load(os.path.join('image','dino_gun2_night.png')),pygame.image.load(os.path.join('image','dino_gun3_night.png')),pygame.image.load(os.path.join('image','dino_gun4_night.png'))]
class Dino():
	def __init__(self,x,y,width,height,choice,jump = False,islie = False,ispower = False,isnight= False):
		self.x = x 
		self.y = y 
		self.width = width 
		self.height = height
		self.walk_count = 0
		self.walk_lie = 0
		self.jump = jump
		self.dot = 0.50
		self.jump_count = 8
		self.islie = islie
		self.ispower = ispower
		self.choice = choice
		self.isnight = isnight
		self.dino = DINO
		self.dino_lie = dino_lie
		self.dino_gun = dino_gun
		self.hit = pygame.Rect(self.x,self.y,self.width,self.height)

	def draw_dino(self,win):
		
		
		if self.jump:
			if self.jump_count >= -8:
				self.y -=(self.jump_count * abs(self.jump_count)) * self.dot
				self.jump_count -=1
			else:
				self.jump_count = 8
				self.jump = False
		if not self.islie:
			if not self.isnight:
				self.dino = DINO
			else:
				self.dino = DINO_NIGHT
			if not self.ispower:
				if self.walk_count + 1 >=4:
					self.walk_count = 0
				self.hit = win.blit(pygame.transform.scale(self.dino[self.walk_count],(self.width,self.height)),(self.x,self.y+5))
				self.dino_rect = self.dino[self.walk_count].get_rect()
				self.walk_count +=1
			else:
				if self.choice == 0:
			
					if self.walk_count + 1 >=4:
						self.walk_count = 0
					self.hit = win.blit(pygame.transform.scale(dino_power[self.walk_count],(self.width,self.height)),(self.x,self.y+5))
					self.walk_count +=1
				else:
					if not self.isnight:
						self.dino_gun = dino_gun
					else:
						self.dino_gun = dino_gun_night

					if self.walk_count + 1 >=4:
						self.walk_count = 0
					self.hit = win.blit(pygame.transform.scale(self.dino_gun[self.walk_count],(self.width + 13,self.height)),(self.x,self.y+5))
					self.walk_count +=1



		else:
			if not self.isnight:
				self.dino_lie = dino_lie
			else:
				self.dino_lie = dino_lie_night
			if not self.ispower:
				if self.walk_lie + 1 >2:
					self.walk_lie = 0
				self.hit = win.blit(pygame.transform.scale(self.dino_lie[self.walk_lie],(50,35)),(self.x,self.y+20))
				self.dino_rect = self.dino_lie[self.walk_lie].get_rect
				self.walk_lie +=1
			else:
				if self.walk_lie + 1 >2:
					self.walk_lie = 0
				self.hit = win.blit(pygame.transform.scale(dino_power_lie[self.walk_lie],(50,35)),(self.x,self.y+20))
				self.walk_lie +=1



		
