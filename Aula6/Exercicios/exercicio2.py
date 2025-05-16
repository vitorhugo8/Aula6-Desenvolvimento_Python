""" Leitura de dois números inteiros do teclado e realizar a divisão dos
números, fazendo os seguintes tratamentos das exeções:
    a) Exista divisão por zero
    b) Um dos nnúmeros digitados não é número """

def dividir():
    try:
        a = int(input("Insira um número inteiro: "))
        b = int(input("Insira mais um número inteiro: "))
        resultado = a / b
        print("Resultado da divisão:", resultado)
    except ZeroDivisionError:
        print("Erro: divisão por zero!")
    except ValueError:
        print("Erro: você não digitou um número inteiro válido!")

dividir()

    

