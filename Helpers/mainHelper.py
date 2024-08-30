from .mainToken import Tokens


class FunctionsClass:
    def __init__(self):
        self.numLabel = 0
        self.numTemp = 0

    def is_integer(self, s):
        return s.isdigit()

    def is_float(self, s):
        try:
            float_value = float(s)
            return True
        except ValueError:
            return False

    def errorCatch(self, linha: int, line: str, word: str) -> None:
        indice = line.find(word)
        print(f"Erro na linha {linha} coluna {indice}")
        print(line)
        # indicar a linha exata da linha
        print(" " * (indice) + "^")
        print("Erro: Lexema inválido")
        exit()

    def errorCatchString(self, linha: int, coluna: int, line: str) -> None:
        print(f"Erro na linha {linha} coluna {coluna}")
        print(line)
        # indicar a linha exata da linha
        print(" " * (coluna - 1) + "^")
        print("Erro: String não fechada")
        exit()

    def errorCatchStringComentario(self, linha: int, coluna: int, line: str) -> None:
        print(f"Erro na linha {linha} coluna {coluna}")
        print(line)
        # indicar a linha exata da linha
        print(" " * (coluna - 1) + "^")
        print("Erro: String não fechada")
        exit()

    def errorCatchComentario(self, linha: int, coluna: int, line: str) -> None:
        print(f"Erro na linha {linha} coluna {coluna}")
        print(line)
        # indicar a linha exata da linha
        print(" " * (coluna - 1) + "^")
        print("Erro: Comentario não fechado não fechada")
        exit()

    def handleTokensAritimeticos(self, word: str) -> str:
        if word == "+":
            simbolo = "tkn_adicao"
        elif word == "-":
            simbolo = "tkn_subtracao"
        elif word == "*":
            simbolo = "tkn_multiplicacao"
        elif word == "/":
            simbolo = "tkn_divisao"
        return simbolo

    def handleTokensSimbolos(self, word: str) -> str:
        if word == ";":
            simbolo = "tkn_pontoevirgula"
        elif word == ",":
            simbolo = "tkn_virgula"
        elif word == ".":
            simbolo = "tkn_ponto"
        elif word == ":":
            simbolo = "tkn_doispontos"
        elif word == "(":
            simbolo = "tkn_abreparentese"
        elif word == ")":
            simbolo = "tkn_fechaparentese"
        return simbolo

    def handleTokensLogicos(self, word: str) -> str:
        if word == "<>":
            simbolo = "tkn_maiormenor"
        elif word == ">":
            simbolo = "tkn_maior"
        elif word == ">=":
            simbolo = "tkn_maiorigual"
        elif word == "<":
            simbolo = "tkn_menor"
        elif word == "<=":
            simbolo = "tkn_menorigual"
        elif word == ":=":
            simbolo = "tkn_atribuicao"
        elif word == "=":
            simbolo = "tkn_igualdade"
        return simbolo

    def obter_valor_simbolo(self, simbolo: any):
        try:
            enum_simbolo = Tokens[simbolo.upper()]
            return enum_simbolo.value
        except KeyError:
            return None

    def gera_label(self):
        label = "label" + str(self.numLabel)
        self.numLabel += 1
        return label

    def gera_temp(self):
        temp = "temp" + str(self.numTemp)
        self.numTemp += 1
        return temp
