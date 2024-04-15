import sys
from parte1 import *
from classTokens import *


def main():
    diretorio = r'listas\lista1\teste.pas'
    lista = analisadorLexico(diretorio)
    print(lista)

    consome(lista, Tokens.PROGRAM.value)
    consome(lista, Tokens.TKN_VARIAVEIS.value)
    consome(lista, Tokens.TKN_PONTOEVIRGULA.value)
    declarations(lista)
    consome(lista, Tokens.BEGIN.value)
    stmtList(lista)
    consome(lista, Tokens.END.value)
    consome(lista, Tokens.TKN_PONTO.value)
    print('CÓDIGO COMPILADO COM SUCESSO')


def declarations(lista):
    consome(lista, Tokens.VAR.value)
    declaration(lista)
    restoDeclaration(lista)
    

def declaration(lista):
    listaIdent(lista)
    consome(lista, Tokens.TKN_DOISPONTOS.value)
    typeFuncao(lista)
    consome(lista, Tokens.TKN_PONTOEVIRGULA.value)
    

def listaIdent(lista):
    consome(lista, Tokens.TKN_VARIAVEIS.value)
    restoIdentList(lista)
    

def restoIdentList(lista):
    if(lista[0][0] == Tokens.TKN_VIRGULA.value):
        consome(lista, Tokens.TKN_VIRGULA.value)
        consome(lista, Tokens.TKN_VARIAVEIS.value)
        restoIdentList(lista)
    # OU VAZIO
    else:
        return
    

def restoDeclaration(lista):
    if(lista[0][0] == Tokens.TKN_VARIAVEIS.value):
        declaration(lista)
        restoDeclaration(lista)
    # OU VAZIO
    else:
        return

def typeFuncao(lista):
    if(lista[0][0] == Tokens.INTEGER.value):
        (consome(lista, Tokens.INTEGER.value))
    # OU
    elif(lista[0][0] == Tokens.REAL.value):
        (consome(lista, Tokens.REAL.value))
    # OU
    elif(lista[0][0] == Tokens.STRING.value):
        (consome(lista,Tokens.STRING.value))

# ------------------------------------------------
# INSTRUÇÕES DOS PROGRAMAS

def bloco(lista):
    consome(lista, Tokens.BEGIN.value)
    stmtList(lista)
    consome(lista, Tokens.END.value)
    consome(lista, Tokens.TKN_PONTOEVIRGULA.value)
    
def stmtList(lista):
    if(lista[0][0] == Tokens.FOR.value or lista[0][0] == Tokens.READ.value or lista[0][0] == Tokens.WRITE.value or lista[0][0] == Tokens.WHILE.value or lista[0][0] == Tokens.TKN_VARIAVEIS.value or lista[0][0] == Tokens.IF.value or lista[0][0] == Tokens.BEGIN.value or lista[0][0] == Tokens.BREAK.value or lista[0][0] == Tokens.CONTINUE.value or lista[0][0] == Tokens.TKN_PONTOEVIRGULA.value):
        stmt(lista)
        stmtList(lista)
    # OU VAZIO
    else:
        return

def stmt(lista):
    if(lista[0][0] == Tokens.FOR.value):
        forStmt(lista)
    # OU
    elif(lista[0][0] == Tokens.READ.value or lista[0][0] == Tokens.WRITE.value):
        ioStmt(lista)

    # OU
    elif(lista[0][0] == Tokens.WHILE.value):
        whileStmt(lista)

    # OU
    elif(lista[0][0] == Tokens.TKN_VARIAVEIS.value):
        atrib(lista)
        consome(lista, Tokens.TKN_PONTOEVIRGULA.value)

    # OU
    elif(lista[0][0] == Tokens.IF.value):
        ifStmt(lista)

    # OU
    elif(lista[0][0] == Tokens.BEGIN.value):
        bloco(lista)

    # OU
    elif(lista[0][0] == Tokens.BREAK.value):
        consome(lista, Tokens.BREAK.value)
        consome(lista, Tokens.TKN_PONTOEVIRGULA.value)

    # OU
    elif(lista[0][0] == Tokens.CONTINUE.value):
        consome(lista, Tokens.CONTINUE.value)
        consome(lista, Tokens.TKN_PONTOEVIRGULA.value)

    # OU
    elif(lista[0][0] == Tokens.TKN_PONTOEVIRGULA.value):
        consome(lista, Tokens.TKN_PONTOEVIRGULA.value)


# ----------------------------------------------------------------------------
# DESCRIÇÃO AS INSTRUCOES

def forStmt(lista):
    consome(lista, Tokens.FOR.value)
    atrib(lista)
    consome(lista, Tokens.TO.value)
    endFor(lista)
    consome(lista, Tokens.DO.value)
    stmt(lista) 

def endFor(lista):
    if(lista[0][0] == Tokens.TKN_VARIAVEIS.value):
        consome(lista, Tokens.TKN_VARIAVEIS.value)

    # OU
    elif(lista[0][0] == Tokens.TKN_INT.value):
        consome(lista, Tokens.TKN_INT.value)

def ioStmt(lista):
    if(lista[0][0] == Tokens.READ.value):
        consome(lista, Tokens.READ.value)
        consome(lista, Tokens.TKN_ABREPARENTESE.value)
        consome(lista, Tokens.TKN_VARIAVEIS.value)
        consome(lista, Tokens.TKN_FECHAPARENTESE.value)
        consome(lista, Tokens.TKN_PONTOEVIRGULA.value)
    # OU
    elif(lista[0][0] == Tokens.WRITE.value):
        consome(lista, Tokens.WRITE.value)
        consome(lista, Tokens.TKN_ABREPARENTESE.value)
        out(lista)
        consome(lista, Tokens.TKN_FECHAPARENTESE.value)
        consome(lista, Tokens.TKN_PONTOEVIRGULA.value)

def outList(lista):
    out(lista)
    restoOutList(lista)
    
def restoOutList(lista):
    if (lista[0][0] == Tokens.TKN_VIRGULA.value):
        consome(lista, Tokens.TKN_VIRGULA)
        outList(lista)
    #OU VAZIO
    else:
        return
    
def out(lista):
    if(lista[0][0] == Tokens.TKN_STRING.value):
        consome(lista, Tokens.TKN_STRING.value)
    # OU
    elif(lista[0][0] == Tokens.TKN_VARIAVEIS.value):
        consome(lista, Tokens.TKN_VARIAVEIS.value)
    # OU
    elif(lista[0][0] == Tokens.TKN_INT.value):
        consome(lista, Tokens.TKN_INT.value)
    # OU
    elif(lista[0][0] == Tokens.TKN_FLOAT.value):
        consome(lista, Tokens.TKN_FLOAT.value)

def whileStmt(lista):
    consome(lista, Tokens.WHILE.value)
    expr(lista)
    consome(lista, Tokens.DO.value)
    stmt(lista)

def ifStmt(lista):
    consome(lista, Tokens.IF.value)
    expr(lista)
    consome(lista, Tokens.THEN.value)
    stmt(lista)
    elsePart(lista)
    

def elsePart(lista):
    if (lista[0][0] == Tokens.ELSE.value):
        consome(lista, Tokens.ELSE.value)
        stmt(lista)
    # OU
    # VAZIO
    else:
        return
# ------------------------------------------------------------------------
# expressoes

def atrib(lista):
    consome(lista, Tokens.TKN_VARIAVEIS.value)
    consome(lista, Tokens.TKN_ATRIBUICAO.value)
    expr(lista)

def expr(lista):
    orFuncao(lista)

def orFuncao(lista):
    andFuncao(lista)
    restoOr(lista)

def restoOr(lista):
    if (lista[0][0] == Tokens.OR.value):
        consome(lista, Tokens.OR.value)
        andFuncao(lista)
        restoOr(lista)
    # OU
    # VAZIO
    else:
        return

def andFuncao(lista):
    notFuncao(lista)
    restoAnd(lista)

def restoAnd(lista):
    if (lista[0][0] == Tokens.AND.value):
        consome(lista, Tokens.AND.value)
        notFuncao(lista)
        restoAnd(lista)
    # OU
    # VAZIO
    else:
        return


def notFuncao(lista):
    if(lista[0][0] == Tokens.NOT.value):
        consome(lista, Tokens.NOT.value)
        notFuncao(lista)
    # OU
    else:
        rel(lista)

def rel(lista):
    addFuncao(lista)
    restoRel(lista)

def restoRel(lista):
    if (lista[0][0] == Tokens.TKN_IGUALDADE.value):
        consome(lista, Tokens.TKN_IGUALDADE.value)
        addFuncao(lista)
    # OU
    elif(lista[0][0] == Tokens.TKN_MAIORMENOR.value):
        consome(lista, Tokens.TKN_MAIORMENOR.value)
        addFuncao(lista)
    # OU
    elif(lista[0][0] == Tokens.TKN_MENOR.value):
        consome(lista, Tokens.TKN_MENOR.value)
        addFuncao(lista)
    # OU
    elif(lista[0][0] == Tokens.TKN_MENORIGUAL.value):
        consome(lista, Tokens.TKN_MENORIGUAL.value)
        addFuncao(lista)

    # OU
    elif(lista[0][0] == Tokens.TKN_MAIOR.value):
        consome(lista, Tokens.TKN_MAIOR.value)
        addFuncao(lista)
    # OU
    elif(lista[0][0] == Tokens.TKN_MAIORIGUAL.value):
        consome(lista, Tokens.TKN_MAIORIGUAL.value)
        addFuncao(lista)
    # OU
    # VAZIO
    else:
        return


def addFuncao(lista):
    mult(lista)
    restoAdd(lista)

def restoAdd(lista):
    if(lista[0][0] == Tokens.TKN_ADICAO.value):
        consome(lista, Tokens.TKN_ADICAO.value)
        mult(lista)
        restoAdd(lista)
    # OU
    elif(lista[0][0] == Tokens.TKN_SUBTRACAO.value):
        consome(lista, Tokens.TKN_SUBTRACAO.value)
        mult(lista)
        restoAdd(lista)

    # OU
    # VAZIO
    else:
        return


def mult(lista):
    uno(lista)
    restoMult(lista)

def restoMult(lista):
    if(lista[0][0] == Tokens.TKN_MULTIPLICACAO.value):
        consome(lista, Tokens.TKN_MULTIPLICACAO.value)
        uno(lista)
        restoMult(lista)
    # OU
    elif(lista[0][0] == Tokens.TKN_DIVISAO.value):
        consome(lista, Tokens.TKN_DIVISAO.value)
        uno(lista)
        restoMult(lista)
    # OU
    elif(lista[0][0] == Tokens.MOD.value):
        consome(lista, Tokens.MOD.value)
        uno(lista)
        restoMult(lista)
    # OU
    elif(lista[0][0] == Tokens.DIV.value):
        consome(lista, Tokens.DIV.value)
        uno(lista)
        restoMult(lista)
    # OU
    # VAZIO
    else:
        return


def uno(lista):
    if(lista[0][0] == Tokens.TKN_ADICAO.value):
        consome(lista, Tokens.TKN_ADICAO.value)
        uno(lista)
    # OU
    elif(lista[0][0] == Tokens.TKN_SUBTRACAO.value):
        consome(lista, Tokens.TKN_SUBTRACAO.value)
        uno(lista)
    # OU
    else:
        fator(lista)


def fator(lista):
    if (lista[0][0] == Tokens.TKN_INT.value):
        consome(lista, Tokens.TKN_INT.value)
        
    elif (lista[0][0] == Tokens.TKN_FLOAT.value):
        consome(lista, Tokens.TKN_FLOAT.value)

    elif (lista[0][0] == Tokens.TKN_VARIAVEIS.value):
        consome(lista, Tokens.TKN_VARIAVEIS.value)
        
    elif (lista[0][0] == Tokens.TKN_ABREPARENTESE.value):
        consome(lista, Tokens.TKN_ABREPARENTESE.value)
        expr(lista)
        
    elif (lista[0][0] == Tokens.TKN_FECHAPARENTESE.value):
        consome(lista, Tokens.TKN_FECHAPARENTESE.value)
        
    elif (lista[0][0] == Tokens.TKN_STRING.value):
        consome(lista, Tokens.TKN_STRING.value)
        




# CADA CONSOME DA UM POP NA LISTA
def consome(lista,token_consumido):
    if lista[0][0] == token_consumido:
            lista.pop(0)
            return
    else:      
        print('ERRO, ESPERAVA TOKEN ' + encontrar_nome_por_valor(token_consumido) + ' TEMOS TOKEN ' + encontrar_nome_por_valor(lista[0][0]))
        exit()

def encontrar_nome_por_valor(valor):
    for token in Tokens:
        if token.value == valor:
            return token.name
main()