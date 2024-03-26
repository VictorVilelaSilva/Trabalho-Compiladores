# Pascal Lexical Analyzer

Este projeto é um analisador léxico para a linguagem de programação Pascal, implementado em Python. Ele analisa um arquivo Pascal `.pas` e extrai os tokens, seguindo as especificações da linguagem.

## Pré-requisitos

Antes de começar, certifique-se de ter o Python instalado em seu sistema. Este projeto foi testado com Python 3.8.

## Uso

Para usar o analisador léxico, execute o script `main.py` passando o caminho do arquivo Pascal como argumento:


Exemplo:

python main.py <localAquivo>

O script irá processar o arquivo e imprimir a lista de tokens no terminal. Um arquivo `resultado.json` também será gerado no diretório atual com os tokens analisados.


## Estrutura do Projeto

O projeto consiste em três arquivos principais:

- `main.py`: Contém o ponto de entrada do script e a lógica para ler arquivos e chamar o analisador léxico.
- `functions.py`: Fornece funções auxiliares para o processo de análise léxica, como a verificação de tipos de tokens e a manipulação de erros.
- `classTokens.py`: Define uma enumeração `Tokens` que mapeia os tipos de tokens para valores numéricos.



