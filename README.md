# Projeto Mini Pascal Compiler

Este projeto é um compilador para uma linguagem de programação similar ao Pascal, chamada Mini Pascal. O compilador é escrito em Python e é capaz de analisar, processar e compilar programas escritos em Mini Pascal.

## Estrutura do Projeto

A estrutura do projeto é a seguinte:

### Principais Arquivos e Diretórios

- **main.py**: Arquivo principal que coordena o processo de compilação.
- **p1main.py, p2main.py, p3main.py**: Módulos que implementam diferentes fases do compilador (análise léxica, sintática, etc.).
- **Helpers/**: Diretório contendo funções e classes auxiliares.
    - **mainHelper.py**: Define a classe `FunctionsClass` com funções auxiliares.
    - **mainToken.py**: Contém a definição dos tokens utilizados pelo analisador léxico.
- **Parte4/**: Diretório contendo implementação adicional do compilador.
    - **parte4.py**: Módulo com funcionalidades avançadas ou específicas da quarta parte do projeto.
- **listas/**: Contém exemplos de programas em Mini Pascal para teste.
- **miniPascal.gmr**: Arquivo de gramática da linguagem Mini Pascal.

## Funcionalidades

- **Análise Léxica**: Identifica e classifica tokens no código fonte.
- **Análise Sintática**: Verifica a estrutura do código de acordo com a gramática definida.
- **Análise Semântica**: Realiza verificações semânticas, como declarações de variáveis e tipos.
- **Geração de Código**: Gera código intermediário ou código objeto a partir da análise do código fonte.

## Testes

Dentro do diretório `listas`, você encontrará vários exemplos de programas em Mini Pascal que podem ser utilizados para testar o compilador. Para executar um desses programas:

1. Abra o arquivo `main.py`.
2. Modifique o trecho do código que lê o arquivo de entrada para apontar para o programa desejado.
3. Execute o compilador conforme as instruções anteriores.