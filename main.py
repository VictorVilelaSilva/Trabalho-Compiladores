import json
import re
from typing import List

from enum import Enum

#####################################Analisador Léxico (Pascal)################################
# percorre o arquivo e retorna os tokens

padrao = r'([a-zA-Z][a-zA-Z0-9_]*|<>|==|:=|>=|<=|<|>|:|[\d.]+|[a-zA-Z0-9]+|\S)'

def variableBuilded(variableRegex, variaveis, buildedVariable,palavrasReservadas,linha,coluna,lista,line):
    if buildedVariable != "" and re.fullmatch(variableRegex, buildedVariable) and (buildedVariable not in palavrasReservadas) :
        coluna = line.find(buildedVariable)
        variaveis.append(['tkn_variaveis',buildedVariable,linha,coluna+1])
        lista.append(['tkn_variaveis',buildedVariable,linha,coluna+1])
        return True
    elif buildedVariable != "" and buildedVariable in palavrasReservadasRegras:
        coluna = line.find(buildedVariable)
        palavrasReservadas.append(['tkn_palavras_reservadas',buildedVariable,linha,coluna+1])
        lista.append(['tkn_palavras_reservadas',buildedVariable,linha,coluna+1])
        return True
    return False

def is_integer(s):
    return s.isdigit()

def is_float(s):
    try:
        float_value = float(s)
        return True
    except ValueError:
        return False

def getTokens(pascalExerciseContent: str) -> List[dict]:

    intRegex = r'^[0-9]+$'
    floatRegex = r'[0-9]+\.[0-9]+'
    variableRegex = r'[a-zA-Z][a-zA-Z0-9_]*'
    # variableRegex = r'^[a-zA-Z][a-zA-Z0-9]*$'

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
    variableBuilder = ""
    numero = ""
    
    
    linha = 0
    coluna = 0
    modoString = False
    dentroComentario = False

    for line in pascalExerciseContent.split('\n'):
        linha += 1
        coluna = 0

        # verifica se a linha é um comentário
        tempLine = line.lstrip()

        if(tempLine.startswith('//')):
            coluna = line.find(word)
            comentariosArray.append(['tkn_comentarios',tempLine,linha,coluna+1])
            coluna = line.find(word)
            lista.append(['tkn_comentarios',tempLine,linha,coluna+1])
            
            linha += 1 #talves possa ocorer problemas aqui
            continue

        # percorre a linha por palavra
        for word in re.findall(padrao, line):
           
            # if not line.startswith(word) and not word.isspace(): 
                
            #faz com que ocorra uma espaco entre as palavras da string
            if(modoString):
                string += " "
                
            
            # verifica se a palavra é uma palavra reservada
            if (word in palavrasReservadasRegras) and not modoString and not dentroComentario:
                coluna = line.find(word)
                palavrasReservadas.append(['tkn_palavras_reservadas',word,linha,coluna+1])
                lista.append([obter_valor_simbolo(word),word,linha,coluna+1])
                coluna += (len(word))
                continue
            elif (is_float(word)):
                coluna = line.find(word)
                simbolo = 'tkn_float'
                lista.append([obter_valor_simbolo(simbolo), word,linha,coluna+1])
                coluna += (len(word))
                continue
            
            elif (is_integer(word)):
                coluna = line.find(word)
                simbolo = 'tkn_int'
                lista.append([obter_valor_simbolo(simbolo), word,linha,coluna+1])
                coluna += (len(word))
                continue
            
            
            # verifica se a palavra não é uma palavra reservada e é uma variável
            elif (word not in palavrasReservadasRegras) and (word not in tokensLogicosRelacionaisAtriRegras)and (re.fullmatch(variableRegex, word) and not modoString and not dentroComentario):
                coluna = line.find(word)
                simbolo = 'tkn_variaveis'
                lista.append([obter_valor_simbolo(simbolo),word,linha,coluna+1])
                coluna += (len(word))
                continue

            # verifica se a palavra é um tokensLogicosRelacionaisAtri
            elif (word in tokensLogicosRelacionaisAtriRegras) and not modoString and not dentroComentario:
                coluna = line.find(word)
                if(word == "<>"):
                    simbolo = 'tkn_maiormenor'
                    coluna += 1
                elif(word == ">"):
                    simbolo = 'tkn_maior'
                    coluna += 1
                elif(word == ">="):
                    simbolo = 'tkn_maiorigual'
                    coluna += 1
                elif(word == "<"):
                    simbolo = 'tkn_menor'
                    coluna += 1
                elif(word == "<="):
                    simbolo = 'tkn_menorigual'
                    coluna += 1
                elif(word == ":="):
                    simbolo = 'tkn_atribuicao'
                    coluna += 1
                elif(word == "=="):
                    simbolo = 'tkn_igualdade'
                    coluna += 1  
                lista.append([obter_valor_simbolo(simbolo),word,linha,coluna])
                coluna += (len(word))
                continue
            
            # verifica se o caractere é um tokensAritimeticos
            elif (word in tokensAritimeticosRegras) and not modoString and not dentroComentario:
                coluna = line.find(word)
                if(word == "+"):
                    simbolo = "tkn_adicao"
                elif(word == "-"):
                    simbolo = "tkn_subtracao"
                elif(word == "*"):
                    simbolo = "tkn_multiplicacao"
                elif(word == "/"):
                    simbolo = "tkn_divisao"
                lista.append([obter_valor_simbolo(simbolo),word,linha,coluna+1])
                continue
            # verifica se o caractere é um tokenSimbolo
            elif(word in tokensSimbolosRegras) and not modoString and not dentroComentario:
                if(word == ";"):
                    simbolo = "tkn_pontoevirgula"
                    coluna+=1
                elif(word == ","):
                        simbolo = "tkn_virgula"
                        coluna+=1
                elif(word == "."):
                        simbolo = "tkn_ponto"
                        coluna+=1
                elif(word == ":"):
                        simbolo = "tkn_doispontos"
                        coluna+=1
                elif(word == "("):
                        simbolo = "tkn_abreparentese"
                        coluna+=1
                elif(word == ")"):
                        simbolo = "tkn_fechaparentese"
                        coluna+=1
                lista.append([obter_valor_simbolo(simbolo),word,linha,coluna])
                continue
            
            # percorre a palavra por caractere
            for caractere in word:
            
                # verifica se esta no modo string
                if modoString:
                    string+=caractere
                    if caractere == "'":
                        modoString = False
                        coluna += 1
                        stringsArray.append(['tkn_string',string[:-1],linha,coluna+1])
                        simbolo = 'tkn_string'
                        lista.append([obter_valor_simbolo(simbolo),string[:-1],linha,coluna+1])
                        string = ""
                    continue  
               
                # verifica se o caractere é um espaço
                if (caractere == r'\s'):
                    if variableBuilded(variableRegex, variaveis, variableBuilder, palavrasReservadas,linha,coluna,lista,line):
                        variableBuilder = "" 
                        continue

                # verifica se o caractere é um string
                elif caractere == "'" and not dentroComentario:
                    stringStart = line.find(caractere)
                    linhaString = linha
                    modoString = True
                    continue
                
                # ativa o modo de comentario
                elif (caractere == '{') and not modoString and not dentroComentario:
                    dentroComentario = True
                    textoComentario = caractere  # Inicia o texto do comentário com '{'
                    
                    continue
            
                # Se estiver dentro de um comentário, acumula o texto
                elif dentroComentario:
                    textoComentario += caractere  # Acumula texto do comentário
                    
                    if caractere == '}':
                        dentroComentario = False
                        coluna = line.find(word)
                        comentariosArray.append(['tkn_comentario',textoComentario,linha,coluna+1])  # Adiciona o comentário acumulado ao array
                        coluna = line.find(word)
                        simbolo = 'tkn_comentario'
                        lista.append([obter_valor_simbolo(simbolo),textoComentario,linha,coluna+1])  # Adiciona o comentário acumulado ao array
                        textoComentario = ""  # Reinicia para o próximo comentário
                    continue

                else:
                    indice = line.find(word)
                    print(f"Erro na linha {linha} coluna {indice}")
                    print(line)
                    #indicar a linha exata da linha
                    print(" "*(indice) + "^")
                    print("Erro: Lexema inválido")
                    exit() 
            
            

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
    '==' 
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

class Tokens(Enum):
    PROGRAM = 1
    VAR = 2
    INTEGER = 3
    REAL = 4
    STRING = 5
    BEGIN = 6
    BOOLEAN = 7
    END = 8
    FOR = 9
    TO = 10
    WHILE = 11
    DO = 12
    BREAK = 13
    CONTINUE = 14
    IF = 15
    ELSE = 16
    THEN = 17
    WRITE = 18
    READ = 19
    OR = 20
    AND = 21
    NOT = 22
    MOD = 23
    DIV = 24
    TKN_VARIAVEIS = 100
    TKN_INT = 101
    TKN_MAIORMENOR = 102
    TKN_MAIOR = 103
    TKN_MAIORIGUAL = 104
    TKN_MENOR = 105
    TKN_MENORIGUAL = 106
    TKN_ATRIBUICAO = 107
    TKN_ADICAO = 108
    TKN_SUBTRACAO = 109
    TKN_MULTIPLICACAO = 110
    TKN_DIVISAO = 111
    TKN_FLOAT = 112
    TKN_PONTOEVIRGULA = 113
    TKN_VIRGULA = 114
    TKN_PONTO = 115
    TKN_DOISPONTOS = 116
    TKN_ABREPARENTESE = 117
    TKN_FECHAPARENTESE = 118
    TKN_COMENTARIO = 119
    TKN_STRING = 120
    TKN_IGUALDADE = 121
    

def obter_valor_simbolo(simbolo):
    try:
        enum_simbolo = Tokens[simbolo.upper()]
        return enum_simbolo.value
    except KeyError:
        return None

diretorio = r'listas\lista1\EXS1.pas'

pascalExercise = open( diretorio, 'r')
pascalExerciseContent = pascalExercise.read()

tokenDict,lista = getTokens(pascalExerciseContent)

resultadoJsom = json.dumps(lista)
criarArquivo = open('resultado.json', 'w')
criarArquivo.write(resultadoJsom)
#passar resultado para JSON
