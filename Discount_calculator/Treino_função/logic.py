#Chamando Valores
salario = float(input("Digite o Valor do Salário: "))
percentual_de_desconto = float(input("Digite o Valor do Desconto (%):"))

#Definindo função de Calculo De porcentagem (%)
def cal_desconto (salario, percentual_de_desconto):
    # percentual_de_desconto vai ser convertido pra decimal e multiplicado pelo salario
    desconto_final = salario * (percentual_de_desconto/100) 
    salario_final = salario - desconto_final
    return salario_final

#Chamando Função 
resultado = cal_desconto(salario, percentual_de_desconto)

"""
percentual_de_desconto:g (:g) remove (.0) se o número for inteiro (ex: 5.0 → 5)
o f no inicio da variavel permite inserir variáveis diretamente dentro da string usando chaves {}
:.2f (Formatação de números) 
: → Indica o início da formatação.
.2 → Define 2 casas decimais após o ponto.
f → Indica que é um float (número decimal).
"""
print (f"O Salario com Desconto de {percentual_de_desconto:g}% é:R${resultado :.2f}")
