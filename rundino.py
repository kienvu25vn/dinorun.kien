import pygame
import os
import sys
pygame.init()
pygame.font.init()
pygame.mixer.init()
import random

win = pygame.display.set_mode((600,300))
score_font = pygame.font.SysFont('comicsans',20)
game_font = pygame.font.SysFont('comicsans',40)

pygame.display.set_caption("Dinorun")
clock = pygame.time.Clock()
bg = pygame.image.load(os.path.join('image','background.jpg'))
bg1 = pygame.image.load(os.path.join('image','background.jpg'))
tree = pygame.image.load(os.path.join('image','tree.png'))
dino = [pygame.image.load(os.path.join('image','rex1.png')),pygame.image.load(os.path.join('image','rex2.png')),pygame.image.load(os.path.join('image','rex3.png')),pygame.image.load(os.path.join('image','rex4.png'))]
dinofire = [pygame.image.load(os.path.join('image','trex1.png')),pygame.image.load(os.path.join('image','trex2.png')),pygame.image.load(os.path.join('image','trex3.png')),pygame.image.load(os.path.join('image','trex4.png'))]
dino_lie = [pygame.image.load(os.path.join('image','rexlie1.png')),pygame.image.load(os.path.join('image','rexlie2.png'))]
item = pygame.image.load(os.path.join('image','item.png'))
bird = pygame.image.load(os.path.join('image','bird.png'))
jump_sound = pygame.mixer.Sound(os.path.join('music','tick.wav'))
pass_sound = pygame.mixer.Sound(os.path.join('music','te.wav'))
dead_sound = pygame.mixer.Sound(os.path.join('music','death.mp3'))
collect_sound = pygame.mixer.Sound(os.path.join('music','collect.mp3'))
sword_sound = pygame.mixer.Sound(os.path.join('music','sword.wav'))
gameover = game_font.render("Game over",1,(0,0,0))
button1 = pygame.transform.scale(pygame.image.load(os.path.join('image','start1.png')),(40,40))
button2 = pygame.transform.scale(pygame.image.load(os.path.join('image','start2.png')),(40,40))
dino_start = pygame.transform.scale(pygame.image.load(os.path.join('image','rex5.png')),(50,50))

def draw_win(high_score,x,y,islie):
	win.blit(gameover,(300-gameover.get_width()//2,150-gameover.get_height()//2))
	highscore = score_font.render("Highscore: "+str(high_score),1,(0,0,0))
	win.blit(highscore,(300-highscore.get_width()//2,150-highscore.get_height()//2+gameover.get_height()//2+20))
	if not islie:
		win.blit(dino_start,(x,y))

	pygame.display.update()
	dead_sound.play()
	run =True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run=False
				pygame.quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				pre_main()

def main():
	run = True
	X =0
	Y= 0
	score = 0
	walk_count = 0
	jump_count =8
	run= True
	jump = False
	x=50
	y=220
	islie = False
	x_co =1
	plus=1
	vel = 10
	high_score = 0
	y_bird = 200
	x_bird = 150
	dot =0.5
	items = []
	DINO = dino[0].get_rect()
	DINOLIE =dino_lie[0].get_rect()
	weapon = False
	count =0
	xf = 1
	fire = False
	boolhit=False
	hit =0 
	x_item = 590
	y_item =120
	COUNT = 0
    
	while run:
		clock.tick(15)
		score +=1
		if score %50==0:
			
			vel +=2
		if score % 100 ==0:
			pass_sound.play()

		score_text = score_font.render("Score: "+ str(score),1,(0,0,0))

   
		win.blit(bg,(X,Y))
		win.blit(bg1,(X+600,Y))
		win.blit(score_text,(520,10))
		BIRD= win.blit(pygame.transform.scale(bird,(40,25)),(X+600+x_bird,y_bird))
		if not weapon:
			pygame.draw.circle(win,(255,0,0),(500,15),6)
		else:
			pygame.draw.circle(win,(0,255,0),(500,15),6)



		

		if x_co ==4:
			plus = random.randint(-1,1)
			x_co =random.randint(1,4)


		for i in range(x_co):
			if i %2 !=0 :

			
				Tree = win.blit(pygame.transform.scale(tree,(20,40 + i*10*plus)),(X+600  + (i+1)*25,230 - i*10*plus))
			else:
				Tree = win.blit(pygame.transform.scale(tree,(20,40 )),(X+600  + (i+1)*25,230 ))

		


		if not islie:
			if not weapon or fire == False:
				if walk_count + 1 >=4:
					walk_count=0
				DINO=win.blit(pygame.transform.scale(dino[walk_count],(50,50)),(x,y+5))
				if DINO.colliderect(Tree) or DINO.colliderect(BIRD):
					if score >= high_score :
						high_score = score


					draw_win(high_score,x,y+5,islie)
		
				walk_count+=1
			if weapon and fire ==  True:
				
				if count +1>=4:
					count=0
				DINOFIRE=win.blit(pygame.transform.scale(dinofire[count],(50,50)),(x,y))
				sword_sound.play()
				count+=1

				if DINOFIRE.colliderect(Tree) :
					if x > (X+600+tree.get_width()*x_co+5):
						weapon=False
				elif DINOFIRE.colliderect(BIRD):
					if x > (X+600+40+10):
						weapon=False
							
				

					
			
		else:
			
			if COUNT + 1 ==2:
				COUNT =0
			DINOLIE = win.blit(pygame.transform.scale(dino_lie[COUNT],(50,35)),(x,y+20))
			COUNT+=1
			if DINOLIE.colliderect(Tree) or DINOLIE.colliderect(BIRD):
				if score >= high_score :
					high_score = score


				draw_win(high_score,x,y+5,islie)
			
		 
		
		if not boolhit and hit % 2 ==0:
			IT=win.blit(pygame.transform.scale(item,(30,30)),(X+x_item,y_item))
			if IT.colliderect(DINO) or IT.colliderect(DINOLIE):
				collect_sound.play()
				boolhit = True
				weapon = True


		if X<= - 750:
			x_co +=1
			X=0
			y_bird = random.randint(50,250)
			
					
			hit = random.randint(1,3)
			boolhit = False
		 
		X -= vel
		if jump:
			if jump_count >= -8:
				y -=(jump_count * abs(jump_count)) * dot
				jump_count -=1
			else:
				jump_count = 8
				jump = False

		
		

		
    
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run=False
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					jump_sound.play()
					if y == 220:
						jump = True
				if event.key == pygame.K_f:
					fire = True

			if event.type == pygame.KEYUP:
				if event.key== pygame.K_f:
					fire = False
				if event.key == pygame.K_DOWN:
					islie=False

		keys = pygame.key.get_pressed()

		if keys[pygame.K_DOWN]:
			islie = True
		



		

		pygame.display.update()
def pre_main():
	x=random.randint(0,100)
	y=x
	speedx=1
	speedy=1
	radius = 0
	running = True
	while running:
		clock.tick(15)
		win.blit(bg,(0,0))
		win.blit(pygame.transform.rotate(dino_start,radius),(x,y))
		BUT = win.blit(button1,(300 - button1.get_width()//2,150-button1.get_height()//2))
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

			
		if BUT.collidepoint(pygame.mouse.get_pos()):
			BUT = win.blit(button2,(300 - button2.get_width()//2,150-button2.get_height()//2))
			if pygame.mouse.get_pressed()[0]:
				main()




		pygame.display.update()





pre_main()

			

 


