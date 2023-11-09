################################################
##### BY: LEIUQUEZE INACIO #####
################################################

from time import sleep
from random import randint
import sys

def exibir_tabuleiro(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    tabuleiro = '''
     |     |   
  {}  |  {}  |  {}
_____|_____|_____
     |     |
  {}  |  {}  |  {}
_____|_____|_____
     |     |
  {}  |  {}  |  {}
     |     |
    '''.format(p1, p2, p3, p4, p5, p6, p7, p8, p9)
    print(tabuleiro)

def obter_jogada_jogador():
    while True:
        try:
            jogada = int(input('Digite a posição da sua jogada (1 a 9) e pressione Enter: '))
            if 1 <= jogada <= 9:
                return jogada
            else:
                print('\nNúmero inválido! Digite um número inteiro de 1 a 9.\n')
        except ValueError:
            print('\nValor digitado inválido. Digite um número inteiro de 1 a 9!\n')

def realizar_jogada_jogador(j, tabuleiro):
    jogada = obter_jogada_jogador()
    while tabuleiro[jogada - 1] != ' ':
        print('\nEste espaço já está ocupado!\n')
        jogada = obter_jogada_jogador()
    tabuleiro[jogada - 1] = j

def realizar_jogada_pc(adv, tabuleiro):
    print('Deixe-me pensar na minha jogada...')
    sleep(1.5)
    jogada_aleatoria = randint(1, 9)

    while tabuleiro[jogada_aleatoria - 1] != ' ':
        jogada_aleatoria = randint(1, 9)

    print('\nEu jogo na posição {}!'.format(jogada_aleatoria))
    tabuleiro[jogada_aleatoria - 1] = adv

def verificar_vencedor(j, adv, tabuleiro):
    # Verificar todas as condições de vitória
    for linha in ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)):
        if tabuleiro[linha[0]] == tabuleiro[linha[1]] == tabuleiro[linha[2]] == j:
            print('VOCÊ GANHOU!\n')
            return True
        elif tabuleiro[linha[0]] == tabuleiro[linha[1]] == tabuleiro[linha[2]] == adv:
            print('EU GANHEI!\n')
            return True
    return False

def jogar_novamente():
    while True:
        reiniciar = input('\nQuer jogar de novo? Digite S para sim ou N para não: ').lower()
        if reiniciar in ('s', 'n'):
            return reiniciar == 's'
        print('\nResposta inválida!')

def main():
    pts_jogador = 0
    pts_pc = 0

    while True:
        j = ''
        primeiro = ''
        tabuleiro = [' '] * 9
        turnos = 1
        vencedor = ''

        tabuleiro_inicial = '''
--- COMO JOGAR ---

Quando for sua vez, digite o número correspondente à posição no tabuleiro para fazer sua jogada nela.

Por exemplo, digamos que você queira jogar no centro, então você digita 5.

     |     |     
  1  |  2  |  3  
_____|_____|_____
     |     |     
  4  |  5  |  6  
_____|_____|_____
     |     |     
  7  |  8  |  9  
     |     |     
    '''

        print(tabuleiro_inicial)

        print('Você quer ser o X (xis) ou a O (bola)?', end=' ')
        j = input('Digite X ou O e pressione Enter para escolher: ').strip().upper()
        adv = 'O' if j == 'X' else 'X'

        print('\nQuem joga primeiro?', end=' ')
        primeiro = input('Digite EU e pressione Enter para você começar, ou digite PC e pressione Enter para eu começar: ').strip().upper()

        if primeiro == 'PC':
            realizar_jogada_pc(adv, tabuleiro)
            exibir_tabuleiro(*tabuleiro)

        while turnos <= 5:
            realizar_jogada_jogador(j, tabuleiro)
            exibir_tabuleiro(*tabuleiro)
            if verificar_vencedor(j, adv, tabuleiro):
                break

            if turnos < 5:
                realizar_jogada_pc(adv, tabuleiro)
                exibir_tabuleiro(*tabuleiro)
                if verificar_vencedor(j, adv, tabuleiro):
                    break

            turnos += 1

        print('-------- PLACAR --------')
        print('Você: {} | Computador: {}'.format(pts_jogador, pts_pc))
        print('------------------------')

        if not jogar_novamente():
            sys.exit(0)

if __name__ == "__main__":
    main()
