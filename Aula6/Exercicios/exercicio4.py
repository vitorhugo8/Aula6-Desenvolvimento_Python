""" Tendo um arquivo de texto, conte quantas palavras tem esse arquivo. Além de contar
quantas linhas, esse script também deve verificar se o arquivo está no diretório. """

import os

# Nome do arquivo
nome_arquivo = "arquivo.txt"

# Verifica se o arquivo existe no diretório
if os.path.exists(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            num_linhas = len(linhas)
            num_palavras = sum(len(linha.split()) for linha in linhas)

        print(f"O arquivo '{nome_arquivo}' foi encontrado.")
        print(f"Total de linhas: {num_linhas}")
        print(f"Total de palavras: {num_palavras}")

    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
else:
    print(f"Arquivo '{nome_arquivo}' não encontrado no diretório atual.")
