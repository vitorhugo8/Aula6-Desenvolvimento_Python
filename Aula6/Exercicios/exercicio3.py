""" Tendo uma lista de números inteiros, faça o cálculo do fatorial de cada número da lista.
Faça os seguintes tratamentos de exeções: 
    a) Exista um elemento da lista que não seja número
    b) Exista um número negativo.
    """

import math

lista = [2, 4, 6, 8, 10, "a", -3]

for i in lista:
    try:
        # Verifica se é um número inteiro
        if not isinstance(i, int):
            raise ValueError(f"Elemento '{i}' não é um número inteiro.")

        # Verifica se é negativo
        if i < 0:
            raise ValueError(f"Elemento '{i}' é um número negativo.")

        # Calcula o fatorial
        f = math.factorial(i)
        print(f"Fatorial de {i} é {f}")

    except ValueError as e:
        print("Erro:", e)
