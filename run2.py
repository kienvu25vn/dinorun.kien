import pygame 
import os
import sys
import random

pygame.init()
pygame.font.init()
pygame.mixer.init()
win = pygame.display.set_mode((600,300))
jump_sound = pygame.mixer.Sound(os.path.join('music','tick.wav'))
pass_sound = pygame.mixer.Sound(os.path.join('music','te.wav'))
dead_sound = pygame.mixer.Sound(os.path.join('music','death.mp3'))
lazer_sound = pygame.mixer.Sound(os.path.join('music','laze.mp3'))
bg = pygame.image.load(os.path.join('image','background.jpg'))
bg1 = pygame.image.load(os.path.join('image','background.jpg'))
tree = pygame.image.load(os.path.join('image','tree.png'))
tree_cut = pygame.image.load(os.path.join('image','tree1.png'))
bird = pygame.image.load(os.path.join('image','bird.png'))
bird_cut = pygame.image.load(os.path.join('image','bird_cut.png'))
DINO = [pygame.image.load(os.path.join('image','rex1.png')),pygame.image.load(os.path.join('image','rex2.png')),pygame.image.load(os.path.join('image','rex3.png')),pygame.image.load(os.path.join('image','rex4.png'))]
dino_lie = [pygame.image.load(os.path.join('image','rexlie1.png')),pygame.image.load(os.path.join('image','rexlie2.png'))]
dino_power_lie = [pygame.image.load(os.path.join('image','dino_power_lie1.png')),pygame.image.load(os.path.join('image','dino_power_lie2.png'))]
dino_power = [pygame.image.load(os.path.join('image','dino_power1.png')),pygame.image.load(os.path.join('image','dino_power2.png')),pygame.image.load(os.path.join('image','dino_power3.png')),pygame.image.load(os.path.join('image','dino_power4.png'))]
item = [pygame.transform.scale(pygame.image.load(os.path.join('image','collect.png')),(20,20)),pygame.transform.scale(pygame.image.load(os.path.join('image','gun.png')),(25,15))]
dino_gun = [pygame.image.load(os.path.join('image','dino_gun1.png')),pygame.image.load(os.path.join('image','dino_gun2.png')),pygame.image.load(os.path.join('image','dino_gun3.png')),pygame.image.load(os.path.join('image','dino_gun4.png'))]
clock = pygame.time.Clock()
score_font = pygame.font.Font("Font.ttf",10)
highscore_font = pygame.font.Font("Font.ttf",25)
dino_start = pygame.transform.scale(pygame.image.load(os.path.join('image','rex5.png')),(50,50))

class Dino():
	def __init__(self,x,y,width,height,jump = False,islie = False,ispower = False):
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
		self.choice = 1
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
			if not self.ispower:
				if self.walk_count + 1 >=4:
					self.walk_count = 0
				self.hit = win.blit(pygame.transform.scale(DINO[self.walk_count],(self.width,self.height)),(self.x,self.y+5))
				self.dino_rect = DINO[self.walk_count].get_rect()
				self.walk_count +=1
			else:
				if self.choice == 0:
			
					if self.walk_count + 1 >=4:
						self.walk_count = 0
					self.hit = win.blit(pygame.transform.scale(dino_power[self.walk_count],(self.width,self.height)),(self.x,self.y+5))
					self.walk_count +=1
				else:
					if self.walk_count + 1 >=4:
						self.walk_count = 0
					self.hit = win.blit(pygame.transform.scale(dino_gun[self.walk_count],(self.width + 13,self.height)),(self.x,self.y+5))
					self.walk_count +=1



		else:
			if not self.ispower:
				if self.walk_lie + 1 >2:
					self.walk_lie = 0
				self.hit = win.blit(pygame.transform.scale(dino_lie[self.walk_lie],(50,35)),(self.x,self.y+20))
				self.dino_rect = dino_lie[self.walk_lie].get_rect
				self.walk_lie +=1
			else:
				if self.walk_lie + 1 >2:
					self.walk_lie = 0
				self.hit = win.blit(pygame.transform.scale(dino_power_lie[self.walk_lie],(50,35)),(self.x,self.y+20))
				self.walk_lie +=1



		

class Tree():
	def __init__(self,x,y,width,height,numOftree,isfired=False):
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
	def draw_tree(self,win):
		if not self.isfired:
			self.tree = tree
		else:
			self.tree = tree_cut
		for i in range(self.numOftree):
			if i %2 !=0 :

				self.hit = win.blit(pygame.transform.scale(self.tree,(self.width,self.height + i*10*self.dot)),(self.x + (i+1)*25,self.y - i*10*self.dot))
				self.hitbox = (self.x + (i+1)*25,self.y-10*i*self.dot,self.width,self.height + i*10*self.dot)
				
			else:
				self.hit = win.blit(pygame.transform.scale(self.tree,(self.width,self.height )),(self.x  + (i+1)*25,self.y ))
				self.hitbox = (self.x +(i+1)*25,self.y,self.width,self.height)
				


class Bird():
	def __init__(self,x,y,width,height,isfired = False):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.hit = pygame.Rect(self.x,self.y,self.width,self.height)
		self.bird = bird
		self.isfired = isfired
	def draw_bird(self,win):
		if not self.isfired:
			self.bird = bird
		else:
			self.bird = bird_cut
		self.hit = win.blit(pygame.transform.scale(self.bird,(self.width,self.height)),(self.x,self.y))




def Score_text(x):
	s = str(x)
	while(len(s)<5):
		s = "0" + s
	return s	


def draw_win(score,x,y,islie):
	high_score = highscore_font.render("GameOver" ,1,(0,0,0))
	win.blit(high_score,((600- high_score.get_width())//2,(300-high_score.get_height())//2))
	if not islie:
		win.blit(pygame.transform.scale(dino_start,(50,50)),(x,y))
	pygame.display.update()

	running = True
	while running:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fb = open("highscore.txt",'w')
				fb.write('0')
				fb.close()
				running = False
				pygame.quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				main()
def draw_time_power(x,y,count,time):
	
	pygame.draw.rect(win,(255,0,0),(x,y,20,10))
	pygame.draw.rect(win,(0,255,0),(x,y,20-(20//time)*count,10))
	




class Item():
	def __init__(self,x,y,isappear=True):
		self.x = x
		self.y = y
		self.isappear = isappear
		self.hit = pygame.Rect(self.x,self.y,20,20)
		self.choice = 1
	def draw_item(self,win):
		if self.isappear :
		
			self.hit=win.blit(item[self.choice],(self.x,self.y))
		
class bullet():
	def __init__(self,x,y,width,height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.hit = pygame.Rect(self.x,self.y,self.width,self.height)
	def draw_bullet(self,win):
		pygame.draw.rect(win,(255,0,0),(self.x,self.y,self.width,self.height))


def main():
	
	run = True 
	dino = Dino(50,220,50,50)
	tick = 0
	tick1 = 0
	istick = False
	count = 0
	X = 0
	Y = 0
	vel = 10
	TREE = Tree(600,230,20,40,2)
	BIRD = Bird(900,240,40,25)
	bird_x = 800
	score = 0
	ITEM = Item(750,220)
	x_score = 550
	fb = open("highscore.txt",'r+')
	high_score = int(fb.read().strip())
	fb.close()
	fire = False

	while run:
		score_text = score_font.render(Score_text(score),1,(0,0,0))
		high_score_text = score_font.render("HI "+Score_text(high_score),1,(0,0,0))
		clock.tick(15)
		win.blit(bg,(X,Y))
		
		
		win.blit(bg1,(X+600,Y))
		win.blit(bg,(X+1200,Y))
		score+=1
		if score % 100 ==0:
			vel +=1
			pass_sound.play()

		
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fb = open("highscore.txt",'w')
				fb.write('0')
				fb.close()
				run= False
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					jump_sound.play()
					dino.jump = True
				if event.key == pygame.K_DOWN :
					if dino.choice == 1 and dino.ispower:
						dino.islie = False
					else:
						dino.islie = True
					
				if event.key == pygame.K_f and dino.choice == 1 and dino.ispower:
					lazer_sound.play()
					fire = True
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_DOWN:
					dino.islie = False
				if event.key == pygame.K_f:
					fire = False
		

		if fire:
			weapon = bullet(dino.x + dino.hit[2],dino.y + dino.hit[3]//2 + 4,600-dino.x,2)
			weapon.draw_bullet(win)
			if weapon.hit.colliderect(TREE.hit) :
				TREE.isfired = True
			if  weapon.hit.colliderect(BIRD.hit):
				BIRD.isfired = True




		
		TREE.draw_tree(win)
		BIRD.draw_bird(win)
		ITEM.draw_item(win)
		dino.draw_dino(win)
		
		if (dino.hit.colliderect(TREE.hit) or dino.hit.colliderect(BIRD.hit)) and not dino.ispower:
			dead_sound.play()
			if high_score < score:
				high_score = score
			fb = open("highscore.txt",'w+')
			fb.write(str(high_score))
			fb.close()


			draw_win(score,dino.x,dino.y+5,dino.islie)
		if istick :

			tick+=1
			if tick % 15 ==0:
				count+=1
			draw_time_power(400,10,count,5)
			if tick //15 == 5:
				dino.ispower = False
				tick = 0
				count =0
				istick = False
		
		if dino.hit.colliderect(ITEM.hit) and ITEM.isappear == True:
			dino.ispower = True
			istick = True
			ITEM.isappear = False
		
			
			
			
			
		
		if X <=-(bird_x + BIRD.width):
			
			X=0
			TREE.x = 600
			BIRD.x = random.randrange(800,900)
			BIRD.y = random.randrange(190,240)
			bird_x = BIRD.x
			ITEM.x = 750
			isappear = random.randrange(1,3)
			
			if isappear == 1 and not istick :
				ITEM.isappear = True
				ITEM.choice = random.randrange(0,2)
				print(ITEM.choice)
				if ITEM.choice == 0:
					dino.choice = 0
				else:
					dino.choice =1 

			else:
				ITEM.isappear = False
			      
			TREE.dot = random.randint(-1,1)
			
			TREE.numOftree = random.randint(1,3)
			TREE.isfired = False
			BIRD.isfired = False
			
		
		X-=vel
		TREE.x -=vel
		BIRD.x -=vel
		ITEM.x -= vel
		win.blit(score_text,(600-score_text.get_width()-10,10))
		win.blit(high_score_text,(600-score_text.get_width()-25 - high_score_text.get_width(),10))
		pygame.display.update()
main()

