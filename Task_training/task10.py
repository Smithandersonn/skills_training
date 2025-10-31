 # 10 - Faça um algoritmo que leia três notas obtidas por um aluno, e imprima na tela a média das notas.
print("Preencha os Campos ultilizando o '.' seguindo o exemplo abaixo!")
print("7.5")

value1 = float(input("\nDigite o valor da primeira nota: "))
value2 = float(input("Digite o valor da segunda nota: "))
value3 = float(input("Digite o valor da terceira nota: "))

mediaFinal = (value1 + value2 + value3)/3

print(f"\nA média final das notas é de: {mediaFinal:.2f}")