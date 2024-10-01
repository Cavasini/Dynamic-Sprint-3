# 🏥 HealthTech Training Management System

Este projeto foi desenvolvido como parte do **Desafio HC Challenge** da **FIAP**. O objetivo é fornecer uma solução eficiente para o gerenciamento de dados e pontuações de sessões de treinamento médico, focado em estudantes, residentes, médicos e professores.

## 📋 Sumário
- [💡 Introdução](#💡-introdução)
- [✨ Funcionalidades](#✨-funcionalidades)
- [🛠️ Arquitetura](#🛠️-arquitetura)
- [🗄️ Banco de Dados](#🗄️-banco-de-dados)
- [🔍 Técnicas Utilizadas](#🔍-técnicas-utilizadas)
- [📊 Relatório de Performance](#📊-relatório-de-performance)
- [⚙️ Como Executar](#⚙️-como-executar)
- [👥 Contribuidores](#👥-contribuidores)

## 💡 Introdução
Este sistema gerencia dados de sessões de treinamento utilizando estruturas de dados eficientes como busca binária e árvores binárias. O objetivo é garantir um desempenho otimizado ao processar grandes volumes de dados, facilitando a análise e a avaliação de habilidades dos usuários em exercícios médicos, como em treinamento para laparoscopia.

## ✨ Funcionalidades
- Armazenamento de dados de sessões e pontuações dos usuários.
- Implementação de buscas eficientes em listas e árvores binárias.
- Geração de matrizes de dados e remoção de duplicatas.
- Avaliação de performance baseada no número de passos das operações de busca.
- Relatórios detalhados sobre o desempenho dos usuários.

## 🛠️ Arquitetura
A arquitetura do sistema segue uma abordagem em camadas, com as principais funcionalidades divididas em:
- **ServiceManager**: Responsável por gerenciar os serviços e conexões com o banco de dados.
  - **UsuarioService**: Gerencia operações relacionadas a usuários.
  - **ModuloTreinamentoService**: Manipula os módulos de treinamento.
  - **ExercicioService**: Gerencia exercícios de treinamento.
  - **SessaoService**: Administra as sessões de treinamento, coletando e armazenando resultados.

## 🗄️ Banco de Dados
O sistema utiliza um banco de dados relacional com as seguintes entidades principais:
- **Usuario**: Armazena informações dos usuários do sistema.
- **ModuloTreinamento**: Contém dados dos módulos de treinamento.
- **Exercicio**: Armazena os exercícios de treinamento.
- **Sessao**: Registra sessões de treinamento, incluindo pontuações e status.

## 🔍 Técnicas Utilizadas
- **Busca Binária**: Utilizada em listas ordenadas para garantir busca eficiente com complexidade O(log n).
- **Árvores Binárias**: Implementadas para garantir buscas rápidas em grandes volumes de dados dinâmicos.
- **Medição por Passos**: Cada operação de busca é medida pelo número de passos necessários para encontrar um valor, fornecendo insights sobre a eficiência do sistema.

## 📊 Relatório de Performance
O sistema gera relatórios com base no número de passos realizados nas operações de busca, o que auxilia na análise de eficiência e identificação de possíveis gargalos de performance. Esses dados podem ser utilizados para otimizar o balanceamento de árvores ou reordenar listas.

## ⚙️ Como Executar
1. Clone este repositório.
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
