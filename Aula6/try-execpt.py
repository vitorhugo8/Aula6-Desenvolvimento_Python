""" Reolvendo as Excessões: 
    try:
        <código passivel de erro>
    execpt Erro:
        <Código que irá trtar o erro>
        <mensagem informando o erro encontrado>"""
import math 
num = 400

try: 
    result = math.sqrt(num)
    print("A raiz quadrada", result)
except Exception:
    print("Não existe a raiz quadrada de numero negativo")

# ========= Exemplo 2 ==================
import math 
num = -1

try: 
    result = math.sqrt(num)
    print("A raiz quadrada", result)
except ValueError:
    num = -num
    print("Transformando numero negativo em positivo")
    result = math.sqrt(num)
    print("A raiz quadrada", result)


# ========= Exemplo 3 ==================
try:
    x = int(input("Enter number: "))
    x += 1
    print(x)
except:
    print("Invalid input")

# ========= Exemplo 4 ==================
try:
    x = int(input("Enter number: "))
    x += 1
    print(x)
except:
    print("Invalid input")
finally:
    print("Valid input!") # O que está dentro do bloco 'finally' sempre será executado

# ========= Exemplo 5 ==================
def div(a, b):
    try:
        result = a / b 
    except ZeroDivisionError:
        print("Division by zero")
    else:
        print("Result is", result)

div(2, 0)

# ========= Exemplo 6 ==================
def dividir():
    try:
        num1 = int(input("Primeiro numero: "))
        num2 = int(input("Segundo numero: "))
        result = (num1 / num2)
        print("Divisão: ", result)
    except ValueError:
        print("Dado informado inválido")
    except ZeroDivisionError:
        print("Divisão por zero!")

dividir()

# ========= Exemplo 7 ==================
def verifica_divisao():
    try: 
        dividir()
    except ValueError:
        print("Dado informado inválido")
    except ZeroDivisionError:
        print("Divisão por zero")

verifica_divisao()

# ========= Exemplo 8 ==================
def ReadFile():
    try:
        print("Abrindo um arquivo!")
        open("texto.txt", "r")
    except FileNotFoundError:
        print("O Arquivo não existe")

ReadFile()

# ========= Exemplo 9 ==================
try:
    print("Abrindo um arquivo!")
    open("texto.txt", "r")
except FileNotFoundError as captura:
        print(captura)

# ========= Exemplo 10 ==================
import os 

try:
    os.remove("teste.txt")
    print("Arquivo Removido!")
except FileNotFoundError as erro:
    print("Erro: ", erro)
    print("Aviso: Arquivo Inexistente!")
except PermissionError as erro:
    print("Erro", erro)
    print("Sem permissão de acesso")
except IsADirectoryError as erro:
    print("Erro: ", erro)
    print("Tentativa de remover diretório!")

# ========= Exemplo 11 ==================
try: 
    os.rename("teste_orig.txt", "teste_dest.txt")
    print("Arquivo Renomeado")
except FileNotFoundError as erro:
    print("Erro: ", erro)
    print("Aviso: Arquivo Inexistente!")
except PermissionError as erro:
    print("Erro: ", erro)
    print("Sem permissão de acesso")
except FileExistsError as erro:
    print("Erro: ", erro)
    print("Arquivo destino já existe!")


