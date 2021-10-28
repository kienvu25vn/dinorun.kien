
import pygame 
import os
import sys
import random
from background import back_ground
from item import Item
from Bullet import bullet
pygame.init()
pygame.font.init()
pygame.mixer.init()
win = pygame.display.set_mode((600,300))
jump_sound = pygame.mixer.Sound(os.path.join('music','tick.wav'))
pass_sound = pygame.mixer.Sound(os.path.join('music','te.wav'))
dead_sound = pygame.mixer.Sound(os.path.join('music','death.mp3'))
lazer_sound = pygame.mixer.Sound(os.path.join('music','laze.mp3'))
# bg = pygame.image.load(os.path.join('image','background.jpg'))
bg1 = pygame.image.load(os.path.join('image','background.jpg'))
guide_bg = pygame.image.load(os.path.join('image','guide_bg.jpg'))
# night_bg = pygame.image.load(os.path.join('image','night_bg.png'))
tree = pygame.image.load(os.path.join('image','tree.png'))
tree_night = pygame.image.load(os.path.join('image','tree_night.png'))
tree_cut = pygame.image.load(os.path.join('image','tree1.png'))
bird = pygame.image.load(os.path.join('image','bird.png'))
bird_cut = pygame.image.load(os.path.join('image','bird_cut.png'))
DINO = [pygame.image.load(os.path.join('image','rex1.png')),pygame.image.load(os.path.join('image','rex2.png')),pygame.image.load(os.path.join('image','rex3.png')),pygame.image.load(os.path.join('image','rex4.png'))]
DINO_NIGHT = [pygame.image.load(os.path.join('image','b1.png')),pygame.image.load(os.path.join('image','b2.png')),pygame.image.load(os.path.join('image','b3.png')),pygame.image.load(os.path.join('image','b4.png'))]
dino_lie = [pygame.image.load(os.path.join('image','rexlie1.png')),pygame.image.load(os.path.join('image','rexlie2.png'))]
dino_lie_night = [pygame.image.load(os.path.join('image','a1.png')),pygame.image.load(os.path.join('image','a2.png'))]
dino_power_lie = [pygame.image.load(os.path.join('image','dino_power_lie1.png')),pygame.image.load(os.path.join('image','dino_power_lie2.png'))]
dino_power = [pygame.image.load(os.path.join('image','dino_power1.png')),pygame.image.load(os.path.join('image','dino_power2.png')),pygame.image.load(os.path.join('image','dino_power3.png')),pygame.image.load(os.path.join('image','dino_power4.png'))]
# item = [pygame.transform.scale(pygame.image.load(os.path.join('image','collect.png')),(20,20)),pygame.transform.scale(pygame.image.load(os.path.join('image','gun.png')),(25,15))]
dino_gun = [pygame.image.load(os.path.join('image','dino_gun1.png')),pygame.image.load(os.path.join('image','dino_gun2.png')),pygame.image.load(os.path.join('image','dino_gun3.png')),pygame.image.load(os.path.join('image','dino_gun4.png'))]
dino_gun_night = [pygame.image.load(os.path.join('image','dino_gun1_night.png')),pygame.image.load(os.path.join('image','dino_gun2_night.png')),pygame.image.load(os.path.join('image','dino_gun3_night.png')),pygame.image.load(os.path.join('image','dino_gun4_night.png'))]

clock = pygame.time.Clock()
score_font = pygame.font.Font("Font.ttf",10)
highscore_font = pygame.font.Font("Font.ttf",25)
text_guide = pygame.font.Font("Font.ttf",6)
dino_start = pygame.transform.scale(pygame.image.load(os.path.join('image','rex5.png')),(50,50))
dino_start_night = pygame.transform.scale(pygame.image.load(os.path.join('image','b5.png')),(50,50))
button1 = pygame.transform.scale(pygame.image.load(os.path.join('image','play_button.png')),(40,40))
button2 = pygame.transform.scale(pygame.image.load(os.path.join('image','guide_button.png')),(40,40))
back_button = pygame.transform.scale(pygame.image.load(os.path.join('image','button_back.png')),(40,40))
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


# class Item():
# 	def __init__(self,x,y,choice,isappear=True):
# 		self.x = x
# 		self.y = y
# 		self.isappear = isappear
# 		self.hit = pygame.Rect(self.x,self.y,20,20)
# 		self.choice = choice
# 	def draw_item(self,win):
# 		if self.isappear :
		
# 			self.hit=win.blit(item[self.choice],(self.x,self.y))
		
# class bullet():
# 	def __init__(self,x,y,width,height):
# 		self.x = x
# 		self.y = y
# 		self.width = width
# 		self.height = height
# 		self.hit = pygame.Rect(self.x,self.y,self.width,self.height)
# 	def draw_bullet(self,win):
# 		pygame.draw.rect(win,(255,0,0),(self.x,self.y,self.width,self.height))
# class back_ground():
# 	def __init__(self,x,y,isnight = False):
# 		self.x = x
# 		self.y = y
# 		self.isnight = isnight
# 		self.bg = bg
# 	def draw_bg(self,win):
# 		if not self.isnight:
# 			self.bg = bg
# 		else:
# 			self.bg = night_bg
# 		win.blit(self.bg,(self.x,self.y))
def Score_text(x):
	s = str(x)
	while(len(s)<5):
		s = "0" + s
	return s	


def draw_win(score,x,y,islie,isnight):
	if not isnight:
		high_score = highscore_font.render("GameOver" ,1,(0,0,0))
	else:
		high_score = highscore_font.render("GameOver" ,1,(255,255,255))
	win.blit(high_score,((600- high_score.get_width())//2,(300-high_score.get_height())//2))
	if not islie:
		if not isnight:
			win.blit(pygame.transform.scale(dino_start,(50,50)),(x,y))
		else:
			win.blit(pygame.transform.scale(dino_start_night,(50,50)),(x,y))
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
				sys.exit()
		if pygame.mouse.get_pressed()[2]:
				pre_main()
		if pygame.mouse.get_pressed()[0]:
				main()
def draw_time_power(x,y,count,time):
	
	pygame.draw.rect(win,(255,0,0),(x,y,20,10))
	pygame.draw.rect(win,(0,255,0),(x,y,20-(20//time)*count,10))
	



def main():
	
	run = True 
	tick = 0
	istick = False
	count = 0
	vel = 10
	BG1 = back_ground(0,0)
	BG2 = back_ground(600,0)
	BG3 = back_ground(1200,0)
	TREE = Tree(600,230,20,40,2)
	BIRD = Bird(900,240,40,25)
	bird_x = 800
	score = 0
	ITEM = Item(750,220,random.randrange(0,2))
	dino = Dino(50,220,50,50,ITEM.choice)
	x_score = 550
	fb = open("highscore.txt",'r+')
	high_score = int(fb.read().strip())
	fb.close()
	fire = False

	while run:
		if not dino.isnight:
			score_text = score_font.render(Score_text(score),1,(0,0,0))
			high_score_text = score_font.render("HI "+Score_text(high_score),1,(0,0,0))
		else:
			score_text = score_font.render(Score_text(score),1,(255,255,255))
			high_score_text = score_font.render("HI "+Score_text(high_score),1,(255,255,255))
		clock.tick(15)
		
		BG2.x = BG1.x + 600
		BG3.x = BG1.x + 1200
		BG1.draw_bg(win)
		BG2.draw_bg(win)
		BG3.draw_bg(win)
		score+=1
		if score % 100 ==0:
			vel+=1
			pass_sound.play()
		if score %500 ==0 and (score//500)%2==1:
			BG1.isnight = True
			BG2.isnight = True
			BG3.isnight = True
			dino.isnight = True
			TREE.isnight = True
		if score %500 ==0 and (score//500)%2==0:
			BG1.isnight = False
			BG2.isnight = False
			BG3.isnight = False
			dino.isnight = False
			TREE.isnight = False

		
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fb = open("highscore.txt",'w')
				fb.write('0')
				fb.close()
				run= False
				pygame.quit()
				sys.exit()
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
				if event.key == pygame.K_f or not dino.ispower:
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
		
		if (dino.hit.colliderect(TREE.hit) or dino.hit.colliderect(BIRD.hit)) and not dino.ispower  and not TREE.isfired and not BIRD.isfired:
			dead_sound.play()
			if high_score < score:
				high_score = score
			fb = open("highscore.txt",'w+')
			fb.write(str(high_score))
			fb.close()


			draw_win(score,dino.x,dino.y+5,dino.islie,BG1.isnight)
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
		
			
			
			
			
		
		if BG1.x <= -(bird_x + BIRD.width):
			
			BG1.x=0
			TREE.x = 600
			BIRD.x = random.randrange(800,900)
			BIRD.y = random.randrange(190,240)
			bird_x = BIRD.x
			ITEM.x = random.randrange(710,760)
			ITEM.y = random.randrange(150,220)
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
			
		
		BG1.x-=vel
		TREE.x -=vel
		BIRD.x -=vel
		ITEM.x -= vel
		win.blit(score_text,(600-score_text.get_width()-10,10))
		if high_score > 0:
			win.blit(high_score_text,(600-score_text.get_width()-25 - high_score_text.get_width(),10))
		pygame.display.update()
def pre_main():
	x=random.randint(0,100)
	y=0
	speedx=1
	speedy=1
	radius = 0
	running = True
	BG1 = back_ground(0,0)
	while running:
		clock.tick(15)
		BG1.draw_bg(win)
		win.blit(pygame.transform.rotate(dino_start,radius),(x,y))
		BUT = win.blit(button1,(300 - button1.get_width()-5,150-button1.get_height()//2))
		Guide_but = win.blit(button2,(305 ,150 - button2.get_height()//2))
		x+=speedx
		y+=speedy
		radius +=5
		if x<=0 or x + dino_start.get_width()>=600:
			speedx = - speedx
		if y <= 0 or y + dino_start.get_height()>=300:
			speedy = - speedy

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running= False
				pygame.quit()
				sys.exit()

			
		if BUT.collidepoint(pygame.mouse.get_pos()):
			
			if pygame.mouse.get_pressed()[0]:
				main()
		if Guide_but.collidepoint(pygame.mouse.get_pos()):
			
			if pygame.mouse.get_pressed()[0]:
				guide_main()




		pygame.display.update()


def guide_main():
	run = True
	while run:
		win.blit(guide_bg,(0,0))
		back_but = win.blit(back_button,(600-back_button.get_width()-10,10))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				sys.exit()
		if back_but.collidepoint(pygame.mouse.get_pos()):
			
			if pygame.mouse.get_pressed()[0]:
				pre_main()
		pygame.display.update()



pre_main()

