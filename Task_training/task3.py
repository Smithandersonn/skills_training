# 3 - Faça um algoritmo que leia dois valores inteiros A e B, se os valores de A e B forem iguais, deverá somar os dois valores, 
# caso contrário devera multiplicar A por B. Ao final de qualquer um dos cálculos deve-se atribuir o resultado a uma variável C e
# imprimir seu valor na tela.

#Coletando dados
A = int(input("Digite o primeiro Valor: "))
B = int(input("Digite o segundo Valor: "))

print(f"\n Analisando os Dados...")

#Comparando Dados
if A == B:
    C = A + B
    print(f"A soma dos valor {A} + {B} é: {C}")
else:
    C = A * B
    print(f"A multiplicação dos valor {A} x {B} é: {C}")


