from time import sleep
from random import randint

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.pont_total = 0
        self.pont_rodada = 0
        self.rodada_finalizada = False


    # Métodos get e set para pontuações

    def get_pont_total(self):
        return self.pont_total

    def att_pont_rodada(self, novo_valor):
        self.pont_rodada += novo_valor


    # Métodos de controle de rodada


    def fim_rodada(self, adicionar_rodada = 0):

        self.pont_total += adicionar_rodada
        print(f'\n[ Pontos ganhos nessa rodada: {adicionar_rodada} ]')
        self.rodada_finalizada = True
        self.pont_rodada = 0
        sleep(0.3)

    # Método de rolagem de dados

    def rolar_dados(self):
        if self.pont_rodada == 0:
            input('\nAperte Enter para rolar os dados\n')
            sleep(0.5)
        
        else:
            print('\nRolando os dados...\n')
            sleep(0.5)

        return randint(1,6)
    






class Jogo:
    def __init__(self):
        self.lista_jogadores = []
        self.index = 0
        self.contador_rodada = 1
        self.azar = 0
        self.vencedor = False



    def start_jogo(self):
        '''Pede número e nome de jogadores, cria objetos Jogador e adiciona-os à lista; Pede número de azar'''

        num_jogadores = int(input('entre com o numero de jogadores: '))

        for i in range(num_jogadores):

            nome = input(f'Nome do Jogador {i+1}: ')
            self.lista_jogadores.append(Jogador(nome))

        self.azar = int(input('Escolha o número do azar: '))



    def iniciar_rodada(self):

        jogador = self.lista_jogadores[self.index]

        print(f'{jogador.nome}, é a sua vez!')
        print(f'\n---------Rodada {self.contador_rodada}---------')
        return jogador



    def passar_jogador(self):

        if self.index < len(self.lista_jogadores) - 1:
            self.index += 1
        else:
            self.index = 0

        proximo_jogador = self.lista_jogadores[self.index]
        return proximo_jogador

    def finalizar_rodada(self):
        '''Atribui Jogo.index à 0'''

        self.index = 0
