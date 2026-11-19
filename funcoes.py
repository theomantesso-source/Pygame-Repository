import pygame
from constantes import GRAVIDADE,ALTURA,ALTURA_CANO,ALTURA_CHAO,ALTURA_ESCUDO,ALTURA_ESPINHO,ALTURA_PORTAL_AGACHAR,ALTURA_PORTAL_PULAR,LARGURA_PORTAL_AGACHAR,LARGURA,LARGURA_BLOCO_CHAO,LARGURA_CANO,LARGURA_ESCUDO,LARGURA_ESPINHO,LARGURA_PORTAL_PULAR,VELOCIDADE_CENARIO,VELOCIDADE_PULO,TAMANHO_DRONE,TAMANHO_JOGADOR,DISTANCIA_FINAL
from classes import jogador,Espinho,Vida,Cano,Drone,Portal,Linha_chegada,Moeda,Faixa

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

    img_inicio = pygame.image.load("Assets/Imgs/botao_inicio.png").convert_alpha()
    img_inicio = pygame.transform.scale(img_inicio, (100, 100))
    botao_inicio = img_inicio.get_rect(center=(LARGURA // 2, 650))    

    while tela:
        timer.tick(30)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                tela = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    if botao_inicio.collidepoint(evento.pos):
                        return "inicio"

        janela.blit(img_game_over,(0,0))
        janela.blit(texto_titulo, (300,220))
        janela.blit(texto_tente,(320,280))
        janela.blit(total_ponto,(310,400))
        janela.blit(img_inicio, botao_inicio)

        pygame.display.update()

def tela_inicial(janela):
    img_inicio = pygame.image.load("Assets/Imgs/menu_evolution_race.png").convert()
    img_inicio = pygame.transform.scale(img_inicio, (LARGURA, ALTURA))

    timer = pygame.time.Clock()
    fonte = pygame.font.Font("Assets/Fonts/PressStart2P.ttf", 20)

    largura_area = LARGURA // 3

    area_facil = pygame.Rect(0, 200, largura_area, ALTURA - 200)
    area_media = pygame.Rect(largura_area, 200, largura_area, ALTURA - 200)
    area_dificil = pygame.Rect(largura_area * 2, 200,LARGURA - largura_area * 2, ALTURA - 200)

    img_facil = pygame.image.load("Assets/Imgs/botao_facil.png").convert_alpha()
    img_facil = pygame.transform.scale(img_facil, (150, 150))
    img_medio = pygame.image.load("Assets/Imgs/botao_medio.png").convert_alpha()
    img_medio = pygame.transform.scale(img_medio, (150, 150))
    img_dificil = pygame.image.load("Assets/Imgs/botao_dificil.png").convert_alpha()
    img_dificil = pygame.transform.scale(img_dificil, (150, 150))

    pygame.mixer.music.load("Assets/Sons/menu_evolution_race_mais_alto.wav")
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play(-1)

    while True:
        timer.tick(30)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "sair"

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    if area_facil.collidepoint(evento.pos):
                        pygame.mixer.music.stop()
                        return "facil"

                    elif area_dificil.collidepoint(evento.pos):
                        pygame.mixer.music.stop()
                        return "dificil"

        janela.blit(img_inicio, (0, 0))
        janela.blit(img_facil, (108, 540))
        janela.blit(img_medio, (475, 540))
        janela.blit(img_dificil, (842, 540))

        
        pygame.display.update()

        

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
    img_portal_agachar = pygame.transform.scale(img_portal_agachar, (LARGURA_PORTAL_AGACHAR,ALTURA_PORTAL_AGACHAR))
    img_portal_pular = pygame.image.load("Assets/Imgs/portal_pular.png").convert_alpha()
    img_portal_pular = pygame.transform.scale(img_portal_pular, (LARGURA_PORTAL_PULAR,ALTURA_PORTAL_PULAR))
    img_vida = pygame.image.load("Assets/Imgs/vida_retro.png").convert_alpha()
    img_vida = pygame.transform.scale(img_vida, (LARGURA_ESCUDO,ALTURA_ESCUDO ))    
    img_moeda = pygame.image.load("Assets/Imgs/moeda_ouro.png").convert_alpha()
    img_moeda = pygame.transform.scale(img_moeda, (50,50)) 
    img_chegada = pygame.image.load("Assets/Imgs/chegada_fim.png").convert_alpha()
    img_chegada = pygame.transform.scale(img_chegada, (280,280))   
    


    imagem_robo_andando = []
    for nome in ["robo_andando_1.png", "robo_andando_2.png"]:
        img_player = pygame.image.load("Assets/Imgs/" + nome).convert_alpha()
        img_player = pygame.transform.scale(img_player,(TAMANHO_JOGADOR,TAMANHO_JOGADOR))
        imagem_robo_andando.append(img_player)

    img_pulo = pygame.image.load("Assets/Imgs/robo_pulando_v2.png").convert_alpha()
    img_pulo = pygame.transform.scale(img_pulo,(TAMANHO_JOGADOR,TAMANHO_JOGADOR))
    img_agachado = pygame.image.load("Assets/Imgs/robo_agachado.png").convert_alpha()
    img_agachado = pygame.transform.scale(img_agachado,(TAMANHO_JOGADOR,TAMANHO_JOGADOR))

    som_pulo = pygame.mixer.Sound("Assets/Sons/som_pulo.wav")
    som_pulo.set_volume(0.3)
    som_batida = pygame.mixer.Sound("Assets/Sons/batida_quebra.wav")
    som_batida.set_volume(0.5)
    som_morte = pygame.mixer.Sound("Assets/Sons/morte.wav")
    som_morte.set_volume(0.5)
    som_vida = pygame.mixer.Sound("Assets/Sons/coleta_vida.wav")
    som_vida.set_volume(0.7)
    som_moeda = pygame.mixer.Sound("Assets/Sons/coleta_moeda_v2.wav")
    som_moeda.set_volume(0.7)
    som_vitoria = pygame.mixer.Sound("Assets/Sons/vitoria.wav")
    som_vitoria.set_volume(0.7)



    player = jogador(imagem_robo_andando, img_pulo, img_agachado,som_pulo)
    all_sprites = pygame.sprite.Group()
    all_espinhos = pygame.sprite.Group()
    all_drones = pygame.sprite.Group()
    all_canos = pygame.sprite.Group()
    all_portais = pygame.sprite.Group()
    all_coins = pygame.sprite.Group()

    all_sprites.add(player)
    global VELOCIDADE_CENARIO
    VELOCIDADE_CENARIO = 15

    linha_chegada = Linha_chegada(img_chegada,21900)
    all_sprites.add(linha_chegada)
    vida = Vida(img_vida,9370)
    all_vidas = pygame.sprite.Group()
    all_sprites.add(vida)
    all_vidas.add(vida)


    posicoes_espinhos = [700, 1200, 1240, 1650, 1800, 1840, 2400, 2700, 2996, 3036, 3600, 3620, 3820, 4020, 4200, 4240, 5000, 5300, 5600, 6200, 6240, 6420, 8270, 8700, 9000, 9040, 10400, 10440, 11070, 11110, 11350, 11390, 12700, 12740, 13200, 13240, 14400, 14440, 14680, 15500, 15540, 15800, 15840, 17000, 17040, 17080, 17300, 18100, 18140, 18180, 18450, 18490, 19800, 19840, 19880, 21100, 21140, 21180]
    for x in posicoes_espinhos:
        espinho = Espinho(img_espinho,x)
        all_sprites.add(espinho)
        all_espinhos.add(espinho)
 
    posicoes_drone = [2650, 2800, 3700, 4200, 4520, 5800, 6050, 6200, 6300, 12400, 12700, 14320, 16300, 17200, 17860, 18450, 21100, 21750, 26800] 
    for x in posicoes_drone:
        drone = Drone(img_drone,x)
        all_sprites.add(drone)
        all_drones.add(drone)

    posicoes_cano = [5800, 6000, 6900, 8400, 9200, 10850, 11800, 13000, 13550, 16050, 18800, 20500] 
    for x in posicoes_cano:
        cano = Cano(img_cano,x)
        all_sprites.add(cano)
        all_canos.add(cano)

    posicoes_portal_pular = [7600, 8000, 8600, 10000, 11950, 14950, 16280, 17600, 21600]
    for x in posicoes_portal_pular:
            portal = Portal(img_portal_pular,x)
            all_sprites.add(portal)
            all_portais.add(portal)

    posicoes_portal_agachar = [7000, 12350, 13950, 15180, 16550, 19300]
    for x in posicoes_portal_agachar:
        portal = Portal(img_portal_agachar,x)
        all_sprites.add(portal)
        all_portais.add(portal)

    posicao_moeda_x = [3550, 11680, 15920, 18680, 21050]
    posicao_moeda_y = [500, 420, 420, 420, 500]
    i = 0
    while i<len(posicao_moeda_x):
        moeda = Moeda(img_moeda,posicao_moeda_x[i],posicao_moeda_y[i])
        all_sprites.add(moeda)
        all_coins.add(moeda)
        i+=1
    

    ultima_aceleracao = pygame.time.get_ticks()
    intervalo_aceleracao = 15000
    velocidade_maxima = 19
    life = 0
    distancia_percorrida = 0
    pontos = 0
    fonte_tex = pygame.font.Font("Assets/Fonts/PressStart2P.ttf", 24)
    pygame.mixer.music.load("Assets/Sons/musica_fundo.wav")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(-1)

    FPS = 30
    jogo = True
    relogio = pygame.time.Clock()
    
    deslocamento_chao = 0
    keydown = False

    morrendo = False
    vencendo = False
    pontos_moedas = 0
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
                if evento.key == pygame.K_UP or evento.key == pygame.K_SPACE or evento.key == pygame.K_w:
                    keydown = True
                elif evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                    player.agachar()
                
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_UP or evento.key == pygame.K_SPACE or evento.key == pygame.K_w:
                    keydown = False
                elif evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                    player.agachado = False
            

        if morrendo == True:
            if canal_morte.get_busy() == False:
                resultado = tela_game_over(janela,pontos)
                return resultado
            continue


        if vencendo == True:
            if canal_vitoria.get_busy() == False:
                pygame.mixer.music.play(-1)
                tela_final(janela,pontos,pontos_moedas,life)
                return "venceu"
            continue

    
        if keydown == True:
            player.jump()

        all_sprites.update()
        colisao_espinho = pygame.sprite.spritecollide(player,all_espinhos,True,pygame.sprite.collide_mask)
        colisao_drone = pygame.sprite.spritecollide(player,all_drones,True,pygame.sprite.collide_mask)
        colisao_cano = pygame.sprite.spritecollide(player,all_canos,True,pygame.sprite.collide_mask)
        colisao_portal = pygame.sprite.spritecollide(player,all_portais,True,pygame.sprite.collide_mask)
        colisao_vidas = pygame.sprite.spritecollide(player,all_vidas,True,pygame.sprite.collide_mask)
        colisao_moedas = pygame.sprite.spritecollide(player,all_coins,True,pygame.sprite.collide_mask)


        if colisao_espinho !=[] or colisao_drone !=[] or colisao_cano !=[] or colisao_portal !=[]:
            life -= 1
            if life>=0:
                som_batida.play()

        if colisao_vidas != []:
            som_vida.play()
            life += 1

        if colisao_moedas!=[]:
            som_moeda.play()
            pontos_moedas+=100

        
        if life<0:
            pygame.mixer.music.stop()
            canal_morte = som_morte.play()
            morrendo = True
            continue
        
        agora = pygame.time.get_ticks()
        distancia_percorrida += VELOCIDADE_CENARIO
        pontos = distancia_percorrida // 10 + pontos_moedas

        if distancia_percorrida>=DISTANCIA_FINAL:
            pygame.mixer.music.stop()
            canal_vitoria = som_vitoria.play()
            vencendo = True
            continue
        
        deslocamento_chao -= VELOCIDADE_CENARIO
        if deslocamento_chao <= -LARGURA_BLOCO_CHAO:
            deslocamento_chao += LARGURA_BLOCO_CHAO

        janela.fill((8, 12, 32))

        for i in range(0, LARGURA + LARGURA_BLOCO_CHAO, LARGURA_BLOCO_CHAO):
            janela.blit(img_chao,(i + deslocamento_chao, ALTURA - ALTURA_CHAO))

        all_sprites.draw(janela)

        fonte = pygame.font.Font("Assets/Fonts/PressStart2P.ttf", 36)
        texto_vida = fonte.render("♥"*(life + 1),True,(255,0,0))
        text_ponto = fonte_tex.render(f"Pontos: {pontos}",True,(255,255,255))
        janela.blit(texto_vida, (20, 60))
        janela.blit(text_ponto,(20,20))

        pygame.display.update()

    return "sair"


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
    vidas = 2

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