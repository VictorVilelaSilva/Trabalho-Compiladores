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
    declaration()

def declaration(lista):
    listaIdent()

def listaIdent(lista):
    consome(lista,obter_valor_simbolo('tkn_variaveis'))
    restoIdentList()

def restoIdentList(lista):
    consome(lista,obter_valor_simbolo('tkn_virgula'))
    consome(lista,obter_valor_simbolo('tkn_variaveis'))
    restoIdentList()

def type1(lista):
    consome(lista,3)
    consome(lista,4)
    consome(lista,5)

def stmList(lista):
    stmt()
    stmList()

def stmt(lista):
    forStmt()

    ioStmt()

    whileStmt()

    atrib()
    consome('tkn_pontoevirgula')

# CADA CONSOME DA UM POP NA LISTA
def consome(lista,token_consumido):
    lista.pop



main()