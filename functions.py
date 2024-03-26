from classTokens import Tokens
import re
from typing import List

def variableBuilded(variableRegex: str, variaveis: list, buildedVariable: str,palavrasReservadas: list,linha: int,coluna: int,lista: list,line: str)->bool:
    if buildedVariable != "" and re.fullmatch(variableRegex, buildedVariable) and (buildedVariable not in palavrasReservadas) :
        coluna = line.find(buildedVariable)
        variaveis.append(['tkn_variaveis',buildedVariable,linha,coluna])
        lista.append(['tkn_variaveis',buildedVariable,linha,coluna])
        return True
    elif buildedVariable != "" and buildedVariable in palavrasReservadas:
        coluna = line.find(buildedVariable)
        palavrasReservadas.append(['tkn_palavras_reservadas',buildedVariable,linha,coluna])
        lista.append(['tkn_palavras_reservadas',buildedVariable,linha,coluna])
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


def errorCatch(linha: int, line: str, word: str) ->None:
    indice = line.find(word)
    print(f"Erro na linha {linha} coluna {indice}")
    print(line)
    #indicar a linha exata da linha
    print(" "*(indice) + "^")
    print("Erro: Lexema inválido")
    exit()

def errorCatchString(linha: int, coluna: int,line: str) ->None:
    print(f"Erro na linha {linha} coluna {coluna}")
    print(line)
    #indicar a linha exata da linha
    print(" "*(coluna-1) + "^")
    print("Erro: String não fechada")
    exit()


def handleTokensAritimeticos(word: str)->str:
    if(word == "+"):
        simbolo = "tkn_adicao"
    elif(word == "-"):
        simbolo = "tkn_subtracao"
    elif(word == "*"):
        simbolo = "tkn_multiplicacao"
    elif(word == "/"):
        simbolo = "tkn_divisao"
    return simbolo

def handleTokensSimbolos(word: str)->str:
    if(word == ";"):
        simbolo = "tkn_pontoevirgula"

    elif(word == ","):
            simbolo = "tkn_virgula"

    elif(word == "."):
            simbolo = "tkn_ponto"

    elif(word == ":"):
            simbolo = "tkn_doispontos"

    elif(word == "("):
            simbolo = "tkn_abreparentese"

    elif(word == ")"):
            simbolo = "tkn_fechaparentese"
    return simbolo

def handleTokensLogicos(word: str) ->str:
    if(word == "<>"):
        simbolo = 'tkn_maiormenor'
    elif(word == ">"):
        simbolo = 'tkn_maior'
    elif(word == ">="):
        simbolo = 'tkn_maiorigual'
    elif(word == "<"):
        simbolo = 'tkn_menor'
    elif(word == "<="):
        simbolo = 'tkn_menorigual'
    elif(word == ":="):
        simbolo = 'tkn_atribuicao'
    elif(word == "="):
        simbolo = 'tkn_igualdade'
    return simbolo

def obter_valor_simbolo(simbolo:any):
    try:
        enum_simbolo = Tokens[simbolo.upper()]
        return enum_simbolo.value
    except KeyError:
        return None
