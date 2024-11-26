from random import randint
from time import sleep
from funcoes import cadastro_jogador, obter_info_jogador, alterar_info_jogador

pont_total = 0 
pont_rodada = 0
lista_de_jogadores=[]
jogador_atual = ''

lista_de_jogadores = cadastro_jogador()


# Define o número que encerra a rodada
n_azar = int(input('Escolha o número do azar: '))





# Iteração que conta o número de rodadas e permite alternar entre jogadores na mesma rodada
n_rodada = 1


vencedor = False
# Estrutura responsável pela contagem de rodadas
while vencedor == False:
    print()
    print(f'----------Rodada {n_rodada}----------')
    input('Aperte Enter para iniciar a rodada')
    print()

    # Estrutura responsável por definir o jogador atual
    for index_jogador in range(len(lista_de_jogadores)):
        
        if pont_total >= 100:
            vencedor = True
            break
        else:

            pont_rodada = 0
            jogador_atual, pont_total = obter_info_jogador(lista_de_jogadores, index_jogador)



            # Uma tabela que mostra a pontuação dos jogadores
            print('TABELA')
            for c in range(len(lista_de_jogadores)):
                print(lista_de_jogadores[c]['nome'], end=' | ')
                print(lista_de_jogadores[c]['pontos'], 'pontos')
            print()



            print(f'---------| Vez de: {jogador_atual} | Pontuação: {pont_total} |---------')
            print()

            value = True
            while value == True:

                input('Aperte Enter para rolar')
                sleep(0.5)
                print()
                roll = randint(1,6)

                print(f'Você obteve {roll}')

                if roll == n_azar:
                    print('A pontuação da sua rodada foi perdida.')
                    print()
                    value = False

                else:
                    pont_rodada += roll
                    response = input(f'Pontos acumulados na rodada: {pont_rodada}. Deseja encerrar a sua rodada? [S/N] ')
                    print()
                    
                    if response.lower() in ('sim'):
                        alterar_info_jogador(pont_rodada, index_jogador, lista_de_jogadores)
                        break

                    else:
                        continue
            


    # Isso passa para a próxima rodada; Ainda está dentro da estrutura while vencedor
    n_rodada += 1



print(f'Temos um vencedor! {jogador_atual} alcançou {pont_total} pontos!')

# Uma tabela que mostra a pontuação dos jogadores
print('TABELA')
for c in range(len(lista_de_jogadores)):
    print(lista_de_jogadores[c]['nome'], end=' | ')
    print(lista_de_jogadores[c]['pontos'], 'pontos')