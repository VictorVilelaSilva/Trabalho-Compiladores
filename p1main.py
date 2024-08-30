import sys
sys.path.append('..')
from Helpers.mainHelper import FunctionsClass
import json
import re
from typing import List


#####################################Analisador Léxico (Pascal)################################
# percorre o arquivo e retorna os tokens
helper = FunctionsClass()
padrao = r"(\d+[a-zA-Z_][a-zA-Z0-9_]*|[a-zA-Z_][a-zA-Z0-9_]*|<>|=|:=|>=|<=|<|>|:|[\d.]+|'[^']*'| |\S)"

def getTokens(pascalExerciseContent: str) -> List[dict]:

    variableRegex = r'[a-zA-Z][a-zA-Z0-9_]*'
    TokensAritimeticos = {
        "+": "tkn_adicao",
        "-": "tkn_subtracao",
        "*": "tkn_multiplicacao",
        "/": "tkn_divisao"
    }

    TokensSimbolos = {
        ";": "tkn_pontoevirgula",
        ",": "tkn_virgula",
        ".": "tkn_ponto",
        ":": "tkn_doispontos",
        "(": "tkn_abreparentese",
        ")": "tkn_fechaparentese"
    }

    TokensLogicos = {
        "<>": "tkn_maiormenor",
        ">": "tkn_maior",
        ">=": "tkn_maiorigual",
        "<": "tkn_menor",
        "<=": "tkn_menorigual",
        ":=": "tkn_atribuicao",
        "=": "tkn_igualdade"
    }

    lista = []
    tokensAritimeticos = []
    tokensLogicosRelacionaisAtri = []
    palavrasReservadas = []
    tokensSimbolos = []
    variaveis = []
    stringsArray = []
    inteirosArray = []
    comentariosArray = []
    floatsArray = []
    string = ""
    comentario2 = ""
    
    
    linha = 0
    coluna = 0
    linhaString = 0
    stringStart = 0
    linhaComentario = 0
    colunaComentario = 0

    modoString = False
    dentroComentario = False

    for line in pascalExerciseContent.split('\n'):
        linha += 1
        coluna = 1

        # verifica se a linha é um comentário
        tempLine = line.lstrip()

        if (modoString):
            helper.errorCatchString(linhaString, stringStart, actualLine)

        if(tempLine.startswith('//')):
            coluna = coluna+2
            simbolo = 'tkn_comentario'
            continue


        # percorre a linha por palavra
        for word in re.findall(padrao, line):
           
            if(word == ' '):
                coluna = coluna+1
                if(modoString):
                    string += " "
                elif(dentroComentario):
                    comentario2 += " "
                continue
            
            if(word == '/' and line[coluna-1] == '/'):
                #percorre até o final da linha para pegar o comentario
                comentario = line[coluna-1:]
                break

            if(word.startswith("{") or dentroComentario):
                dentroComentario = True
                lineComentario = line
                if(line.endswith("}")):
                    dentroComentario = False
                    comentario2 = line[coluna-1:]
                    break
                elif(word.endswith("}")):
                    dentroComentario = False
                    comentario2 += word
                    break
                comentario2 += word
                continue
                
                
            if(word.startswith("'")):
                if(word.endswith("'")):
                    stringsArray.append(['tkn_string',word,linha,coluna])
                    lista.append([helper.obter_valor_simbolo('tkn_string'),word,linha,coluna])
                    coluna += (len(word))
                    continue
                else:
                    stringStart = coluna
                    linhaString = linha
                    actualLine = line
                    string += word[1:]
                    modoString = True
                    continue
            

            elif(modoString):
                string += " " + word
                if(word.endswith("'")):
                    stringsArray.append(['tkn_string',string,linhaString,stringStart])
                    lista.append([helper.obter_valor_simbolo('tkn_string'),string,linhaString,stringStart])
                    coluna += (len(word))
                    string = ""
                    modoString = False
                continue
                
            # verifica se a palavra é uma palavra reservada
            if (word in palavrasReservadasRegras) and not dentroComentario:
                lista.append([helper.obter_valor_simbolo(word),word,linha,coluna])
                coluna += (len(word))
                continue

            elif (helper.is_float(word)):
                simbolo = 'tkn_float'
                word += '0'  # adicionar float
                lista.append([helper.obter_valor_simbolo(simbolo), word,linha,coluna])
                coluna += (len(word))
                continue
            
            elif (helper.is_integer(word)):
                simbolo = 'tkn_int'
                lista.append([helper.obter_valor_simbolo(simbolo), word,linha,coluna])
                coluna += (len(word))
                continue
            
            
            # verifica se a palavra não é uma palavra reservada e é uma variável
            elif (word not in palavrasReservadasRegras) and (word not in tokensLogicosRelacionaisAtriRegras)and (re.fullmatch(variableRegex, word) and not dentroComentario):

                simbolo = 'tkn_variaveis'
                lista.append([helper.obter_valor_simbolo(simbolo),word,linha,coluna])
                coluna += (len(word))
                continue

            # verifica se a palavra é um tokensLogicosRelacionaisAtri
            elif (word in tokensLogicosRelacionaisAtriRegras) and not dentroComentario:
                simbolo = TokensLogicos[word]
                lista.append([helper.obter_valor_simbolo(simbolo),word,linha,coluna])
                coluna += (len(word))
                continue
            
            # verifica se o caractere é um tokensAritimeticos
            elif (word in tokensAritimeticosRegras) and not dentroComentario:
                simbolo = TokensAritimeticos[word]
                lista.append([helper.obter_valor_simbolo(simbolo),word,linha,coluna])
                coluna += (len(word))
                continue
            # verifica se o caractere é um tokenSimbolo
            elif(word in tokensSimbolosRegras) and not dentroComentario:
                simbolo = TokensSimbolos[word]
                lista.append([helper.obter_valor_simbolo(simbolo),word,linha,coluna])
                coluna += (len(word))
                continue
            
            # percorre a palavra por caractere
            for caractere in word:
                # coluna += 1

                # verifica se o caractere é um espaço
                if (caractere == r'\s'):
                    continue

                # ativa o modo de comentario
                elif (caractere == '{') and not dentroComentario:
                    dentroComentario = True
                    linhaComentario = linha
                    colunaComentario = coluna
                    lineComentario = line
                    textoComentario = caractere  # Inicia o texto do comentário com '{'
                    
                    continue
            
                # Se estiver dentro de um comentário, acumula o texto
                elif dentroComentario:
                    textoComentario += caractere  # Acumula texto do comentário
                    
                    if caractere == '}':
                        dentroComentario = False
                        simbolo = 'tkn_comentario'
                        textoComentario = ""  # Reinicia para o próximo comentário
                    continue

                else:
                    helper.errorCatch(linha, line, word) 
    if(dentroComentario):
        helper.errorCatchComentario(linhaComentario, colunaComentario, lineComentario)        
            

    tokensDict = {
        'tokensAritimeticos': tokensAritimeticos,
        'tokensLogicosRelacionaisAtri' : tokensLogicosRelacionaisAtri,
        'palavrasReservadas' : palavrasReservadas,
        'tokensSimbolos' : tokensSimbolos,
        'variaveis' : variaveis,
        'strings' : stringsArray,
        'inteiros' : inteirosArray,
        'floats' : floatsArray,
        'comentarios' : comentariosArray
    }
    return tokensDict, lista



tokensAritimeticosRegras: List[str] = [
    '+',
    '-',
    '*',
    '/'
]

tokensLogicosRelacionaisAtriRegras: List[str]  = [
    '<>',
    '>',
    '>=',
    '<',
    '<=',
    ':=',
    '=' 
]

palavrasReservadasRegras: List[str] = [
    'program',	
    'var',
    'integer',
    'real',
    'string',
    'begin',
    'boolean',
    'end',
    'for',
    'to',
    'while',
    'do',
    'breal',
    'continue',
    'if',
    'else',
    'then',
    'write',
    'read',
    'mod',
    'div',
    'or',
    'and',
    'not',
]

tokensSimbolosRegras: List[str] = [
    ';',
    ',',
    '.',
    ':',
    '(',
    ')',
]

def analisadorLexico(arquivo):
    # Abre o arquivo informado como argumento
    try:
        with open(arquivo, 'r') as pascalExercise:
            pascalExerciseContent = pascalExercise.read()
        
        tokenDict, lista = getTokens(pascalExerciseContent)

        resultadoJson = json.dumps(lista)
        with open('resultado.json', 'w') as criarArquivo:
            criarArquivo.write(resultadoJson)

        return lista


            
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        analisadorLexico(sys.argv[1])
    else:
        print("Erro: Informe o arquivo a ser analisado.")
        print("Exemplo: python3 p1main.py arquivo.pas")
        exit()