""" Um script que leia um nome completo, converta a primeira letra em letra maiuscula
(nome e sobrenome) e armazene dentro de um arquivo. Elabore tratamento de exceção para
verificar se é um nome válido e se o arquivo está no diretório. """

import os

def validar_nome(nome):
    if not nome.strip():
        raise ValueError("O nome não pode estar vazio.")
    if any(char.isdigit() for char in nome):
        raise ValueError("O nome não pode conter números.")

def salvar_nome(nome_formatado, nome_arquivo):
    # Verifica se o arquivo existe antes de tentar escrever
    if not os.path.exists(nome_arquivo):
        raise FileNotFoundError(f"O arquivo '{nome_arquivo}' não existe no diretório.")

    with open(nome_arquivo, 'a', encoding='utf-8') as arquivo:
        arquivo.write(nome_formatado + '\n')

try:
    nome = input("Digite seu nome completo: ").strip()
    validar_nome(nome)
    nome_formatado = nome.title()  # Coloca a primeira letra de cada palavra em maiúscula
    print("Nome formatado:", nome_formatado)

    nome_arquivo = "nomes.txt"
    salvar_nome(nome_formatado, nome_arquivo)
    print(f"Nome salvo com sucesso no arquivo '{nome_arquivo}'.")

except ValueError as ve:
    print("Erro de validação:", ve)

except FileNotFoundError as fe:
    print("Erro de arquivo:", fe)

except Exception as e:
    print("Ocorreu um erro inesperado:", e)
