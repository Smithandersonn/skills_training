# 8 - Faça um algoritmo que leia três valores inteiros diferentes e imprima na tela os valores em ordem decrescente.

A  = int(input("Insira o primeiro valor: "))
B  = int(input("Insira o segundo valor: "))
C  = int(input("Insira o terceiro valor: "))


# Encontrar o maior, menor e intermediário
maior = max(A, B, C)
menor = min(A, B, C)
intermediario = A + B + C - maior - menor  # Matemática simples

print(f"Valores em ordem decrescente: {maior}, {intermediario}, {menor}")