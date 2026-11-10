import pygame

pygame.init()

# Medidas da tela
LARGURA = 1100
ALTURA = 700

# Outras constantes
ALTURA_CHAO = 200
TAMANHO_JOGADOR = 50
GRAVIDADE = 4
VELOCIDADE_PULO = -36
VELOCIDADE_CENARIO = 12
LARGURA_BLOCO_CHAO = 330
LARGURA_ESPINHO = 40
ALTURA_ESPINHO = 45

janela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Meu Jogo")


class jogador(pygame.sprite.Sprite):
    def __init__(self, imagem):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagem
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.bottom = ALTURA - ALTURA_CHAO
        self.velocidade_y = 0

    def update(self):
        self.velocidade_y += GRAVIDADE
        self.rect.y += self.velocidade_y

        if self.rect.bottom >= ALTURA - ALTURA_CHAO:
            self.rect.bottom = ALTURA - ALTURA_CHAO
            self.velocidade_y = 0

    def jump(self):
        if self.rect.bottom == ALTURA - ALTURA_CHAO:
            self.velocidade_y = VELOCIDADE_PULO
        


class Espinho(pygame.sprite.Sprite):
    def __init__(self, imagem):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagem
        self.rect = self.image.get_rect()
        self.rect.x = 700
        self.rect.bottom = ALTURA-ALTURA_CHAO
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.x-=VELOCIDADE_CENARIO
        if self.rect.x<-LARGURA_ESPINHO:
            self.rect.x = LARGURA


def fase_dificil(janela):
    img_player = pygame.image.load("Assets/Imgs/Jogador.jpeg")
    img_player = pygame.transform.scale(img_player, (TAMANHO_JOGADOR, TAMANHO_JOGADOR))
    img_chao = pygame.image.load("Assets/Imgs/chao_futurista.png")
    img_chao = pygame.transform.scale(img_chao, (LARGURA_BLOCO_CHAO, ALTURA_CHAO))
    img_espinho = pygame.image.load("Assets/Imgs/espinho_futurista.png").convert_alpha()
    img_espinho = pygame.transform.scale(img_espinho,(LARGURA_ESPINHO,ALTURA_ESPINHO))


    espinho = Espinho(img_espinho)
    player = jogador(img_player)
    all_sprites = pygame.sprite.Group()
    all_espinhos = pygame.sprite.Group()
    all_espinhos.add(espinho)
    all_sprites.add(player)
    all_sprites.add(espinho)

    FPS = 30
    jogo = True
    relogio = pygame.time.Clock()

    deslocamento_chao = 0
    keydown = False

    while jogo:
        relogio.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogo = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    keydown = True

            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_SPACE:
                    keydown = False

        if keydown == True:
            player.jump()

        all_sprites.update()
        colisoes = pygame.sprite.spritecollide(player,all_espinhos,False,pygame.sprite.collide_mask)    
        if colisoes !=[]:
            print("Bateu!!")
            for obstaculo in colisoes:
                obstaculo.rect.x = LARGURA
        
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