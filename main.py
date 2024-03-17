import json
import re
from typing import List

#####################################Analisador Léxico (Pascal)################################
# percorre o arquivo e retorna os tokens

def variableBuilded(variableRegex, variaveis, buildedVariable,palavrasReservadas):
    if buildedVariable != "" and re.fullmatch(variableRegex, buildedVariable) and (buildedVariable not in palavrasReservadasRegras) :
        if buildedVariable not in variaveis:
            variaveis.append(buildedVariable)
        return True
    elif buildedVariable != "" and buildedVariable in palavrasReservadasRegras:
        palavrasReservadas.append(buildedVariable)
        return True
    return False


def getTokens(pascalExerciseContent: str) -> List[dict]:

    intRegex = r'^[0-9]+$'
    floatRegex = r'[0-9]+\.[0-9]+'
    variableRegex = r'[a-zA-Z][a-zA-Z0-9_]*'
    # variableRegex = r'^[a-zA-Z][a-zA-Z0-9]*$'


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
            comentariosArray.append(tempLine)
            linha += 1
            continue

        # percorre a linha por palavra
        for word in line.split(' '):
     
            if not line.startswith(word) and not word.isspace(): 
                coluna += 1
            
            #faz com que ocorra uma espaco entre as palavras da string
            if(modoString):
                string += " "
                coluna += 1

            
            # verifica se a palavra é uma palavra reservada
            if (word in palavrasReservadasRegras) and not modoString and not dentroComentario: 
                palavrasReservadas.append(word)
                coluna =+ (len(word))
                continue
            
            # verifica se a palavra não é uma palavra reservada e é uma variável
            elif (word not in palavrasReservadasRegras) and (word not in tokensLogicosRelacionaisAtriRegras)and (re.fullmatch(variableRegex, word) and not modoString and not dentroComentario):
                if(word[-1] == ';'):
                    variaveis.append(word[:-1])
                    tokensSimbolos.append(';')
                    continue
                variaveis.append(word)
                coluna =+ (len(word))
                continue

            # verifica se a palavra é um tokensLogicosRelacionaisAtri
            elif (word in tokensLogicosRelacionaisAtriRegras) and not modoString and not dentroComentario:
                tokensLogicosRelacionaisAtri.append(word)
                coluna =+ (len(word))
                continue
            
            # percorre a palavra por caractere
            for caractere in word:
                coluna += 1

                # verifica se esta no modo string
                if modoString:
                    string+=caractere
                    if caractere == "'":
                        modoString = False
                        stringsArray.append(string[:-1])
                        string = ""
                    continue  
               
                # verifica se o caractere é um espaço
                if (caractere == '\s'):
                   if variableBuilded(variableRegex, variaveis, variableBuilder, palavrasReservadas):
                        variableBuilder = "" 
                        continue
                
                # verifica se o caractere é um tokensAritimeticos
                if (caractere in tokensAritimeticosRegras) and not modoString and not dentroComentario:
                    tokensAritimeticos.append(caractere)
                    if variableBuilded(variableRegex, variaveis, variableBuilder, palavrasReservadas):
                        variableBuilder = "" 
                        continue
                    continue

                # verifica se o caractere é um tokensLogicosRelacionaisAtri
                elif (caractere in tokensLogicosRelacionaisAtriRegras) and not modoString and not dentroComentario:
                    #achar a possição do caractere na linha
                    posicao = line.find(caractere)
                    newCaractere = caractere+line[posicao+1]
                    if  (newCaractere  in tokensLogicosRelacionaisAtriRegras):
                        tokensLogicosRelacionaisAtri.append(newCaractere)
                        variableBuilder = ""  # Reinicia para o próximo número
                        continue

    
                    tokensLogicosRelacionaisAtri.append(caractere)
                    if variableBuilded(variableRegex, variaveis, variableBuilder, palavrasReservadas):
                        variableBuilder = "" 
                        continue
                    continue

                # Se não é um dígito, mas temos um número acumulado, verifique se é um flutuante
                elif (caractere.isdigit() or caractere == '.') and variableBuilder == "" and not modoString and not dentroComentario:
                    numero += caractere
                    indice = line.find(caractere)
            
                    if caractere == '.' and line[indice+1].isdigit():
                        numerberType = "float"
                        continue
                    elif not '.' in numero:
                        numerberType = "int"
                        continue

                # Se não é um dígito, mas temos um número acumulado, verifique se é um inteiro
                elif numero and (variableBuilder == "") and (not caractere.isdigit() or caractere == word[-1]) and not modoString and not dentroComentario and (numerberType == "int"):
                    if re.fullmatch(intRegex, numero):
                        inteirosArray.append(int(numero))
                    numero = "" 
                    
                # Finaliza a construção do número flutuante quando encontra um caractere não numérico ou fim da palavra
                elif numero and (not caractere.isdigit() and (caractere != '.' or caractere == word[-1])):
                    if re.fullmatch(floatRegex, numero):
                        floatsArray.append(float(numero))
                        numero = ""  
                    continue
            

                # verifica se o caractere é um tokensSimbolos
                elif (caractere in tokensSimbolosRegras) and not modoString and not dentroComentario:
                    indice = line.find(caractere)
                    # condicional para não querbrar caso seja o ultimo caractere da linha
                    if (caractere not in word[-1]):
                        if(line[indice+1] == "="):
                            tokensLogicosRelacionaisAtri.append(caractere+line[indice+1])
                            continue
                    tokensSimbolos.append(caractere)
                    if variableBuilded(variableRegex, variaveis, variableBuilder, palavrasReservadas):
                        variableBuilder = "" 
                        continue
                    continue

                elif (re.match(variableRegex, caractere) and not modoString and not dentroComentario) or (variableBuilder != ""):
                    variableBuilder += caractere
                    continue


                # verifica se o caractere é um string
                elif caractere == "'" and not dentroComentario:
                    modoString = True
                    continue
                
                # ativa o modo de comentario
                elif (caractere == '{') and not modoString and not dentroComentario:
                    dentroComentario = True
                    textoComentario = caractere  # Inicia o texto do comentário com '{'
                    coluna += 1
                    continue
            
                # Se estiver dentro de um comentário, acumula o texto
                elif dentroComentario:
                    textoComentario += caractere  # Acumula texto do comentário
                    coluna += 1
                    if caractere == '}':
                        dentroComentario = False
                        comentariosArray.append(textoComentario)  # Adiciona o comentário acumulado ao array
                        textoComentario = ""  # Reinicia para o próximo comentário
                    continue

                coluna = 0

            variableBuilder = ""

    tokens = {
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
    return tokens


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
    ':',
    '(',
    ')',
]

# tokens = {
#     'tokensAritimeticosRegras': tokensAritimeticosRegras,
#     'tokensLogicosRelacionaisAtriRegras': tokensLogicosRelacionaisAtriRegras,
#     'palavrasReservadasRegr': palavrasReservadasRegr,
#     'tokensSimbolos': tokensSimbolos
# }

diretorio = 'listas\lista1\EXS22.pas'

pascalExercise = open( diretorio, 'r')
pascalExerciseContent = pascalExercise.read()

resultado = getTokens(pascalExerciseContent)

resultadoJsom = json.dumps(resultado)
criarArquivo = open('resultado.json', 'w')
criarArquivo.write(resultadoJsom)
#passar resultado para JSON
