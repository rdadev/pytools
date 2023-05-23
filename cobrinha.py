import pygame
import time
import random

# Inicialização do Pygame
pygame.init()

# Definição das cores
branco = (255, 255, 255)
preto = (0, 0, 0)
verde = (0, 255, 0)
vermelho = (255, 0, 0)

# Dimensões da tela
largura = 800
altura = 600

# Configuração da tela do jogo
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobrinha")

# Relógio para controle de frames por segundo
clock = pygame.time.Clock()

# Tamanho da cobrinha e velocidade
tamanho_cobrinha = 20
velocidade = 15

# Fonte para exibir a pontuação
fonte = pygame.font.SysFont(None, 30)

# Função para exibir a pontuação na tela
def mostrar_pontuacao(pontos):
    texto = fonte.render("Pontuação: " + str(pontos), True, branco)
    tela.blit(texto, [10, 10])

# Função principal do jogo
def jogo():
    game_over = False
    fim_do_jogo = False

    # Posição inicial da cobrinha
    posicao_x = largura / 2
    posicao_y = altura / 2

    # Movimento inicial da cobrinha
    movimento_x = 0
    movimento_y = 0

    # Lista que irá armazenar as partes do corpo da cobrinha
    cobrinha = []
    comprimento_inicial = 1

    # Gerando posição aleatória para a comida
    comida_x = round(random.randrange(0, largura - tamanho_cobrinha) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura - tamanho_cobrinha) / 20.0) * 20.0

    pontos = 0

    while not game_over:
        while fim_do_jogo:
            tela.fill(preto)
            mensagem = fonte.render("Fim de jogo! Pressione Q para sair ou C para jogar novamente.", True, branco)
            tela.blit(mensagem, [largura / 6, altura / 2.5])
            mostrar_pontuacao(pontos)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        fim_do_jogo = False
                    if event.key == pygame.K_c:
                        jogo()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    movimento_x = -tamanho_cobrinha
                    movimento_y = 0
                elif event.key == pygame.K_RIGHT:
                    movimento_x = tamanho_cobrinha
                    movimento_y = 0
                elif event.key == pygame.K_UP:
                    movimento_y = -tamanho_cobrinha
                    movimento_x = 0
                elif event.key == pygame.K_DOWN:
                    movimento_y = tamanho_cobrinha
                    movimento_x = 0

        if posicao_x >= largura or posicao_x < 0 or posicao_y >= altura or posicao_y < 0:
            fim_do_jogo = True

        posicao_x += movimento_x
        posicao_y += movimento_y

        tela.fill(preto)
        pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho_cobrinha, tamanho_cobrinha])

        cabeca_cobrinha = []
        cabeca_cobrinha.append(posicao_x)
        cabeca_cobrinha.append(posicao_y)
        cobrinha.append(cabeca_cobrinha)

        if len(cobrinha) > comprimento_inicial:
            del cobrinha[0]

        for segmento in cobrinha[:-1]:
            if segmento == cabeca_cobrinha:
                fim_do_jogo = True

        for segmento in cobrinha:
            pygame.draw.rect(tela, branco, [segmento[0], segmento[1], tamanho_cobrinha, tamanho_cobrinha])

        mostrar_pontuacao(pontos)

        pygame.display.update()

        if posicao_x == comida_x and posicao_y == comida_y:
            comida_x = round(random.randrange(0, largura - tamanho_cobrinha) / 20.0) * 20.0
            comida_y = round(random.randrange(0, altura - tamanho_cobrinha) / 20.0) * 20.0
            comprimento_inicial += 1
            pontos += 1

        clock.tick(velocidade)

    pygame.quit()

jogo()
