# arvores.py

# Função para inserir valores em uma árvore binária
def inserir_arvore(arvore, valor):
    # Se a árvore estiver vazia, crie um novo nó
    if not arvore:
        return [valor, None, None]

    # Se o valor a ser inserido for menor que o valor do nó atual, insira na subárvore esquerda
    if valor < arvore[0]:
        arvore[1] = inserir_arvore(arvore[1], valor)
    # Se o valor a ser inserido for maior que o valor do nó atual, insira na subárvore direita
    elif valor > arvore[0]:
        arvore[2] = inserir_arvore(arvore[2], valor)
    else:
        # Se o valor já existe na árvore, não faça nada ou trate de outra forma
        print(f"Valor {valor} já existe na árvore e não será inserido.")  # Para depuração

    return arvore

# Função para construir a árvore binária a partir de uma lista
def construir_arvore_binaria(lista):
    arvore = None
    for valor in lista:
        arvore = inserir_arvore(arvore, valor)  # Insere cada valor na árvore
    return arvore

# Função para buscar um valor na árvore binária e contar os passos
def buscar_arvore(arvore, valor):
    passos = 0
    while arvore:
        passos += 1
        if valor == arvore[0]:
            return True, passos
        elif valor < arvore[0]:
            arvore = arvore[1]  # Subárvore esquerda
        else:
            arvore = arvore[2]  # Subárvore direita
    return False, passos

# Função para buscar sessão na árvore binária
def buscar_sessao_arvore(arvore, valor_sessao):
    encontrado, passos = buscar_arvore(arvore, valor_sessao)
    if encontrado:
        return f"Sessão {valor_sessao} encontrada com {passos} passos (árvore binária)."
    return f"Sessão {valor_sessao} não encontrada após {passos} passos (árvore binária)."

# Função para buscar usuário na árvore binária
def buscar_usuario_arvore(arvore, valor_usuario):
    encontrado, passos = buscar_arvore(arvore, valor_usuario)
    if encontrado:
        return f"Usuário {valor_usuario} encontrado com {passos} passos (árvore binária)."
    return f"Usuário {valor_usuario} não encontrado após {passos} passos (árvore binária)."
