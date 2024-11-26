def cadastro_jogador():
    """Pergunta quantas pessoas vão jogar. Retorna lista com
    dicionários contendo informações de cada jogador.
    Lista = [{'nome': 'jogador n', 'pontos': 0}, ...]"""

    print('----------Cadastro de jogador----------')
    print()
    
    n_jogadores = int(input('Quantas pessoas vão jogar? '))
    lista_jog = []

    for c in range(n_jogadores):
        jogador_dict = {'nome': f'jogador {c+1}', 'pontos': 0}
        lista_jog.append(jogador_dict)
     
    return lista_jog
        


def obter_info_jogador(lista_de_jogadores, index):
    """ Função que retira os dados 'nome' e 'pontos' da lista_de_jogadores. Requer (lista_de_jogadores, index). Retorna nome e pontuacao"""
    
    nome = lista_de_jogadores[index]['nome']
    pontuacao = lista_de_jogadores[index]['pontos']
    return nome, pontuacao



def alterar_info_jogador(adicionar_pontuacao, n_jogador, lista_de_jogadores):
    """ Recebe o valor de pontuação da rodada, número do jogador e a lista como um todo. Adiciona a pontuação ao jogador especificado """
    
    lista_de_jogadores[n_jogador]['pontos'] += adicionar_pontuacao