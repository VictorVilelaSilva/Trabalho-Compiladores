import json
import re
from typing import List

def extrair_comentarios_pascal(caminho_do_arquivo):
    # comentarios = []
    
    # # Abrir o arquivo para leitura
    with open(caminho_do_arquivo, 'r') as arquivo:
        pascalExerciseContent = arquivo.read()
        
    #     # Procurar por comentários no conteúdo do arquivo
    #     comentarios = re.findall(r'\{.*?\}', conteudo, re.DOTALL)
    for line in pascalExerciseContent.split(' '):
        content = ""
        open_bracket = False
        if "{" in line:
            open_bracket = True
            content += line[line.index("{")+1:]
        elif "}" in line and open_bracket:
            content += line[:line.index("}")]
            break
        elif open_bracket:
            content += line

        print(content)
        exit()
    return comentarios

# Substitua 'caminho_para_seu_arquivo.pas' pelo caminho real do seu arquivo Pascal

caminho_do_arquivo = 'listas\lista3\EXS17.pas'
comentarios = extrair_comentarios_pascal(caminho_do_arquivo)
print(comentarios)
