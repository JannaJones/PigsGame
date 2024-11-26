from time import sleep
from random import randint

class Jogador:
    def __init__(self):
        self.pont_total = 0
        self.pont_rodada = 0
        self.n_rodada = 1


    # Métodos get e set para pontuações

    def get_pont_total(self):
        return self.pont_total

    def att_pont_rodada(self, novo_valor):
        self.pont_rodada += novo_valor


    # Métodos de controle de rodada

    def iniciar_rodada(self):
        print(f'\n---------Rodada {self.n_rodada}---------')
        print(f'Total de pontos: {self.pont_total}')


    def finalizar_rodada(self, adicionar_rodada = 0):

        self.pont_total += adicionar_rodada
        print(f'\n[ Pontos ganhos nessa rodada: {adicionar_rodada} ]')
        self.pont_rodada = 0
        self.n_rodada += 1
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