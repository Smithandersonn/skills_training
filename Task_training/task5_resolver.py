#5 - Faça um algoritmo que leia o valor do salário mínimo e o valor do salário de um usuário, 
#    calcule quantos salários mínimos esse usuário ganha e imprima na tela o resultado. (Base para o Salário mínimo R$ 1.293,20).



salario_base = 1.293,20
salario_user = float(input("Digite o Valor do seu Salario: "))
result = (f"{salario_user:,.2f}")/salario_base
 
print(result)