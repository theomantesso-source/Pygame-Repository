import pygame
from constantes import GRAVIDADE,ALTURA,ALTURA_CANO,ALTURA_CHAO,ALTURA_ESCUDO,ALTURA_ESPINHO,ALTURA_PORTAL_AGACHAR,ALTURA_PORTAL_PULAR,LARGURA_PORTAL_AGACHAR,LARGURA,LARGURA_BLOCO_CHAO,LARGURA_CANO,LARGURA_ESCUDO,LARGURA_ESPINHO,LARGURA_PORTAL_PULAR,VELOCIDADE_CENARIO,VELOCIDADE_PULO,TAMANHO_DRONE,TAMANHO_JOGADOR,DISTANCIA_FINAL
from classes import jogador,Espinho,Vida,Cano,Drone,Portal,Linha_chegada,Moeda
from funcoes import tela_final,tela_game_over,fase_dificil

pygame.init()

janela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Evolution Race")


fase_dificil(janela)

pygame.quit()