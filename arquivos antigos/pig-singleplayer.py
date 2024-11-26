# %%
from random import randint
from time import sleep

pont_total = 0 
n_rodada = 0
pont_rodada = 0

# Funções

def rolagem_dados(pont_rodada):
    """Responsável pela rolagem de dados. pont_rodada é usado para verificar
    se é a primeira rolagem da rodada. Retorna um valor entre 1 e 6"""

    if pont_rodada == 0:
        input('Aperte Enter para rolar os dados ')
        print()
        sleep(0.5)
        roll = randint(1,6)
        return roll
    else:
        sleep(0.5)
        roll = randint(1,6)
        return roll




# Define o número que encerra a rodada
n_azar = int(input('Escolha o número do azar: '))

# encerra quando chegar a 100 pontos
while pont_total < 100:
    
    n_rodada += 1
    print(f'---------Rodada {n_rodada}---------') #reset da rodada 
    pont_rodada = 0
    print(f'Total de pontos: {pont_total}')

    while True:
        
        roll = rolagem_dados(pont_rodada)

        print(f'Você obteve {roll}')
        
        if roll == n_azar:
            print('A pontuação da rodada foi perdida. Iniciando a próxima rodada...')
            print()
            sleep(0.5)
            break
        else:
            pont_rodada += roll
            response = input(f'Pontos acumulados na rodada: {pont_rodada}. Deseja encerrar a rodada? [S/N] ')
            print()
            if response.lower() in ('sim'):
                pont_total += pont_rodada
                break
            else:
                print('Rolando os dados...')
                print()
                sleep(0.5)
                continue

print('Você alcançou os 100 pontos e venceu!')
# %%
