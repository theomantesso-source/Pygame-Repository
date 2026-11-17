import pygame
from constantes import GRAVIDADE,ALTURA,ALTURA_CANO,ALTURA_CHAO,ALTURA_ESCUDO,ALTURA_ESPINHO,ALTURA_PORTAL_AGACHAR,ALTURA_PORTAL_PULAR,LARGURA_PORTAL_AGACHAR,LARGURA,LARGURA_BLOCO_CHAO,LARGURA_CANO,LARGURA_ESCUDO,LARGURA_ESPINHO,LARGURA_PORTAL_PULAR,VELOCIDADE_CENARIO,VELOCIDADE_PULO,TAMANHO_DRONE,TAMANHO_JOGADOR,DISTANCIA_FINAL


def tela_final(janela,pontos,pontos_moedas,vidas):
    img_fundo = pygame.image.load("Assets/Imgs/final_fase.png")
    img_fundo = pygame.transform.scale(img_fundo, (LARGURA, ALTURA))
    timer = pygame.time.Clock()
    tela = True
    fonte_titulo = pygame.font.Font("Assets/Fonts/PressStart2P.ttf",36)
    fonte_info = pygame.font.Font("Assets/Fonts/PressStart2P.ttf",24)
    texto_titulo = fonte_titulo.render(f"FASE CONCLUIDA!",True,(0,220,255))
    texto_pontos = fonte_info.render(f"Pontos: {pontos}",True,(255,255,255))
    texto_moedas = fonte_info.render(f"Moedas: {pontos_moedas//100}/5",True,(255,210,60))
    texto_vidas = fonte_info.render(f"Pontos por vida: {(vidas)*500}  ",True,(255,0,0))
    texto_final = fonte_info.render(f"Total de pontos: {((vidas)*500)+pontos}  ",True,(255,255,255))
    

    while tela:
        timer.tick(30)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                tela = False

        janela.blit(img_fundo,(0,0))
        janela.blit(texto_titulo, (300,320))
        janela.blit(texto_pontos,(370,420))
        janela.blit(texto_moedas,(370,470))
        janela.blit(texto_vidas,(370,520))
        janela.blit(texto_final,(370,570))
        pygame.display.update()

def tela_game_over(janela,pontos):
    img_game_over = pygame.image.load("Assets/Imgs/game_over.png")
    img_game_over = pygame.transform.scale(img_game_over, (LARGURA,ALTURA)) 
  
    timer = pygame.time.Clock()
    tela = True
    fonte_titulo = pygame.font.Font("Assets/Fonts/PressStart2P.ttf",46)
    fonte_info = pygame.font.Font("Assets/Fonts/PressStart2P.ttf",24)

    texto_titulo = fonte_titulo.render(f"GAME OVER!",True,(255,0,0))
    texto_tente = fonte_info.render(f"Tente novamente!",True,(255,255,255))
    total_ponto = fonte_info.render(f"Total pontos: {pontos}",True,(255,255,255))

    while tela:
        timer.tick(30)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                tela = False

        janela.blit(img_game_over,(0,0))
        janela.blit(texto_titulo, (300,220))
        janela.blit(texto_tente,(320,280))
        janela.blit(total_ponto,(310,400))
   
        pygame.display.update()
