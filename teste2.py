import json
import re
from typing import List

from enum import Enum

#####################################Analisador Léxico (Pascal)################################
# percorre o arquivo e retorna os tokens

padrao = r'([a-zA-Z][a-zA-Z0-9_]*|<>|:=|>=|<=|<|>|[a-zA-Z0-9]+|\S)'

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
                coluna =+ (len(word))
                continue
            
            elif (is_integer(word)):
                coluna = line.find(word)
                lista.append(['tkn_inteiro', word,linha,coluna+1])
                coluna =+ (len(word))
                continue
            
            # verifica se a palavra não é uma palavra reservada e é uma variável
            elif (word not in palavrasReservadasRegras) and (word not in tokensLogicosRelacionaisAtriRegras)and (re.fullmatch(variableRegex, word) and not modoString and not dentroComentario):
                if(word[-1] == ';'):
                    coluna = line.find(word)
                    variaveis.append(word)
                    lista.append(['tkn_variaveis',word,linha,coluna+1])
                    coluna = line.find(word-1)
                    tokensSimbolos.append(['tkn_simbolo',word-1,linha,coluna+1])
                    lista.append(['tkn_simbolo',word-1,linha,coluna+1])
                    continue
                coluna = line.find(word)
                variaveis.append(['tkn_variaveis',word,linha,coluna+1])
                coluna = line.find(word)
                lista.append(['tkn_variaveis',word,linha,coluna+1])
                coluna =+ (len(word))
                continue

            # verifica se a palavra é um tokensLogicosRelacionaisAtri
            elif (word in tokensLogicosRelacionaisAtriRegras) and not modoString and not dentroComentario:
                coluna = line.find(word)
                tokensLogicosRelacionaisAtri.append(['tkn_logicos_relacionais_atributos',word,linha,coluna+1])
                coluna = line.find(word)
                lista.append(['tkn_logicos_relacionais_atributos',word,linha,coluna+1])
                coluna =+ (len(word))
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
                        lista.append(['tkn_string',string[:-1],linha,coluna+1])
                        string = ""
                    continue  
               
                # verifica se o caractere é um espaço
                if (caractere == r'\s'):
                    if variableBuilded(variableRegex, variaveis, variableBuilder, palavrasReservadas,linha,coluna,lista,line):
                        variableBuilder = "" 
                        continue
                
                # verifica se o caractere é um tokensAritimeticos
                if (caractere in tokensAritimeticosRegras) and not modoString and not dentroComentario:
                    coluna += 1
                    tokensAritimeticos.append(['tkn_aritimetico',caractere,linha,coluna+1])
                    lista.append(['tkn_aritimetico',caractere,linha,coluna+1])
                    if variableBuilded(variableRegex, variaveis, variableBuilder, palavrasReservadas,linha,coluna,lista,line):
                        variableBuilder = "" 
                        continue
                    continue

                # verifica se o caractere é um tokensLogicosRelacionaisAtri
                elif (caractere in tokensLogicosRelacionaisAtriRegras) and not modoString and not dentroComentario:
                    #achar a possição do caractere na linha
                    posicao = line.find(caractere)
                    newCaractere = caractere+line[posicao+1]
                    if  (newCaractere  in tokensLogicosRelacionaisAtriRegras):
                        coluna += 1
                        tokensLogicosRelacionaisAtri.append(['tkn_logicos_relacionais_atributos',newCaractere, linha, coluna])
                        lista.append(['tkn_logicos_relacionais_atributos',newCaractere, linha, coluna])
                        variableBuilder = ""  # Reinicia para o próximo número
                        continue
                    coluna += 1
                    tokensLogicosRelacionaisAtri.append(['tkn_logicos_relacionais_atributos',caractere,linha,coluna+1])
                    lista.append(['tkn_logicos_relacionais_atributos',caractere,linha,coluna+1])
                    if variableBuilded(variableRegex, variaveis, variableBuilder, palavrasReservadas,linha,coluna,lista,line):
                        variableBuilder = "" 
                        continue
                    continue
                    
                # Se não é um dígito, mas temos um número acumulado, verifique se é um flutuante
                elif (caractere.isdigit() or caractere == '.') and variableBuilder == "" and not modoString and not dentroComentario:
                    numero += caractere
                    indice = line.find(caractere)
            
                    if caractere == '.' and line[indice].isdigit():
                        numerberType = "float"
                        continue
                    elif not '.' in numero:
                        numerberType = "int"
                        continue

                # Se não é um dígito, mas temos um número acumulado, verifique se é um inteiro
                elif numero and (variableBuilder == "") and (not caractere.isdigit() or caractere == word[-1]) and not modoString and not dentroComentario and (numerberType == "int"):
                    #se o caractere é uma letra
                    if (caractere.isalpha()):
                        caractererInd = line.find(caractere)
                        print(f"Erro na linha {linha} coluna {indice}")
                        print(line)
                        #indicar a linha exata da linha
                        print(" "*(indice) + "^")
                        print("Erro: Lexema inválido")
                        exit() 
                    if re.fullmatch(intRegex, numero):
                        coluna += 1
                        inteirosArray.append(['tkn_inteiro',int(numero),linha,coluna+1])
                        lista.append(['tkn_inteiro',int(numero),linha,coluna+1])
                    numero = "" 
                    
                # Finaliza a construção do número flutuante quando encontra um caractere não numérico ou fim da palavra
                elif numero and (not caractere.isdigit() and (caractere != '.' or caractere == word[-1])):
                    if re.fullmatch(floatRegex, numero):
                        coluna += 1
                        floatsArray.append(['tkn_float',float(numero),linha,coluna+1])
                        lista.append(['tkn_float',float(numero),linha,coluna+1])
                        numero = ""  
                    continue
            

                # verifica se o caractere é um tokensSimbolos
                elif (caractere in tokensSimbolosRegras) and not modoString and not dentroComentario:
                    indice = line.find(caractere)
                    # condicional para não querbrar caso seja o ultimo caractere da linha
                    if (caractere not in word[-1]):
                        if(line[indice+1] == "="):
                            coluna += 1
                            tokensLogicosRelacionaisAtri.append(['tkn_logicos_relacionais_atributos',caractere+line[indice+1],linha,coluna+1])
                            lista.append(['tkn_logicos_relacionais_atributos',caractere+line[indice+1],linha,coluna+1])
                            if(variableBuilder != ""): #resolvendo n4:= linha 30 coluna                            #     variaveis.append(['tkn_variaveis',variableBuilder,linha,coluna+1])
                                lista.append(['tkn_variaveis',variableBuilder,linha,coluna+1])
                                variableBuilder = ""
                            continue
                    coluna = line.find(caractere)
                    tokensSimbolos.append(['tkn_simbolo',caractere,linha,coluna+1])
                    lista.append(['tkn_simbolo',caractere,linha,coluna+1])
                    if variableBuilded(variableRegex, variaveis, variableBuilder, palavrasReservadas,linha,coluna,lista,line):
                        variableBuilder = "" 
                        continue
                    continue

                elif (re.match(variableRegex, caractere) and not modoString and not dentroComentario) or (variableBuilder != ""):
                    variableBuilder += caractere
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
                        lista.append(['tkn_comentario',textoComentario,linha,coluna+1])  # Adiciona o comentário acumulado ao array
                        textoComentario = ""  # Reinicia para o próximo comentário
                    continue

                coluna = 0
            if(variableBuilder != ""):
                if(re.fullmatch(variableRegex,variableBuilder) and not (variableBuilder in palavrasReservadasRegras)):
                    separatorindex = line.find(';')
                    variaveis.append(['tkn_variaveis',variableBuilder,linha,separatorindex+2])
                    lista.append(['tkn_variaveis',variableBuilder,linha,separatorindex+2])
                elif(variableBuilder in palavrasReservadasRegras):
                    palavrasReservadas.append(['tkn_palavras_reservadas',variableBuilder,linha,separatorindex+2])
                    lista.append(['tkn_palavras_reservadas',variableBuilder,linha,separatorindex+2])
                else:
                    print(f"Essa merda => {variableBuilder} não existe 👌. Linha:{linha} Coluna: {coluna}") 
                    exit()
            
            variableBuilder = ""
            

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
    
    '==',
    '<>',
    '>',
    '>=',
    '<',
    '<=',
    ':='   
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
    MOD = 72
    DIV = 73

def obter_valor_simbolo(simbolo):
    try:
        enum_simbolo = Tokens[simbolo.upper()]
        return enum_simbolo.value
    except KeyError:
        return None

diretorio = r'listas\lista1\EXS3.pas'

pascalExercise = open( diretorio, 'r')
pascalExerciseContent = pascalExercise.read()

tokenDict,lista = getTokens(pascalExerciseContent)

resultadoJsom = json.dumps(lista)
criarArquivo = open('resultado.json', 'w')
criarArquivo.write(resultadoJsom)
#passar resultado para JSON
