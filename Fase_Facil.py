
import pygame
from constantes import LARGURA, ALTURA, ALTURA_CHAO, TAMANHO_JOGADOR, LARGURA_ESPINHO, ALTURA_ESPINHO, TAMANHO_DRONE
from classes import jogador, Espinho, Drone


def fase_facil(janela):
    relogio = pygame.time.Clock()
    rodando = True


    img_fundo = pygame.image.load("Assets/Imgs/fundo_jurassico.png").convert()
    img_fundo = pygame.transform.scale(img_fundo, (LARGURA, ALTURA - ALTURA_CHAO))


    img_chao = pygame.image.load("Assets/Imgs/chao_grama.png").convert_alpha()

    area_visivel = img_chao.get_bounding_rect(min_alpha=10)
    img_chao = img_chao.subsurface(area_visivel).copy()
    img_chao = pygame.transform.scale(img_chao, (330, ALTURA_CHAO))

    TAMANHO_CAVERNICOLA = TAMANHO_JOGADOR + 20

    imagem_robo_andando = []

    for nome in ["cavernicola_andando_1.png", "cavernicola_andando_2.png"]:
        img_player = pygame.image.load("Assets/Imgs/" + nome).convert_alpha()
        img_player = pygame.transform.scale(img_player, (TAMANHO_CAVERNICOLA, TAMANHO_CAVERNICOLA))
        imagem_robo_andando.append(img_player)

    img_pulo = pygame.image.load("Assets/Imgs/cavernicola_pulando.png").convert_alpha()
    img_pulo = pygame.transform.scale(img_pulo, (TAMANHO_CAVERNICOLA, TAMANHO_CAVERNICOLA))

    img_agachado = pygame.image.load("Assets/Imgs/cavernicola_agachado.png").convert_alpha()

    altura_agachado = int(TAMANHO_CAVERNICOLA * 0.9)
    img_agachado = pygame.transform.scale(img_agachado, (TAMANHO_CAVERNICOLA, altura_agachado))

    quadro = pygame.Surface((TAMANHO_CAVERNICOLA, TAMANHO_CAVERNICOLA), pygame.SRCALPHA)
    quadro.blit(img_agachado, (0, TAMANHO_CAVERNICOLA - altura_agachado))
    img_agachado = quadro

    som_pulo = pygame.mixer.Sound("Assets/Sons/som_pulo.wav")

    player = jogador(imagem_robo_andando, img_pulo, img_agachado, som_pulo)

    deslocamento_chao = 0

    img_pedra = pygame.image.load("Assets/Imgs/espinho_pedra.png").convert_alpha()

    LARGURA_PEDRA = int(LARGURA_ESPINHO * 1.3)
    ALTURA_PEDRA = int(ALTURA_ESPINHO * 1.3)

    img_pedra = pygame.transform.scale(img_pedra, (LARGURA_PEDRA, ALTURA_PEDRA))

    all_pedras = pygame.sprite.Group()

    posicoes_pedras = [700, 750, 1600, 1800, 2000, 2050, 2500, 2700, 3150]

    for x in posicoes_pedras:
        pedra = Espinho(img_pedra, x)
        all_pedras.add(pedra)

    img_pterodatilo = pygame.image.load("Assets/Imgs/pterodactilo.png").convert_alpha()
    img_pterodatilo = pygame.transform.scale(img_pterodatilo, (TAMANHO_DRONE * 2, TAMANHO_DRONE))

    all_pterodatilos = pygame.sprite.Group()

    posicoes_pterodatilos = [3900]

    for x in posicoes_pterodatilos:
        pterodatilo = Drone(img_pterodatilo, x)
        pterodatilo.rect.bottom = ALTURA - ALTURA_CHAO - 72
        all_pterodatilos.add(pterodatilo)

    img_game_over = pygame.image.load("Assets/Imgs/game_over_TRex.png").convert()
    img_game_over = pygame.transform.scale(img_game_over, (LARGURA, ALTURA))

    perdeu = False
    vidas = 3

    distancia_percorrida = 0
    pontos_moedas = 0
    pontos = 0

    fonte_tex = pygame.font.Font("Assets/Fonts/PressStart2P.ttf", 24)
    fonte_titulo = pygame.font.Font("Assets/Fonts/PressStart2P.ttf", 48)
    fonte_texto = pygame.font.Font("Assets/Fonts/PressStart2P.ttf", 24)
    fonte_vidas = pygame.font.Font("Assets/Fonts/PressStart2P.ttf", 36)

    while rodando:
        relogio.tick(30)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        if not rodando:
            break

        if perdeu:
            janela.blit(img_game_over, (0, 0))

            titulo = fonte_titulo.render("GAME OVER!", True, (255, 0, 0))
            mensagem = fonte_texto.render("Tente novamente!", True, (255, 255, 255))
            resultado = fonte_texto.render(f"Total pontos: {pontos}", True, (255, 255, 255))

            janela.blit(titulo, titulo.get_rect(center=(LARGURA // 2, 100)))
            janela.blit(mensagem, mensagem.get_rect(center=(LARGURA // 2, 170)))
            janela.blit(resultado, resultado.get_rect(center=(LARGURA // 2, 240)))

            pygame.display.update()
            continue

        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_w] or teclas[pygame.K_UP] or teclas[pygame.K_SPACE]:
            player.jump()

        if teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
            player.agachar()
        else:
            player.agachado = False

        deslocamento_chao -= 15
        distancia_percorrida += 15
        pontos = distancia_percorrida // 10 + pontos_moedas

        if deslocamento_chao <= -330:
            deslocamento_chao = 0

        player.update()
        all_pedras.update()
        all_pterodatilos.update()

        colisao_pedra = pygame.sprite.spritecollide(
            player, all_pedras, True, pygame.sprite.collide_mask
        )

        colisao_pterodatilo = pygame.sprite.spritecollide(
            player, all_pterodatilos, True, pygame.sprite.collide_mask
        )

        if colisao_pedra or colisao_pterodatilo:
            vidas -= 1

            if vidas == 0:
                perdeu = True

        janela.blit(img_fundo, (0, 0))

        for x in range(0, LARGURA + 330, 330):
            janela.blit(img_chao, (x + deslocamento_chao, ALTURA - ALTURA_CHAO))

        janela.blit(player.image, player.rect)
        all_pedras.draw(janela)
        all_pterodatilos.draw(janela)

        texto_pontos = fonte_tex.render(f"Pontos: {pontos}", True, (255, 255, 255))
        janela.blit(texto_pontos, (20, 20))

        texto_vida = fonte_vidas.render("♥" * vidas, True, (255, 0, 0))
        janela.blit(texto_vida, (20, 60))

        pygame.display.update()

    return "sair"


if __name__ == "__main__":
    pygame.init()
    janela = pygame.display.set_mode((LARGURA, ALTURA))
    fase_facil(janela)
    pygame.quit()
