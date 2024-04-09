import sys
from parte1 import *

def main():
    diretorio = r'listas\lista1\EXS1.pas'
    lista = analisadorLexico(diretorio)
    print(lista)

    consome(lista,obter_valor_simbolo('program'))
    consome(lista,obter_valor_simbolo('tkn_variaveis'))
    consome(lista,obter_valor_simbolo('tkn_pontoevirgula'))
    declarations(lista)
    consome(lista,obter_valor_simbolo('begin'))
    stmList()
    consome(lista,'end')
    consome(lista,'tkn_ponto')



def declarations(lista):
    consome(lista,'var')
    declaration(lista)
    restoDeclaration(lista)

def declaration(lista):
    listaIdent()
    consome(lista,obter_valor_simbolo('tkn_doispontos'))
    typeFuncao(lista)
    consome(lista,obter_valor_simbolo('tkn_pontoevirgula'))

def listaIdent(lista):
    consome(lista,obter_valor_simbolo('tkn_variaveis'))
    restoIdentList(lista)

def restoIdentList(lista):
    consome(lista,obter_valor_simbolo('tkn_virgula'))
    consome(lista,obter_valor_simbolo('tkn_variaveis'))
    restoIdentList(lista)

    # OU
    # VAZIO

def restoDeclaration(lista):
    declaration(lista)
    restoDeclaration(lista)

    # OU
    # VAZIO

def typeFuncao(lista):
    consome(lista,obter_valor_simbolo('integer'))
    # OU
    consome(lista,obter_valor_simbolo('real'))
    # OU
    consome(lista,obter_valor_simbolo('string'))

# ------------------------------------------------
# INSTRUÇÕES DOS PROGRAMAS

def bloco(lista):
    consome(lista,obter_valor_simbolo('begin'))
    stmList(lista)
    consome(lista,obter_valor_simbolo('end'))

def stmList(lista):
    stmt(lista)
    stmList(lista)

    # OU
    # VAZIO


def stmt(lista):
    forStmt(lista)
    # OU
    ioStmt(lista)
    # OU
    whileStmt(lista)
    # OU
    atrib(lista)
    consome('tkn_pontoevirgula')
    # OU
    ifStmt(lista)
    # OU
    bloco(lista)
    # OU
    consome(lista,obter_valor_simbolo('break'))
    consome(lista,obter_valor_simbolo('tkn_pontoevirgula'))
    # OU
    consome(lista,obter_valor_simbolo('continue'))
    consome(lista,obter_valor_simbolo('tkn_pontoevirgula'))
    # OU
    consome(lista,obter_valor_simbolo('tkn_pontoevirgula'))

# ----------------------------------------------------------------------------
# DESCRIÇÃO AS INSTRUCOES
    
def forStmt(lista):
    consome(lista,obter_valor_simbolo('for'))
    atrib(lista)
    consome(lista,obter_valor_simbolo('to'))
    endFor(lista)
    consome(lista,obter_valor_simbolo('do'))
    stmt(lista)

def endFor(lista):
    consome(lista,obter_valor_simbolo('tkn_variaveis'))
    # OU
    consome(lista,obter_valor_simbolo('tkn_int'))

def ioStmt(lista):
    consome(lista,obter_valor_simbolo('read'))
    consome(lista,obter_valor_simbolo('tkn_abreparentese'))
    consome(lista,obter_valor_simbolo('tkn_variaveis'))
    consome(lista,obter_valor_simbolo('tkn_fechaparentese'))
    consome(lista,obter_valor_simbolo('tkn_ponoevirula'))
    # OU
    consome(lista,obter_valor_simbolo('write'))
    consome(lista,obter_valor_simbolo('tkn_abreparentese'))
    out(lista)
    consome(lista,obter_valor_simbolo('tkn_fechaparentese'))
    consome(lista,obter_valor_simbolo('tkn_ponoevirula'))

def out(lista):
    consome(lista,obter_valor_simbolo('tkn_string'))
    # OU
    consome(lista,obter_valor_simbolo('tkn_variaveis'))
    # OU
    consome(lista,obter_valor_simbolo('tkn_int'))
    # OU
    consome(lista,obter_valor_simbolo('tkn_float'))

def whileStmt(lista):
    consome(lista,obter_valor_simbolo('while'))
    expr(lista)
    stmt(lista)

def ifStmt(lista):
    consome(lista,obter_valor_simbolo('if'))
    expr(lista)
    consome(lista,obter_valor_simbolo('then'))
    stmt(lista)
    elsePart(lista)

def elsePart(lista):
    consome(lista,obter_valor_simbolo('else'))
    stmt(lista)
    # OU
    # VAZIO

# ------------------------------------------------------------------------
# expressoes
    
def atrib(lista):
    consome(lista,obter_valor_simbolo('tkn_variaveis'))
    consome(lista,obter_valor_simbolo('tkn_atribuicao'))
    expr(lista)

def expr(lista):
    orFuncao(lista)

def orFuncao(lista):
    andFuncao(lista)
    restoOr(lista)

def restoOr(lista):
    consome(lista,obter_valor_simbolo('or'))
    andFuncao(lista)
    restoOr(lista)
    # OU
    # VAZIO

    




# CADA CONSOME DA UM POP NA LISTA
def consome(lista,token_consumido):
    lista.pop



main()