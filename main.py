import pygame

pygame.init()

LARGURA = 1100
ALTURA = 700
ALTURA_CHAO = 110
TAMANHO_JOGADOR = 50
GRAVIDADE = 0.8
VELOCIDADE_PULO = -15


janela = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption("Meu Jogo")


img_player = pygame.image.load("Assets/Imgs/Jogador.jpeg")
img_player = pygame.transform.scale(img_player, (TAMANHO_JOGADOR, TAMANHO_JOGADOR))

class jogador(pygame.sprite.Sprite):
    def __init__(self, imagem):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagem
        self.rect = self.image.get_rect()
        self.rect.x = 150
        self.rect.bottom = ALTURA-ALTURA_CHAO
        self.velocidade_y = 0

    def update(self):
        self.velocidade_y += GRAVIDADE
        self.rect.y += self.velocidade_y

        if self.rect.bottom >= ALTURA - ALTURA_CHAO:
            self.rect.bottom = ALTURA - ALTURA_CHAO
            self.velocidade_y = 0


    def jump(self):

        if self.rect.bottom == ALTURA-ALTURA_CHAO:
            self.velocidade_y = VELOCIDADE_PULO


player = jogador(img_player)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

FPS = 60
jogo = True

relogio = pygame.time.Clock()

while jogo:
    relogio.tick(FPS)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogo = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                player.jump()
                
    all_sprites.update()
    janela.fill((8, 12, 32))
    pygame.draw.rect(janela,(30,75,40),(0,(ALTURA-ALTURA_CHAO),LARGURA,ALTURA_CHAO))
    all_sprites.draw(janela)
    pygame.display.update()

pygame.quit()