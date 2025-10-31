# Recebe dois números como parâmetros
# RETORNA uma tupla com: (soma, subtração, multiplicação, divisão)

def calc(value1, value2):
    resultado = [value1 + value2, value1 - value2, value1 * value2, value1 / value2]
    return  resultado
    
print("Insira os Dados Abaixo: ")

value1 = int(input(f"\nDigite o Primeiro Valor: "))
value2 = int(input("Digite o Primeiro Valor: "))

valores = calc(value1, value2)
print(valores)


