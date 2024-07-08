def executar_operacao(operacao, op1, op2, variaveis):
  """Executa uma operação aritmética, lógica ou relacional."""

  if operacao == "+":
    return op1 + op2
  elif operacao == "-":
    return op1 - op2
  elif operacao == "*":
    return op1 * op2
  elif operacao == "/":
    if op2 == 0:
      raise ZeroDivisionError("Divisão por zero")
    return op1 / op2
  elif operacao == "//":
    if op2 == 0:
      raise ZeroDivisionError("Divisão por zero")
    return op1 // op2
  elif operacao == "%":
    if op2 == 0:
      raise ZeroDivisionError("Módulo por zero")
    return op1 % op2
  elif operacao == "||":
    return op1 or op2
  elif operacao == "&&":
    return op1 and op2
  elif operacao == "==":
    return op1 == op2
  elif operacao == "<>":
    return op1 != op2
  elif operacao == ">":
    return op1 > op2
  elif operacao == ">=":
    return op1 >= op2
  elif operacao == "<":
    return op1 < op2
  elif operacao == "<=":
    return op1 <= op2
  else:
    raise ValueError(f"Operação inválida: {operacao}")

def resolver_operando(operando, variaveis):
  """Resolve um operando, que pode ser uma variável ou um valor numérico."""

  if isinstance(operando, str) and operando in variaveis:
    return variaveis[operando]
  elif operando is None:
    return None
  else:
    return float(operando)

def encontrar_label(label, labels):
  """Encontra o índice de um label na lista de labels."""

  for i, tupla in enumerate(labels):
    if tupla[1] == label:
      return i
  raise ValueError(f"Label não encontrado: {label}")


def interpretar_codigo(codigo, variaveis, labels):
  """Interpreta o código intermediário."""

  pc = 0
  while pc < len(codigo):
    instrucao = codigo[pc]
    operacao = instrucao[0]

    if operacao in ("+", "-", "*", "/", "//", "%", "||", "&&", "==", "<>", ">", ">=", "<", "<="):
      guardar, op1, op2, _ = instrucao
      op1_valor = resolver_operando(op1, variaveis)
      op2_valor = resolver_operando(op2, variaveis) if op2 is not None else None
      resultado = executar_operacao(operacao, op1_valor, op2_valor, variaveis)
      variaveis[guardar] = resultado

    elif operacao == "=":
      guardar, op1, _, _ = instrucao
      variaveis[guardar] = resolver_operando(op1, variaveis)

    elif operacao == "IF":
      _, condicao, label1, label2 = instrucao
      if variaveis.get(condicao, False):  # Considera variáveis não existentes como False
        pc = encontrar_label(label1, labels)
      else:
        pc = encontrar_label(label2, labels)
      continue  # Pula o incremento do pc, pois ele já foi atualizado

    elif operacao == "JUMP":
      _, label, _, _ = instrucao
      pc = encontrar_label(label, labels)
      continue

    elif operacao == "CALL":
      _, funcao, argumento, _ = instrucao
      if funcao == "PRINT":
        print(resolver_operando(argumento, variaveis))
      elif funcao == "SCAN":
        variaveis[argumento] = float(input())

    pc += 1  # Incrementa o pc para a próxima instrução

def main():
  """Função principal do interpretador."""

  nome_arquivo = input("Digite o nome do arquivo de entrada: ")

  try:
    with open(nome_arquivo, "r") as arquivo:
      codigo = eval(arquivo.read())  # Avalia o conteúdo do arquivo para obter a lista de tuplas
  except FileNotFoundError:
    print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
    return
  except SyntaxError:
    print("Erro na sintaxe do código intermediário.")
    return

  variaveis = {}
  labels = [(i, tupla[1]) for i, tupla in enumerate(codigo) if tupla[0] == "LABEL"]

  try:
    interpretar_codigo(codigo, variaveis, labels)
  except (ValueError, ZeroDivisionError) as e:
    print(f"Erro durante a execução: {e}")

if __name__ == "__main__":
  main()
