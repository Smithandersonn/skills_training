# Recebe dois números como parâmetros
# RETORNA uma tupla com: (soma, subtração, multiplicação, divisão)
# Agora modifique para DESEMPACOTAR a tupla:
# LISTA (mutável):lista = [10, 20, 30]
# TUPLA (imutável):tupla = (10, 20, 30)

def calc(value1, value2):
    soma = (value1 + value2)
    subtracao = (value1 - value2)
    multiplicacao = (value1 * value2)
    divisao = (value1 / value2)
    return  (soma, subtracao, multiplicacao, divisao)
    
print("Insira os Dados Abaixo: ")

value1 = int(input(f"\nDigite o Primeiro Valor: "))
value2 = int(input("Digite o Primeiro Valor: "))

soma, subtracao, multiplicacao, divisao = calc(value1, value2)

print(f"\nA soma de {value1} + {value2} = {soma}")
print(f"A subtração de {value1} - {value2} = {subtracao}")
print(f"A multiplicação de {value1} x {value2} = {multiplicacao}")
print(f"A divisão de {value1} / {value2} = {divisao:.2f}")



