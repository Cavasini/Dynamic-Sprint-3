import random

# Função para preencher matriz com dados aleatórios
def preencher_matriz_aleatoria(qtd_linhas, qtd_colunas):
    matriz = []
    for _ in range(qtd_linhas):
        linha = [random.randint(1, 1000) for _ in range(qtd_colunas)]  # Gera números aleatórios
        matriz.append(linha)
    return matriz

# Função para organizar a matriz em uma lista e remover duplicatas
def organizar_matriz(matriz):
    conjunto = set()  # Usando um conjunto para evitar duplicatas
    for linha in matriz:
        conjunto.update(linha)  # Adiciona todos os números da linha ao conjunto
    
    lista = sorted(conjunto)  # Converte o conjunto em uma lista e ordena
    return lista

# Função para realizar busca binária em uma lista com contagem de passos
def busca_binaria(lista, valor):
    esquerda, direita = 0, len(lista) - 1
    passos = 0
    while esquerda <= direita:
        passos += 1
        meio = (esquerda + direita) // 2
        if lista[meio] == valor:
            return meio, passos
        elif lista[meio] < valor:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1, passos  # Retorna -1 se não encontrado

# Função para buscar uma sessão específica
def buscar_sessao(lista, valor_sessao):
    indice, passos = busca_binaria(lista, valor_sessao)
    if indice != -1:
        return f"Sessão {valor_sessao} encontrada na posição {indice}, com {passos} passos (busca binária)."
    return f"Sessão {valor_sessao} não encontrada após {passos} passos."

# Função para buscar um usuário específico
def buscar_usuario(lista, valor_usuario):
    indice, passos = busca_binaria(lista, valor_usuario)
    if indice != -1:
        return f"Usuário {valor_usuario} encontrado na posição {indice}, com {passos} passos (busca binária)."
    return f"Usuário {valor_usuario} não encontrado após {passos} passos."
