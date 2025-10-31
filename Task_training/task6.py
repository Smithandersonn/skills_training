# 6 - Faça um algoritmo que leia um valor qualquer e imprima na tela com um reajuste de 5%.

value = int(input("Digite o Valor desejado: "))
reajuste = (value*5/100)

print("Analisando os Dados...")
print(f"{value}+5% é = {value+reajuste:.2f}")


