import sys
import importlib.util

def executar_operacao(operacao, op1, op2, variaveis):

  if operacao == "+":
    return float(op1) + float(op2)
  elif operacao == "-":
    return float(op1) - float(op2)
  elif operacao == "*":
    return float(op1) * float(op2)
  elif operacao == "/":
    if float(op2) == 0:
      raise ZeroDivisionError("Divisão por zero")
    return float(op1) / float(op2)
  elif operacao == "//":
    if float(op2) == 0:
      raise ZeroDivisionError("Divisão por zero")
    return float(op1) // float(op2)
  elif operacao == "%":
    if float(op2) == 0:
      raise ZeroDivisionError("Módulo por zero")
    return float(op1) % float(op2)
  elif operacao == "||":
    return bool(op1) or bool(op2)
  elif operacao == "&&":
    return bool(op1) and bool(op2)
  elif operacao == "==":
    return op1 == op2
  elif operacao == "<>":
    return op1 != op2
  elif operacao == ">":
    return float(op1) > float(op2)
  elif operacao == ">=":
    return float(op1) >= float(op2)
  elif operacao == "<":
    return float(op1) < float(op2)
  elif operacao == "<=":
    return float(op1) <= float(op2)
  else:
    raise ValueError(f"Operação inválida: {operacao}")

def resolver_operando(operando, variaveis):

    if isinstance(operando, str):  # Verifica se o operando é uma string
        if operando in variaveis:
            return variaveis[operando]
        else:
            return operando  # Retorna a string sem modificações
    else:
        return float(operando)  # Tenta converter para float

def encontrar_label(label, labels):

  for i, tupla in enumerate(labels):
    if tupla[1] == label:
      return tupla[0]
  raise ValueError(f"Label não encontrado: {label}")

def interpretar_codigo(codigo, variaveis, labels):

  pc = 0
  while pc < len(codigo):
    instrucao = codigo[pc]
    operacao = instrucao[0]

    if operacao in ("+", "-", "*", "/", "//", "%", "||", "&&", "==", "<>", ">", ">=", "<", "<="):
      _, guardar, op1, op2= instrucao
      op1_valor = resolver_operando(op1, variaveis)
      op2_valor = resolver_operando(op2, variaveis) if op2 is not None else None
      resultado = executar_operacao(operacao, op1_valor, op2_valor, variaveis)
      variaveis[guardar] = resultado

    elif operacao == "=":
      _, guardar, op1, _ = instrucao
      variaveis[guardar] = resolver_operando(op1, variaveis)

    elif operacao == "if":
      _, condicao, label1, label2 = instrucao 
      if variaveis.get(condicao, False):  # Considera variáveis não existentes como False
        pc = encontrar_label(label1, labels)
      else:
        pc = encontrar_label(label2, labels)
      continue  # Pula o incremento do pc, pois ele já foi atualizado

    elif operacao == "jump":
      _, label, _, _ = instrucao
      pc = encontrar_label(label, labels)
      continue

    elif operacao == "call":
      _, funcao, argumento, _ = instrucao
      if funcao == "print":
        if(argumento in variaveis):
          print(variaveis[argumento])
        else:
          print(argumento)
      elif funcao == "scan":
        variaveis[argumento] = input()

    pc += 1  # Incrementa o pc para a próxima instrução

def mainP4(codigo):
    # -----------------DESCOMENTAR CASO QUEIRA TESTAR PELOS ARQUIVOS COD_1.PY...-----------------
    # nome_arquivo = input("Digite o nome do arquivo .py:")
    # nome_arquivo = "cod_2.py"
    # try:
    #     spec = importlib.util.spec_from_file_location("modulo_personalizado", nome_arquivo)
    #     modulo = importlib.util.module_from_spec(spec)
    #     sys.modules["modulo_personalizado"] = modulo
    #     spec.loader.exec_module(modulo)
    #     codigo = modulo.programa()  # Obtém a lista de tuplas da função programa
    # except FileNotFoundError:
    #     print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
    #     return

    variaveis = {}
    labels = [(i, tupla[1]) for i, tupla in enumerate(codigo) if tupla[0] == "label"]

    try:
      interpretar_codigo(codigo, variaveis, labels)
    except (ValueError, ZeroDivisionError) as e:
      print(f"Erro durante a execução: {e}")
        
if __name__ == "__main__":
  mainP4()
