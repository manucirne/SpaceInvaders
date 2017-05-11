#ARRUMAR A POSICAO DO GIF E O TEMPO DE TICK (clock.tick(4))
#COLOCAR ELES NO LUGAR DOS MONSTROS ATUAIS 
#TENTEI ADD MP3 NAO DEU DO MESMO JEITO (mus_inic)
#COLOCAR NAVE MAE NO JOGO -- CONTINUAR (PRECISO COLOCA_LA NO LOOP PRINC)
import pygame , sys
from pygame.locals import *

pygame.init()
pygame.mixer.init()
pygame.font.init()

# def interseccao(s1_x, s1_y, s2_x, s2_y):
# 	return (s1_x > s2_x - 10) and \
# 	       (s1_y > s2_y - 10) and \
# 	       (s1_x < s2_x + 10) and \
# 	       (s1_y < s2_y + 10)


class jogador(pygame.sprite.Sprite):
	def __init__(self,tela,imagem):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(imagem)
	#self.image = pygame.transform.scale(image, (50,50)) #para dimensionar mas nao deu certp
		self.tela = tela


	def posicao(self,x,y,tela):
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.rect.top = 480
		self.rect.left = 350


	def desenha(self,nave_topo,nave_esq):
		self.tela.blit(self.image,(nave_topo,
			                        nave_esq))


class monstros(pygame.sprite.Sprite):
	def __init__(self,tela,imagem):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load(imagem)
		self.tela = tela
		self.passo = 0
		self.direcao = 1
		self.type = 1

	def posicao(self,x,y):
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def desenha(self):
		self.tela.blit(self.image,(self.rect.x,
			                        self.rect.y))


	def update(self):
		if self.passo == 10:
			self.direcao = -1
		elif self.passo == -10:
			self.direcao = 1
		self.passo += self.direcao
		self.rect.x += self.direcao
################### nave mae ############################
class navemae(pygame.sprite.Sprite):
	def __init__(self,tela,imagem):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load(imagem)
		self.tela = tela
		self.passo = 0
		self.direcao = 1
		self.type = 1

	def posicao(self,x,y):
		self.rect = self.image.get_rect() #ta da
		self.rect.x = x
		self.rect.y = y

	def desenha(self):
		self.tela.blit(self.image,(self.rect.x,
			                        self.rect.y))


	def update(self):
		if self.rect.x < 800:
			self.rect.x += 3
		elif self.rect.x >= 800:
			self.rect.x -= 3

########################################################
class shots(pygame.sprite.Sprite):
	def __init__(self,tela,imagem):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load(imagem)
		self.tela = tela

		
	def posicao(self,x,y):
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def desenha(self):
		self.tela.blit(self.image,(self.rect.x,
			                        self.rect.y))
	def update(self):
		self.rect.y -= 10
		if self.rect.y < 0:
			self.kill()



clock = pygame.time.Clock()
tela = pygame.display.set_mode((800,600))
pygame.mouse.set_visible(0)
pygame.display.set_caption("Space invaders - Code Girls")

#importanto imgs 
nave = jogador(tela,"nova_nave.png")
background = pygame.image.load("espaco.jpg")
monstrinho = pygame.image.load('monstrinho.png')
mae = navemae(tela,"nave_mae.png")
tiro = shots(tela, "shot.png")
nave_mae = navemae(tela,"nave_mae.png")
nave_mae.posicao(0,0)
grupo_nave_mae = pygame.sprite.Group()
grupo_nave_mae.add(nave_mae)

#nave_topo = tela.get_height() - nave.get_height()
#nave_esq = tela.get_width()/2 - nave.get_width()/2
nave_topo = 487
nave_esq = 350


# carregando os sound effects

shoot_sound = pygame.mixer.Sound("laser_shoot.wav")

#shoot_sound.play() só colocar no loop princ

myfont = pygame.font.SysFont('Arial', 30)
myfont1 = pygame.font.SysFont('Arial', 100)
fim = myfont1.render('Você venceu!!!!!!', False, (255,255,255))

#TENTANDO COLOCAR O GIF AO INVES DA IMG INICIAL
m1 = pygame.image.load("m1.png")
m4 = pygame.image.load("m3.png")

#FALTA A OUTRAS MUSICAS, ESTA DANDO PAU  

# lista_monstros = []
# for i in range(400,560,40):
# 	for j in range(-300,300,40):
# 		novo_monstro = monstros(tela,"monstrinho.png", j, -i)
# 		lista_monstros.append(novo_monstro)

# tiro = shots(tela, "shot.png")
# tiro2 = shots(tela, "shot.png")
# tiro3 = shots(tela, "shot.png")
# tiro4 = shots(tela, "shot.png")
# tiro5 = shots(tela, "shot.png")
#atirar_y = 0
#atirar_x = 0
#tiros = []

grupo_tiros = pygame.sprite.Group()
tiro = 0
numero = 0
pontos = 0


grupo_monstro = pygame.sprite.Group()
for i in range(170,210,40):
	for j in range(300,400,40):
		#novo_monstro = monstros(tela,"monstrinho.png", j, -i)
		#novo_monstro.desenha()
		novo_monstro = monstros(tela,"monstrinho.png")
		novo_monstro.posicao(j, i)
		grupo_monstro.add(novo_monstro)



#nave mae meio cagada



#ARRUMAR A POSICAO DO GIF E O TEMPO DE TICK (clock.tick(4))
#COLOCAR ELES NO LUGAR DOS MONSTROS ATUAIS 
m1 = pygame.image.load("m1.png")
m2 = pygame.image.load("m3.png")
monstrosCurrentImage = 1


####################################################################################

while True:
	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			sys.exit()
		elif evento.type == MOUSEBUTTONDOWN:
			# tiros.append([event.pos[0],500])
			# for t in tiros:
			tiro = shots(tela, "shot.png")
			tiro.posicao(x,nave_topo)
			grupo_tiros.add(tiro)
			shoot_sound.play()
			grupo_tiros.draw(tela)

			# for b in range(len(tiros)):
			# 	tiros[b][0]-=10

			# for t in tiros:
			# 	if t[0]<0:
			# 		tiros.remove(t)


			#atirar_y = nave_topo
			#atirar_x = x
	
	if (monstrosCurrentImage==1): 
		tela.blit(m1, (100,100)) 

	if (monstrosCurrentImage==2): 
		tela.blit(m2, (100,100))

	if (monstrosCurrentImage==2): 
		monstrosCurrentImage=1

	else: 
		monstrosCurrentImage+=1 
	pygame.display.flip() 
	

#---------------------------------#
	tela.blit(background, (0, 0))

	x,y = pygame.mouse.get_pos()
	nave.posicao(x,y,tela)
	nave.desenha(x-50,nave_topo)
	#tela.blit(nave, (x-nave.get_width()/2,nave_topo))
	#tela.fill([0,0,0])
	
	grupo_nave_mae.draw(tela)
	grupo_monstro.draw(tela)
	grupo_tiros.draw(tela)
					

	#if atirar_y > 0:
		#tela.blit(tiro, (atirar_x,atirar_y))
		#atirar_y -= 15

#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

	col = pygame.sprite.groupcollide(grupo_tiros,grupo_monstro,True,True)
	for i in col:
		pontos += 1
	ponto = myfont.render('Pontuação: {0}'.format(pontos), False, (255,255,255))
	tela.blit(ponto,(10,10))

	colnavemae = pygame.sprite.groupcollide(grupo_tiros,grupo_nave_mae,True,True)

	#print(pontos)

	# for monstro in monstros_atingidos:
	# 	grupo_monstro.kill(novo_monstro)


	# lista_sobreviventes = []
	# for k in range(len(grupo_monstro)):
	# 	monstro = grupo_monstro[k]
	# 	if not interseccao(monstro.rect.x, monstro.rect.y, atirar_x, atirar_y):
	# 		lista_sobreviventes.append(k)

	# monstros_restantes = []
	# for k in lista_sobreviventes:
	# 	monstros_restantes.append(lista_monstros[k])

	# lista_monstros = monstros_restantes
	if len(grupo_monstro) == 0 and len(grupo_nave_mae) == 0:
		tela.fill([0,0,0])
		tela.blit(fim,(100,220))

#Fazendo 
	grupo_tiros.update()
	grupo_monstro.update()
	grupo_nave_mae.update()
	pygame.display.update()

	pygame.display.flip()
	clock.tick(60)




