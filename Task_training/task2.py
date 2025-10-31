# 2 - Faça um algoritmo para receber um número qualquer e imprimir na tela se o número é par ou ímpar, positivo ou negativo.

value = int(input("Digite seu numero: "))

if value % 2 == 0:
    print(f"O número digitado:{value}, é par")
else:
    print(f"O número digitado:{value}, é impar")
    

if value > 0:
        print("E é um número positivo")
elif value < 0:
     print("E é um número negativo")
else:
     print("E é um número neutro")
     
     