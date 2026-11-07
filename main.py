import pygame

pygame.init()

LARGURA = 1100
ALTURA = 700
ALTURA_CHAO = 110
TAMANHO_JOGADOR = 50

janela = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption("Meu Jogo")

img_player = pygame.image.load("Assets/Imgs/Jogador.jpeg")
img_player = pygame.transform.scale(img_player, (TAMANHO_JOGADOR, TAMANHO_JOGADOR))
player = pygame.Rect(150,(ALTURA-ALTURA_CHAO-TAMANHO_JOGADOR),TAMANHO_JOGADOR,TAMANHO_JOGADOR) 
jogo = True 
FPS = 60

relogio = pygame.time.Clock()

while jogo:
    relogio.tick(FPS)

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            jogo = False

    janela.fill((8, 12, 32))
    pygame.draw.rect(janela,(30,75,40),(0,(ALTURA-ALTURA_CHAO),LARGURA,ALTURA_CHAO))
    janela.blit(img_player,player)

    pygame.display.update()
pygame.quit()