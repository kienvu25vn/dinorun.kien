
#import khoi tao thu vien
import pygame 
import os
import sys
import random
from background import back_ground
from item import Item
from Bullet import bullet
from Dino import Dino
from tree import Tree
from bird import Bird
pygame.init()
pygame.font.init()
pygame.mixer.init()
clock = pygame.time.Clock()
################################################################
win = pygame.display.set_mode((600,300))                             # Set man hinh display
pygame.display.set_caption("DINORUN BY D19PTIT")				 	 # Set caption cho game

#Khoi tao background , am thanh , Font , button cho game.
jump_sound = pygame.mixer.Sound(os.path.join('music','tick.wav'))
pass_sound = pygame.mixer.Sound(os.path.join('music','te.wav'))
dead_sound = pygame.mixer.Sound(os.path.join('music','death.mp3'))
lazer_sound = pygame.mixer.Sound(os.path.join('music','laze.mp3'))
collect_sound = pygame.mixer.Sound(os.path.join('music','item.mp3'))
click_sound = pygame.mixer.Sound(os.path.join('music','click.mp3'))
bg1 = pygame.image.load(os.path.join('image','background.jpg'))
guide_bg = pygame.image.load(os.path.join('image','guide_bg.jpg'))
score_font = pygame.font.Font("Font.ttf",10)
highscore_font = pygame.font.Font("Font.ttf",25)
text_guide = pygame.font.Font("Font.ttf",6)
dino_start = pygame.transform.scale(pygame.image.load(os.path.join('image','rex5.png')),(50,50))
dino_start_night = pygame.transform.scale(pygame.image.load(os.path.join('image','b5.png')),(50,50))
button1 = pygame.transform.scale(pygame.image.load(os.path.join('image','play_button.png')),(40,40))
button2 = pygame.transform.scale(pygame.image.load(os.path.join('image','guide_button.png')),(40,40))
back_button = pygame.transform.scale(pygame.image.load(os.path.join('image','button_back.png')),(40,40))
##########################################################################################################
def Score_text(x):    #Ham dinh dang highscore
	s = str(x)
	while(len(s)<5):
		s = "0" + s
	return s	


def draw_win(score,x,y,islie,isnight): #Ham ve giao dien khi gameover
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
		if pygame.mouse.get_pressed()[2]: #Click chuot phai de ve man hinh cho
				click_sound.play()
				pre_main()
		if pygame.mouse.get_pressed()[0]: #Click chuot trai de choi lai
				click_sound.play()
				main()



def draw_time_power(x,y,width,height,count,time):  							#Ham ve thoi gian su dung item cho khung long
	pygame.draw.rect(win,(255,0,0),(x,y,width,height))
	pygame.draw.rect(win,(0,255,0),(x,y,width-(width//time)*count,height))
	



def main():   																#Ham chinh cua chuong trinh
	#Khoi tao cac bien
	run = True    
	tick = 0
	istick = False
	count = 0
	vel = 10
	bird_x = 800
	score = 0
	x_score = 550
	fire = False

	#Khoi tao cac gia tri cho cac Sprites
	BG1 = back_ground(0,0)
	BG2 = back_ground(600,0)
	BG3 = back_ground(1200,0)
	ITEM = Item(750,220,random.randrange(0,2))
	dino = Dino(50,220,50,50,ITEM.choice)
	TREE = Tree(600,230,20,40,2)
	BIRD = Bird(900,240,40,25)

	#Doc file highscore lay du lieu!
	fb = open("highscore.txt",'r+')
	high_score = int(fb.read().strip())
	fb.close()

	#Vong lap chinh
	while run:
		clock.tick(15)	#Dat fps cho game: 15fps

		if not dino.isnight:	#Khoi tao font chu cho giao dien gameover!
			score_text = score_font.render(Score_text(score),1,(0,0,0))
			high_score_text = score_font.render("HI "+Score_text(high_score),1,(0,0,0))
		else:
			score_text = score_font.render(Score_text(score),1,(255,255,255))
			high_score_text = score_font.render("HI "+Score_text(high_score),1,(255,255,255))
	
		# Tao giao dien background chuyen dong!
		BG2.x = BG1.x + 600
		BG3.x = BG1.x + 1200
		BG1.draw_bg(win)
		BG2.draw_bg(win)
		BG3.draw_bg(win)

		# Ve cac Sprites len man hinh
		TREE.draw_tree(win)
		BIRD.draw_bird(win)
		ITEM.draw_item(win)
		dino.draw_dino(win)

		# Tao chuyen dong cho Sprites
		BG1.x-=vel
		TREE.x -=vel
		BIRD.x -=vel
		ITEM.x -= vel

		#Xu li toc do game , chuyen trang thai ban ngay va ban dem !
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
			BIRD.isnight = True
		if score %500 ==0 and (score//500)%2==0:
			BG1.isnight = False
			BG2.isnight = False
			BG3.isnight = False
			dino.isnight = False
			TREE.isnight = False
			BIRD.isnight = False

		
		#Xu ly su kien trong game:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: 	 		#Khi nguoi dung click QUIT , ghi de du lieu highscore la 0 va dong game!
				fb = open("highscore.txt",'w')
				fb.write('0')
				fb.close()
				run= False
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:		#Xu ly su kien KEYDOWN
				if event.key == pygame.K_SPACE:     #Khung long nhay
					jump_sound.play()
					dino.jump = True
				if event.key == pygame.K_DOWN :		#Khung long nam
					if dino.choice == 1 and dino.ispower:
						dino.islie = False
					else:
						dino.islie = True
				if event.key == pygame.K_f and dino.choice == 1 and dino.ispower: #Khi khung long su dung vu khi
					lazer_sound.play()
					fire = True
			if event.type == pygame.KEYUP: 			#Xu ly su kien KEYUP
				if event.key == pygame.K_DOWN:		#Khung long  chuyen ve trang thai dung
					dino.islie = False
				if event.key == pygame.K_f:			#Khung long dung su dung vu khi
					fire = False
				if not dino.ispower:
					fire = False
		

		#Xu ly va cham giua cac Sprites
		
		if (dino.hit.colliderect(TREE.hit) or dino.hit.colliderect(BIRD.hit)) and not dino.ispower  and not TREE.isfired and not BIRD.isfired:
			dead_sound.play()
			if high_score < score:
				high_score = score
			fb = open("highscore.txt",'w+')
			fb.write(str(high_score))
			fb.close()
			draw_win(score,dino.x,dino.y+5,dino.islie,BG1.isnight)

		if dino.hit.colliderect(ITEM.hit) and ITEM.isappear == True:
			collect_sound.play()
			dino.ispower = True
			istick = True
			ITEM.isappear = False

		#Xu ly thoi gian su dung item cua khung long
		if istick :
			tick+=1
			if tick % 15 ==0:
				count+=1
			draw_time_power(dino.x,dino.y - 5,dino.width,5,count,5)
			if tick //15 == 5:
				dino.ispower = False
				fire = False
				tick = 0
				count =0
				istick = False
		
		#Xu ly khi khung long nhat duoc item vu khi
		if fire:
			weapon = bullet(dino.x + dino.hit[2],dino.y + dino.hit[3]//2 + 4,600-dino.x,2)
			weapon.draw_bullet(win)
			if weapon.hit.colliderect(TREE.hit) :
				TREE.isfired = True
			if  weapon.hit.colliderect(BIRD.hit):
				BIRD.isfired = True
		
		#Khoi tao lai cac gia tri cua Sprites , background tao vong lap cho game!
		if BG1.x <= -(bird_x + BIRD.width):
			BG1.x=0
			TREE.x = 600
			BIRD.x = random.randrange(800,900)
			BIRD.y = random.randrange(190,240)
			ITEM.x = random.randrange(710,760)
			ITEM.y = random.randrange(150,220)
			isappear = random.randrange(1,3)
			bird_x = BIRD.x
			TREE.dot = random.randint(-1,1)
			TREE.numOftree = random.randint(1,3)
			TREE.isfired = False
			BIRD.isfired = False

			if isappear == 1 and not istick :
				ITEM.isappear = True
				ITEM.choice = random.randrange(0,2)
				if ITEM.choice == 0:
					dino.choice = 0
				else:
					dino.choice =1 
			else:
				ITEM.isappear = False
			      
			
		#Ve highscore len giao dien Gameover!
		win.blit(score_text,(600-score_text.get_width()-10,10))
		if high_score > 0:
			win.blit(high_score_text,(600-score_text.get_width()-25 - high_score_text.get_width(),10))

		pygame.display.update()	#Cap nhat lai giao dien game

##########################################################################################
def pre_main(): 				#Ham xu ly man hinh cho cua game!
	#Khoi tao cac bien
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

		#Xu ly thao tac nguoi choi!
			
		if BUT.collidepoint(pygame.mouse.get_pos()):
			
			if pygame.mouse.get_pressed()[0]:
				click_sound.play()
				main()
		if Guide_but.collidepoint(pygame.mouse.get_pos()):
			
			if pygame.mouse.get_pressed()[0]:
				click_sound.play()
				guide_main()


		pygame.display.update()

##############################################################################

def guide_main(): #Ham xu ly menu guide
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
				click_sound.play()
				pre_main()
		pygame.display.update()


pre_main() # Goi ham man hinh cho

