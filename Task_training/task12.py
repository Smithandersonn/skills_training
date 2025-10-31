 # 12 - Faça um algoritmo que leia o valor de um produto e determine o valor que deve ser pago, conforme a escolha da forma de pagamento pelo comprador e 
# imprima na tela o valor final do produto a ser pago. Utilize os códigos da tabela de condições de pagamento para efetuar o cálculo adequado.
"""
 Tabela de Código de Condições de Pagamento

 1 - À Vista em Dinheiro ou Pix, recebe 15% de desconto
 2 - À Vista no cartão de crédito, recebe 10% de desconto
 3 - Parcelado no cartão em duas vezes, preço normal do produto sem juros
 4 - Parcelado no cartão em três vezes ou mais, preço normal do produto mais juros de 10%
 """




print("Preencha o Campo abaixo!")

produto = float(input("\nDigite o valor do Produto: "))

operacao1 = (produto*15)/100
operacao2 = (produto*10)/100
operacao4 = (produto*10)/100

print("\n1 - À Vista em Dinheiro ou Pix")
print("2 - À Vista no cartão de crédito")
print("3 - Parcelado no cartão em duas vezes")
print("4 - Parcelado no cartão em três vezes ou mais")

formato= int(input("Escolha sua forma de pagamento!: "))

if formato == 1:
    print(f"O valor do produto saiu com 15% de desconto de {produto} por: {produto - operacao1}")
elif formato == 2:
    print(f"O valor do produto saiu com 10% de desconto de {produto} por: {produto - operacao2}")   
elif formato == 4:
    print(f"O valor do produto saiu por: {produto + operacao4}acrecimo de 10% devida a forma de pagamento")   
else:
    print(f"O valor do produto saiu por: {produto} parcelado em 2 vezes sem juros.")   
       
           