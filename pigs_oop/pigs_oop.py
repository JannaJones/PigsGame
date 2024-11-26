# %%

from pacote.v1_0_classes import Jogador

# Pigs destinado a prática de POO em Python.

jogador = Jogador()

azar = int(input('Escolha o número do azar: '))

while jogador.get_pont_total() < 100:

    jogador.iniciar_rodada()

    while True:

        rolagem = jogador.rolar_dados()
        print(f'Você obteve {rolagem}')

        if rolagem == azar:
            print('A pontuação da rodada foi perdida. Iniciando a próxima rodada...')
            jogador.finalizar_rodada()
            break

        else:
            jogador.att_pont_rodada(rolagem)
            resposta = input(f'Pontos acumulados na rodada: {jogador.pont_rodada}. Deseja encerrar a rodada? [S/N] ')
            
            if resposta in ['s', 'sim']:
                jogador.finalizar_rodada(jogador.pont_rodada)
                break

print('Você alcançou os 100 pontos e venceu!')
# %%
