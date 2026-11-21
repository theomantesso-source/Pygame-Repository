import pygame
from constantes import ALTURA,LARGURA
from funcoes import fase_dificil,tela_inicial,fase_facil,fase_media

pygame.init()

janela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Evolution Race")


while True:
    escolha = tela_inicial(janela)
    
    if escolha == "facil":
        resultado = fase_facil(janela)
    elif escolha == "dificil":
        resultado = fase_dificil(janela)
    elif escolha == "medio":
        resultado = fase_media(janela)
    else:
        break
    if resultado != "inicio":
        break

pygame.quit()
