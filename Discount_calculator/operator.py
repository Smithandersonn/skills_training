#Descontos ultilizando porcentagem
salário =float(input("Digite o Valor do Salário:"))
if salário <= 1693.72:
    desconto = salário*0.08
elif salário <= 2822.90:
    desconto = salário*0.09
elif salário <= 5645.80:
    desconto = salário * 0.11
else :
    desconto = 621.04
print(f"O Valor do Desconto é de R$ {desconto:.2f}")