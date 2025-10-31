
# 9 - Faça um algoritmo que calcule o IMC (Índice de Massa Corporal) de uma pessoa, 
# leia o seu peso e sua altura e imprima na tela sua condição 
# de acordo com a tabela abaixo:
# Fórmula do IMC = peso / (altura) ²
"""
Tabela Condições IMC

 Abaixo de 18,5   | Abaixo do peso          

 Entre 18,6 e 24,9 | Peso ideal (parabéns)  

 Entre 25,0 e 29,9 | Levemente acima do peso

 Entre 30,0 e 34,9 | Obesidade grau I 

 Entre 35,0 e 39,9 | Obesidade grau II (severa)

 Maior ou igual a 40 | Obesidade grau III (mórbida)
"""

value1 = float(input("Digite seu peso: "))
value2 = float(input("Digite seu altura: "))
imc= value1/(value2**2)

print("\nAnalisando os valores...")

if imc <= 18.5:
    print(f"Seu imc é de: {imc:.2f}, considerado Abaixo do peso")
elif imc > 18.5 and imc <= 24.9:
    print(f"Seu imc é de: {imc:.2f}, considerado Peso ideal (parabéns)")
elif imc >= 25.0 and imc <= 29.9:
    print(f"Seu imc é de: {imc:.2f}, considerado Levemente acima do peso")
elif imc >= 30.0 and imc <= 34.9:
    print(f"Seu imc é de: {imc:.2f}, considerado Obesidade grau I")
elif imc >= 35.0 and imc <= 39.9:
    print(f"Seu imc é de: {imc:.2f}, considerado Obesidade grau II")
else:
    print(f"Seu imc é de: {imc:.2f}, considerado Obesidade grau III (mórbida)")

