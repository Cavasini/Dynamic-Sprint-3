import matrizes
import arvores
import random

# Exemplo de uso
qtd_dados = 500  # Total de números aleatórios
qtd_colunas = 10  # Colunas da matriz

# Criando a matriz com números aleatórios
matriz_sessoes = matrizes.preencher_matriz_aleatoria(qtd_dados // 10, qtd_colunas)
matriz_usuarios = matrizes.preencher_matriz_aleatoria(qtd_dados // 10, qtd_colunas)


# Organizando as matrizes e transformando em lista, removendo duplicatas
lista_sessoes_ordenada = matrizes.organizar_matriz(matriz_sessoes)
lista_usuarios_ordenada = matrizes.organizar_matriz(matriz_usuarios)


# Construindo as árvores binárias a partir das listas ordenadas
arvore_sessoes = arvores.construir_arvore_binaria(lista_sessoes_ordenada)
arvore_usuarios = arvores.construir_arvore_binaria(lista_usuarios_ordenada)

# Escolhendo um valor aleatório para buscar na lista
valor_sessao_procurado = random.choice(lista_sessoes_ordenada)  # Escolhe um valor existente na lista
valor_usuario_procurado = random.choice(lista_usuarios_ordenada)  # Escolhe um valor existente na lista

print(f"\nBuscando a sessão: {valor_sessao_procurado}")
# Buscando a sessão na lista ordenada
resultado_sessao_lista = matrizes.buscar_sessao(lista_sessoes_ordenada, valor_sessao_procurado)
print(resultado_sessao_lista)
# Buscando a sessão e o usuário na árvore binária
resultado_sessao_arvore = arvores.buscar_sessao_arvore(arvore_sessoes, valor_sessao_procurado)
print(resultado_sessao_arvore)

print(f"\nBuscando o usuário: {valor_usuario_procurado}")
# Buscando o usuário na lista ordenada
resultado_usuario_lista = matrizes.buscar_usuario(lista_usuarios_ordenada, valor_usuario_procurado)
print(resultado_usuario_lista)


resultado_usuario_arvore = arvores.buscar_usuario_arvore(arvore_usuarios, valor_usuario_procurado)
print(resultado_usuario_arvore)
