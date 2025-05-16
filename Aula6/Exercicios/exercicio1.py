""" Faça um script que leia um nome e verifique se o nome é string válido,
usando o try/execpt """
def validar_nome(nome):
    if not nome:
        raise ValueError("Nome vazio")
    if any(char.isdigit() for char in nome):
        raise ValueError("Nome contém números")

try:
    nome = input("Insira o seu nome: ").strip()
    validar_nome(nome)
    print("Olá,", nome)
except ValueError as e:
    print("Erro:", e)
