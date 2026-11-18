
import pygame
from constantes import LARGURA, ALTURA, ALTURA_CHAO, TAMANHO_JOGADOR
from classes import jogador

def fase_facil(janela):
    relogio = pygame.time.Clock()
    rodando = True

    
    img_chao = pygame.image.load("Assets/Imgs/chao_grama.png").convert_alpha()

    area_visivel = img_chao.get_bounding_rect(min_alpha=10)
    img_chao = img_chao.subsurface(area_visivel).copy()

    img_chao = pygame.transform.scale(img_chao, (330, ALTURA_CHAO))


    imagem_robo_andando = []

    for nome in ["robo_andando_1.png", "robo_andando_2.png"]:
        img_player = pygame.image.load("Assets/Imgs/" + nome).convert_alpha()
        img_player = pygame.transform.scale(img_player, (TAMANHO_JOGADOR, TAMANHO_JOGADOR))
        imagem_robo_andando.append(img_player)

    
    img_pulo = pygame.image.load("Assets/Imgs/robo_pulando_v2.png").convert_alpha()
    img_pulo = pygame.transform.scale(img_pulo, (TAMANHO_JOGADOR, TAMANHO_JOGADOR))

    img_agachado = pygame.image.load("Assets/Imgs/robo_agachado.png").convert_alpha()
    img_agachado = pygame.transform.scale(img_agachado, (TAMANHO_JOGADOR, TAMANHO_JOGADOR))

    som_pulo = pygame.mixer.Sound("Assets/Sons/som_pulo.wav")


    player = jogador(imagem_robo_andando, img_pulo, img_agachado, som_pulo)

    deslocamento_chao = 0
    

    while rodando:
        relogio.tick(30)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False


        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_w] or teclas[pygame.K_UP] or teclas[pygame.K_SPACE]:
            player.jump()

        if teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
            player.agachar()
        else:
            player.agachado = False



        deslocamento_chao -= 15

        if deslocamento_chao <= -330:
            deslocamento_chao = 0


        player.update()

        janela.fill((135, 206, 235))
        
        for x in range(0, LARGURA + 330, 330):
            janela.blit(img_chao, (x + deslocamento_chao, ALTURA - ALTURA_CHAO))

        janela.blit(player.image, player.rect)



        
        pygame.display.update()

        

    return "sair"


if __name__ == "__main__":
    pygame.init()
    janela = pygame.display.set_mode((LARGURA, ALTURA))
    fase_facil(janela)
    pygame.quit()
