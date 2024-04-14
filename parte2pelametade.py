import sys
from parte1 import *

def main():
    diretorio = r'listas\lista1\teste.pas'
    lista = analisadorLexico(diretorio)
    print(lista)

    if (consome(lista,obter_valor_simbolo('program'))
        and consome(lista,obter_valor_simbolo('tkn_variaveis'))
        and consome(lista,obter_valor_simbolo('tkn_pontoevirgula'))
        and declarations(lista)
        and consome(lista,obter_valor_simbolo('begin'))
        and stmtList(lista)
        and consome(lista,obter_valor_simbolo('end'))
        and consome(lista,obter_valor_simbolo('tkn_ponto'))):
        return print('CÓDIGO COMPILADO COM SUCESSO')
    else:
        print(lista[0])
        print('ERRO')



def declarations(lista):
    if(consome(lista,obter_valor_simbolo('var'))
        and declaration(lista)
        and restoDeclaration(lista)):
        return True
    else:
        return False
            

def declaration(lista):
    if(listaIdent(lista)
    and consome(lista,obter_valor_simbolo('tkn_doispontos'))
    and typeFuncao(lista)
    and consome(lista,obter_valor_simbolo('tkn_pontoevirgula'))):
        return True
    else:
        return False
        

def listaIdent(lista):
    if(consome(lista,obter_valor_simbolo('tkn_variaveis'))
        and restoIdentList(lista)):
        return True

def restoIdentList(lista):
    if(consome(lista,obter_valor_simbolo('tkn_virgula'))
        and consome(lista,obter_valor_simbolo('tkn_variaveis'))
        and restoIdentList(lista)):
        return True 
    # OU VAZIO
    else:
        return True

def restoDeclaration(lista):
    if (declaration(lista)
        and restoDeclaration(lista)):
        return True
    # OU VAZIO
    else:
        return True

def typeFuncao(lista):
    if(consome(lista,obter_valor_simbolo('integer'))):
        return True
    # OU
    elif(consome(lista,obter_valor_simbolo('real'))):
        return True
    # OU
    elif(consome(lista,obter_valor_simbolo('string'))):
        return True
    else:
        return False

# ------------------------------------------------
# INSTRUÇÕES DOS PROGRAMAS

def bloco(lista):
    if(consome(lista,obter_valor_simbolo('begin'))
        and stmtList(lista)
        and consome(lista,obter_valor_simbolo('end'))):
        return True

def stmtList(lista):
    if(stmt(lista)
        and stmtList(lista)):
        return True
    # OU VAZIO
    else:
        return True


def stmt(lista):
    if(forStmt(lista)):
        return True
    # OU
    elif(ioStmt(lista)):
        return True
    # OU
    elif(whileStmt(lista)):
        return True
    # OU
    elif(atrib(lista)
        and consome(lista,obter_valor_simbolo('tkn_pontoevirgula'))):
        return True
    # OU
    elif(ifStmt(lista)):
        return True
    # OU
    elif(bloco(lista)):
        return True
    # OU
    elif(consome(lista,obter_valor_simbolo('break'))
        and consome(lista,obter_valor_simbolo('tkn_pontoevirgula'))):
        return True
    # OU
    elif(consome(lista,obter_valor_simbolo('continue'))
        and consome(lista,obter_valor_simbolo('tkn_pontoevirgula'))):
        return True
    # OU
    elif(consome(lista,obter_valor_simbolo('tkn_pontoevirgula'))):
        return True

# ----------------------------------------------------------------------------
# DESCRIÇÃO AS INSTRUCOES
    
def forStmt(lista):
    if(consome(lista,obter_valor_simbolo('for'))
        and atrib(lista)
        and consome(lista,obter_valor_simbolo('to'))
        and endFor(lista)
        and consome(lista,obter_valor_simbolo('do'))
        and stmt(lista)):
        return True

def endFor(lista):
    if(consome(lista,obter_valor_simbolo('tkn_variaveis'))):
        return True
    # OU
    elif(consome(lista,obter_valor_simbolo('tkn_int'))):
        return True

def ioStmt(lista):
    if(consome(lista,obter_valor_simbolo('read'))
        and consome(lista,obter_valor_simbolo('tkn_abreparentese'))
        and consome(lista,obter_valor_simbolo('tkn_variaveis'))
        and consome(lista,obter_valor_simbolo('tkn_fechaparentese'))
        and consome(lista,obter_valor_simbolo('tkn_ponoevirula'))):
        return True
    # OU
    elif(consome(lista,obter_valor_simbolo('write'))
        and consome(lista,obter_valor_simbolo('tkn_abreparentese'))
        and out(lista)
        and consome(lista,obter_valor_simbolo('tkn_fechaparentese'))
        and consome(lista,obter_valor_simbolo('tkn_ponoevirula'))):
        return True

def out(lista):
    if(consome(lista,obter_valor_simbolo('tkn_string'))):
        return True
    # OU
    elif(consome(lista,obter_valor_simbolo('tkn_variaveis'))):
        return True
    # OU
    elif(consome(lista,obter_valor_simbolo('tkn_int'))):
        return True
    # OU
    elif(consome(lista,obter_valor_simbolo('tkn_float'))):
        return True

def whileStmt(lista):
    if(consome(lista,obter_valor_simbolo('while'))
        and expr(lista)
        and stmt(lista)):
        return True

def ifStmt(lista):
    if(consome(lista,obter_valor_simbolo('if'))
    and expr(lista)
    and consome(lista,obter_valor_simbolo('then'))
    and stmt(lista)
    and elsePart(lista)):
        return True

def elsePart(lista):
    if(consome(lista,obter_valor_simbolo('else'))
        and stmt(lista)):
        return True
    # OU
    # VAZIO
    else:
        return True

# ------------------------------------------------------------------------
# expressoes
    
def atrib(lista):
    if (consome(lista,obter_valor_simbolo('tkn_variaveis'))
        and consome(lista,obter_valor_simbolo('tkn_atribuicao'))
        and expr(lista)):
        return True

def expr(lista):
    if(orFuncao(lista)):
        return True

def orFuncao(lista):
    if (andFuncao(lista)
        and restoOr(lista)):
        return True

def restoOr(lista):
    if(consome(lista,obter_valor_simbolo('or'))
        and andFuncao(lista)
        and restoOr(lista)):
        return True
    # OU
    # VAZIO
    else:
        return True

def andFuncao(lista):
    if(notFuncao(lista)
        and restoAnd(lista)):
        return True
    
def restoAnd(lista):
    if(consome(lista,obter_valor_simbolo('and'))
        and notFuncao(lista)
        and restoAnd(lista)):
        return True
    # OU
    # VAZIO
    else:
        return True
    
def notFuncao(lista):
    if(consome(lista,obter_valor_simbolo('not'))
        and notFuncao(lista)):
        return True
    # OU
    elif(rel(lista)):
        return True
    
def rel(lista):
    if(addFuncao(lista)
        and restoRel(lista)):
        return True
    
def restoRel(lista):
    if(consome(lista,obter_valor_simbolo('tkn_igualdade'))
        and addFuncao(lista)):
        return True
    # OU
    elif(consome(lista,obter_valor_simbolo('tkn_maiormenor'))
        and addFuncao(lista)):
        return True
    # OU
    elif(consome(lista,obter_valor_simbolo('tkn_menor'))
        and addFuncao(lista)):
        return True
    # OU
    elif(consome(lista,obter_valor_simbolo('tkn_menorigual'))
        and addFuncao(lista)):
        return True
    # OU
    elif(consome(lista,obter_valor_simbolo('tkn_maior'))
        and addFuncao(lista)):
        return True
    # OU
    elif(consome(lista,obter_valor_simbolo('tkn_maiorigual'))
        and addFuncao(lista)):
        return True
    # OU
    # VAZIO
    else:
        return True
    
def addFuncao(lista):
    if(mult(lista)
        and restoAdd(lista)):
        return True
    
def restoAdd(lista):
    if(consome(lista,obter_valor_simbolo('tkn_adicao'))
        and mult(lista)
        and restoAdd(lista)):
        return True
    # OU
    elif(consome(lista,obter_valor_simbolo('tkn_subtracao'))
        and mult(lista)
        and restoAdd(lista)):
        return True
    # OU
    # VAZIO
    else:
        return True
    
def mult(lista):
    if(uno(lista)
        and restoMult(lista)):
        return True
    
def restoMult(lista):
    if(consome(lista,obter_valor_simbolo('tkn_multiplicacao'))
        and uno(lista)
        and restoMult(lista)):
        return True
    # OU
    elif(consome(lista,obter_valor_simbolo('tkn_divisao'))
        and uno(lista)
        and restoMult(lista)):
        return True
    # OU
    elif(consome(lista,obter_valor_simbolo('mod'))
        and uno(lista)
        and restoMult(lista)):
        return True
    # OU
    elif(consome(lista,obter_valor_simbolo('div'))
        and uno(lista)
        and restoMult(lista)):
        return True
    # OU
    # VAZIO
    else:
        return True
    
def uno(lista):
    if(consome(lista,obter_valor_simbolo('tkn_adicao'))
        and uno(lista)):
        return True
    # OU
    elif(consome(lista,obter_valor_simbolo('tkn_subtracao'))
        and uno(lista)):
        return True
    # OU
    elif(fator(lista)):
        return True

def fator(lista):
    if consome(lista,obter_valor_simbolo('tkn_int')):
        return True
    elif consome(lista,obter_valor_simbolo('tkn_float')):
        return
    elif consome(lista,obter_valor_simbolo('tkn_variaveis')):
        return True
    elif consome(lista,obter_valor_simbolo('tkn_abreparentese')):
        expr(lista)
        return True
    elif consome(lista,obter_valor_simbolo('tkn_fechaparentese')):
        return True
    elif consome(lista,obter_valor_simbolo('tkn_string')):
        return True
    else:
        print('ERRO')


# CADA CONSOME DA UM POP NA LISTA
def consome(lista,token_consumido):
    if lista[0][0] == token_consumido:
            lista.pop(0)
            return True
    else:
        return False



main()