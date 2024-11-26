# %% Usando listas

from pacote.v1_1_classes import Jogador, Jogo

j = Jogo()
j.start_jogo()
jogador = j.lista_jogadores[j.index]



while j.vencedor == False:


    while jogador.get_pont_total() < 100:

        if jogador.pont_rodada == 0:
            print(f'\n\n-=-=-=-=-=-=-= {jogador.nome}, é sua vez! =-=-=-=-=-=-=-=-=')
            print(f'\nTotal de pontos: {jogador.pont_total}')

        rolagem = jogador.rolar_dados()
        print(f'Você obteve {rolagem}')

        if jogador.pont_total + rolagem >= 100:
            j.vencedor = True
            break

        if rolagem == j.azar:
            print('A pontuação da rodada foi perdida. Iniciando a próxima rodada...')
            jogador.fim_rodada()
            jogador = j.passar_jogador()
            break

        else:
            jogador.att_pont_rodada(rolagem)
            resposta = input(f'Pontos acumulados na rodada: {jogador.pont_rodada}. Deseja encerrar a rodada? (s p/encerrar) ')
            
            if resposta in ['s', 'sim']:
                jogador.fim_rodada(jogador.pont_rodada)
                jogador = j.passar_jogador()
                break


print('Você alcançou os 100 pontos e venceu!')