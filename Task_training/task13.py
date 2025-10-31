 # 13 - Faça algoritmo que leia o nome e a idade de uma pessoa e imprima na tela o nome da pessoa e se ela é maior ou menor de idade. 


print("Preencha os campos abaixo!")

name = input("\nDigite seu nome: ")
age = int(input("Digite sua idade: "))

if age >= 18:
    print(f"{name} é maior de idade.")
else:
    print(f"{name} é menor de idade.")



