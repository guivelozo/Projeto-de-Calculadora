print("== Calculadora Simples ==")

from decimal import Decimal

# Início da entrada de dados
num1 = Decimal(input("Digite o primeiro número: "))
operador = input("Digite o operador (+, -, *, /): ")
num2 = Decimal(input("Digite o segundo número: "))

# Processamento desses dados
if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: divisão por zero"
else:
    resultado = "Operador inválido"

if isinstance(resultado, Decimal) and resultado % 1 == 0:
    resultado = int(resultado)

# Saída
print("Resultado:", resultado)