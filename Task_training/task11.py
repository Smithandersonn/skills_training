# 11 - Faça um algoritmo que leia quatro notas obtidas por um aluno,
# calcule a média das nota obtidas, imprima na tela o nome do aluno e 
# se o aluno foi aprovado ou reprovado. 
# Para o aluno ser considerado aprovado sua média final deve ser maior ou igual a 7.


print("Preencha os Campos Abaixo!")

aluno = input("\nDigite o nome do Aluno: ")

print("Preencha os Campos ultilizando o '.' seguindo o exemplo abaixo!")
print("7.5")

n1 = float(input("\nDigite o valor da primeira nota: "))
n2 = float(input("Digite o valor da segunda nota: "))
n3 = float(input("Digite o valor da terceira nota: "))
n4 = float(input("Digite o valor da quarta nota: "))

mediaFinal = (n1 + n2 + n3 + n4)/4



if mediaFinal >=7:
    print(f"\nA média do aluno {aluno} é de {mediaFinal:.2f}, foi aprovado com sucesso.")
else:
    print(f"\nA média do aluno {aluno} é de {mediaFinal:.2f}, foi reprovado.")
