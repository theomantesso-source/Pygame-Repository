import pygame
from constantes import GRAVIDADE,ALTURA,ALTURA_CANO,ALTURA_CHAO,ALTURA_ESCUDO,ALTURA_ESPINHO,ALTURA_PORTAL_AGACHAR,ALTURA_PORTAL_PULAR,LARGURA_PORTAL_AGACHAR,LARGURA,LARGURA_BLOCO_CHAO,LARGURA_CANO,LARGURA_ESCUDO,LARGURA_ESPINHO,LARGURA_PORTAL_PULAR,VELOCIDADE_CENARIO,VELOCIDADE_PULO,TAMANHO_DRONE,TAMANHO_JOGADOR


class jogador(pygame.sprite.Sprite):
    def __init__(self, imagem_andando, img_pulo,img_agachado,som_pulo):        
        pygame.sprite.Sprite.__init__(self)
        self.som_pulo = som_pulo
        self.imagem_andando = imagem_andando
        self.img_pulo = img_pulo           
        self.img_agachado = img_agachado
        self.agachado = False
        self.image = self.imagem_andando[0]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.bottom = ALTURA - ALTURA_CHAO
        self.velocidade_y = 0
        self.frame = 0
        self.ultima_troca = pygame.time.get_ticks()
        self.intervalo_animacao = 120

    def update(self):
        self.velocidade_y += GRAVIDADE
        self.rect.y += self.velocidade_y

        if self.rect.bottom >= ALTURA - ALTURA_CHAO:
            self.rect.bottom = ALTURA - ALTURA_CHAO
            self.velocidade_y = 0

        agora = pygame.time.get_ticks()
        if self.rect.bottom < ALTURA - ALTURA_CHAO:
            self.image = self.img_pulo
            self.ultima_troca = agora
        elif self.agachado:
            self.image = self.img_agachado
            self.ultima_troca = agora
        else:
            self.image = self.imagem_andando[0]
            if agora-self.ultima_troca>=self.intervalo_animacao:
                self.frame= 1-self.frame
                self.ultima_troca = agora

            self.image = self.imagem_andando[self.frame]
        
            
        self.mask = pygame.mask.from_surface(self.image)
    def jump(self):
        if self.rect.bottom == ALTURA - ALTURA_CHAO:
            self.velocidade_y = VELOCIDADE_PULO
            self.som_pulo.play()
        
    def agachar(self):
        self.agachado = True
        


class Espinho(pygame.sprite.Sprite):
    def __init__(self, imagem, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagem
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = ALTURA-ALTURA_CHAO
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.x-=VELOCIDADE_CENARIO
        if self.rect.x<-LARGURA_ESPINHO:
            self.kill()

class Drone(pygame.sprite.Sprite):
    def __init__(self, imagem, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagem
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = ALTURA-ALTURA_CHAO-60
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.x-=VELOCIDADE_CENARIO+5
        if self.rect.x<=-TAMANHO_DRONE:
            self.kill()

class Cano(pygame.sprite.Sprite):
    def __init__(self, imagem, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagem
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.top = 0
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.x -= VELOCIDADE_CENARIO
        if self.rect.right < 0:
            self.kill()

class Portal(pygame.sprite.Sprite):
    def __init__(self,imagem, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagem
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = ALTURA - ALTURA_CHAO        
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.x -= VELOCIDADE_CENARIO
        if self.rect.right<0:
            self.kill()

class Vida(pygame.sprite.Sprite):
    def __init__(self,imagem, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagem
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = ALTURA - ALTURA_CHAO - 85    
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.x -= VELOCIDADE_CENARIO
        if self.rect.right<0:
            self.kill()

class Moeda(pygame.sprite.Sprite):
    def __init__(self,imagem, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagem
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = y   
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
            self.rect.x -= VELOCIDADE_CENARIO
            if self.rect.right<0:
                self.kill()

class Linha_chegada(pygame.sprite.Sprite):
    def __init__(self,imagem, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagem
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = ALTURA-ALTURA_CHAO
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
            self.rect.x -= VELOCIDADE_CENARIO

class Faixa(pygame.sprite.Sprite):
    def __init__(self, imagem, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagem
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = ALTURA - ALTURA_CHAO
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.x -= VELOCIDADE_CENARIO

        if self.rect.right < 0:
            self.kill()
