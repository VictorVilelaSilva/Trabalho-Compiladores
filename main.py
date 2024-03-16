import json
import re
from typing import List
###############Analisador Léxico (Pascal)#######################

# lembretes:
# 1. Observa ̧c ̃ao: Como a express ̃ao regular dos n ́umeros flutuantes pode n ̃ao
# ter nada na segunda parte e isso pode tornar mais complexa as pr ́oximas
# etapas. Transformaremos a express ̃ao em [0..9]+.[0..9]∗0 visto que adi-
# cionar um ’0’ a direita depois da virgula n ̃ao vai modificar nosso n ́umero
# original. Esse zero ser ́a adicionado somente a n ́ıvel de lexema, o fonte
# original n ̃ao tem a obriga ̧c ̃ao de colocar esse zero no fim de um n ́umero
# flutuante.
# 2. regex float possivel -> floatRegex = r'[0-9]+.[0-9]*'
# 3. verificar regex re.match(variableRegex, "1"):

# def isString(value: str) -> bool:
#     return value[0] == '"' and value[-1] == '"' and len(value) > 1


# percorre o arquivo e retorna os tokens
def getTokens(pascalExerciseContent: str) -> List[dict]:

    intRegex = r'^[0-9]+$'
    floatRegex = r'[0-9]+\.[0-9]+'
    variableRegex = r'[a-zA-Z][a-zA-Z0-9]*'
    # variableRegex = r'^[a-zA-Z][a-zA-Z0-9]*$'


    tokensAritimeticos = []
    tokensLogicosRelacionaisAtri = []
    palavrasReservadas = []
    tokensSimbolos = []
    variaveis = []
    stringsArray = []
    string = ""
    
    
    linha = 0
    coluna = 0
    modoString = False

    for line in pascalExerciseContent.split('\n'):
        linha += 1

        # verifica se a linha é um comentário
        tempLine = line.lstrip()
        if(tempLine.startswith('//')):
            stringsArray.append(line)
            linha += 1
            continue
    
        # percorre a linha por palavra
        for word in line.split(' '):

            #faz com que ocorra uma espaco entre as palavras da string
            if(modoString):
                string += " "
                coluna += 1

            
            # verifica se a palavra é uma palavra reservada
            if (word in palavrasReservadasRegras) and (modoString == False): 
                palavrasReservadas.append(word)
                coluna =+ (len(word)-1)
                continue
            
            # verifica se a palavra não é uma palavra reservada e é uma variável
            elif (word not in palavrasReservadasRegras) and (re.match(variableRegex, word) and (modoString == False)):
                variaveis.append(word)
                coluna =+ (len(word)-1)
                continue
            
            # percorre a palavra por caractere
            for caractere in word:
                coluna += 1

                # verifica se esta no modo string
                if modoString:
                    print(caractere)
                    string+=caractere
                    if caractere == "'":
                        modoString = False
                        stringsArray.append(string[:-1])
                        string = ""
                    continue  
               
                # verifica se o caractere é um espaço
                if (caractere == '\s'):   
                    continue
                
                # verifica se o caractere é um tokensAritimeticos
                if (caractere in tokensAritimeticosRegras) and (modoString == False):
                    tokensAritimeticos.append(caractere)

                # verifica se o caractere é um tokensLogicosRelacionaisAtri
                elif (caractere in tokensLogicosRelacionaisAtriRegras) and (modoString == False):
                    tokensLogicosRelacionaisAtri.append(caractere)

                # verifica se o caractere é um tokensSimbolos
                elif (caractere in palavrasReservadasRegras) and (modoString == False): #opa opa opa
                    palavrasReservadas.append(caractere)

                # verifica se o caractere é um tokensSimbolos
                elif (caractere in tokensSimbolosRegras) and (modoString == False):
                    tokensSimbolos.append(caractere)

                # verifica se o caractere é um string
                elif caractere == "'":
                    modoString = True
                    continue

                coluna = 0
        

    tokens = {
        'tokensAritimeticos': tokensAritimeticos,
        'tokensLogicosRelacionaisAtri' : tokensLogicosRelacionaisAtri,
        'palavrasReservadas' : palavrasReservadas,
        'tokensSimbolos' : tokensSimbolos,
        'variaveis' : variaveis,
        'strings' : stringsArray
    }
    return tokens

# intRegex = r'[0-9]+'


tokensAritimeticosRegras: List[str] = [
    '+',
    '-',
    '*',
    '/',
    'mod',
    'div'
]

tokensLogicosRelacionaisAtriRegras: List[str]  = [
    'or',
    'and',
    'not',
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
    'read'
]

tokensSimbolosRegras: List[str] = [
    ';',
    ',',
    '.',
    ':'
    '(',
    ')',
]

# tokens = {
#     'tokensAritimeticosRegras': tokensAritimeticosRegras,
#     'tokensLogicosRelacionaisAtriRegras': tokensLogicosRelacionaisAtriRegras,
#     'palavrasReservadasRegr': palavrasReservadasRegr,
#     'tokensSimbolos': tokensSimbolos
# }

diretorio = 'listas\lista1\EXS1.pas'

pascalExercise = open( diretorio, 'r')
pascalExerciseContent = pascalExercise.read()

resultado = getTokens(pascalExerciseContent)

resultadoJsom = json.dumps(resultado)
criarArquivo = open('resultado.json', 'w')
criarArquivo.write(resultadoJsom)
#passar resultado para JSON
