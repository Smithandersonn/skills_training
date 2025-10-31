# 7 -  Faça um algoritmo que leia dois valores booleanos (lógicos) e determine se ambos são VERDADEIRO ou FALSO.
print("Escolha seu valor Booleanos")
print(f"\n1 - True")
print(f"\n2 - False")
valor1 = int(input("\nEscolha sua primeira Opção 'True/False': "))
valor2 = int(input("\nEscolha sua segunda Opção 'True/False': "))

bool1 = valor1 == 1
bool2 = valor2 == 1


if bool1 and bool2:
    print("Ambos são Verdadeiros")
elif not bool1 and not  bool2:
    print("Ambos são Falsos")
else:
    print("Os Valores são diferentes")

