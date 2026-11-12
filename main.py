import pygame

pygame.init()

# Medidas da tela
LARGURA = 1100
ALTURA = 700

# Outras constantes
ALTURA_CHAO = 200
TAMANHO_JOGADOR = 85
GRAVIDADE = 4
VELOCIDADE_PULO = -30
VELOCIDADE_CENARIO = 15
LARGURA_BLOCO_CHAO = 330
LARGURA_ESPINHO = 40
ALTURA_ESPINHO = 45
TAMANHO_DRONE = 50
LARGURA_CANO = 150
ALTURA_CANO = ALTURA - ALTURA_CHAO - 60
LARGURA_PORTAL = 100
ALTURA_PORTAL = ALTURA - ALTURA_CHAO

janela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Meu Jogo")


class jogador(pygame.sprite.Sprite):
    def __init__(self, imagem_andando, img_pulo,img_agachado):        
        pygame.sprite.Sprite.__init__(self)
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
        self.rect.top = ALTURA-ALTURA_CHAO
        self.mask = pygame.mask.from_surface(self.image)    
        
def fase_dificil(janela):
    img_chao = pygame.image.load("Assets/Imgs/chao_futurista.png")
    img_chao = pygame.transform.scale(img_chao, (LARGURA_BLOCO_CHAO, ALTURA_CHAO))

    img_espinho = pygame.image.load("Assets/Imgs/espinho_futurista.png").convert_alpha()
    img_espinho = pygame.transform.scale(img_espinho,(LARGURA_ESPINHO,ALTURA_ESPINHO))
    img_drone = pygame.image.load("Assets/Imgs/drone_futurista.png").convert_alpha()
    img_drone = pygame.transform.scale(img_drone, (TAMANHO_DRONE, TAMANHO_DRONE))
    img_cano = pygame.image.load("Assets/Imgs/cano_futurista.png").convert_alpha()
    img_cano = pygame.transform.scale(img_cano, (LARGURA_CANO, ALTURA_CANO))
    img_portal_agachar = pygame.image.load("Assets/Imgs/portal_agachar.png").convert_alpha()
    img_portal_agachar = pygame.transform.scale(img_portal_agachar, (LARGURA_PORTAL,ALTURA_PORTAL))
    img_portal_pular = pygame.image.load("Assets/Imgs/portal_pular.png").convert_alpha()
    img_portal_pular = pygame.transform.scale(img_portal_pular, (LARGURA_PORTAL,ALTURA_PORTAL))


    imagem_robo_andando = []
    for nome in ["robo_andando_1.png", "robo_andando_2.png"]:
        img_player = pygame.image.load("Assets/Imgs/" + nome).convert_alpha()
        img_player = pygame.transform.scale(img_player,(TAMANHO_JOGADOR,TAMANHO_JOGADOR))
        imagem_robo_andando.append(img_player)

    img_pulo = pygame.image.load("Assets/Imgs/robo_pulando_v2.png").convert_alpha()
    img_pulo = pygame.transform.scale(img_pulo,(TAMANHO_JOGADOR,TAMANHO_JOGADOR))
    img_agachado = pygame.image.load("Assets/Imgs/robo_agachado.png").convert_alpha()
    img_agachado = pygame.transform.scale(img_agachado,(TAMANHO_JOGADOR,TAMANHO_JOGADOR))


    player = jogador(imagem_robo_andando, img_pulo, img_agachado)
    all_sprites = pygame.sprite.Group()
    all_espinhos = pygame.sprite.Group()
    all_drones = pygame.sprite.Group()
    all_canos = pygame.sprite.Group()

    all_sprites.add(player)
    global VELOCIDADE_CENARIO
    VELOCIDADE_CENARIO = 15

    FPS = 30
    jogo = True
    relogio = pygame.time.Clock()

    deslocamento_chao = 0
    keydown = False

    posicoes_espinhos = [700,1200,1240,1650,1800,1840,2400,2700,2996,3036,3600,3620,3820,4020,4200,4240,5000,5300,5600]
    for x in posicoes_espinhos:
        espinho = Espinho(img_espinho,x)
        all_sprites.add(espinho)
        all_espinhos.add(espinho)

    posicoes_drone = [2650,2800,3700,4200,4520,5800,6050,6200,6300]
    for x in posicoes_drone:
        drone = Drone(img_drone,x)
        all_sprites.add(drone)
        all_drones.add(drone)

    posicoes_cano = [5800,6000]
    for x in posicoes_cano:
        cano = Cano(img_cano,x)
        all_sprites.add(cano)
        all_canos.add(cano)

    ultima_aceleracao = pygame.time.get_ticks()
    intervalo_aceleracao = 15000
    velocidade_maxima = 18

    while jogo:
        relogio.tick(FPS)
        agora = pygame.time.get_ticks()

        if agora - ultima_aceleracao>=intervalo_aceleracao:
            if VELOCIDADE_CENARIO<velocidade_maxima:
                    VELOCIDADE_CENARIO+=1

            ultima_aceleracao = pygame.time.get_ticks()

        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogo = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    keydown = True
                elif evento.key == pygame.K_DOWN:
                    player.agachar()
                
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_UP:
                    keydown = False
                elif evento.key == pygame.K_DOWN:
                    player.agachado = False
            

        if keydown == True:
            player.jump()

        all_sprites.update()
        colisao_espinho = pygame.sprite.spritecollide(player,all_espinhos,False,pygame.sprite.collide_mask)
        colisao_drone = pygame.sprite.spritecollide(player,all_drones,False,pygame.sprite.collide_mask)
        colisao_cano = pygame.sprite.spritecollide(player,all_canos,False,pygame.sprite.collide_mask)

        if colisao_espinho !=[] or colisao_drone !=[] or colisao_cano !=[]:
            return "perdeu"

        deslocamento_chao -= VELOCIDADE_CENARIO
        if deslocamento_chao <= -LARGURA_BLOCO_CHAO:
            deslocamento_chao += LARGURA_BLOCO_CHAO
    
        janela.fill((8, 12, 32))

        for i in range(0, LARGURA + LARGURA_BLOCO_CHAO, LARGURA_BLOCO_CHAO):
            janela.blit(img_chao,(i + deslocamento_chao, ALTURA - ALTURA_CHAO))

        all_sprites.draw(janela)
        pygame.display.update()

    return "sair"

fase_dificil(janela)

pygame.quit()