    # 1 - Faça um algoritmo que leia os valores de A, B, C e em seguida imprima na tela a soma entre A e B é mostre se a soma é menor que C.

    A = int(input("Digite o Valor de 'A':"))
    B = int(input("Digite o Valor de 'B':"))
    C = int(input("Digite o Valor de 'C':"))

    soma_AB = A + B

    print (f"A soma A+B={soma_AB})

    if soma_AB < C:
        print(f"A Soma de A + B:{soma_AB} ,é menor que o Valor de 'C': {C}")
    elif soma_AB == C:
        print(f"A Soma de A + B:{soma_AB} ,é igual  ao Valor de 'C': {C}")
    else:
        print(f"A Soma de A + B:{soma_AB}, é maior que o Valor de 'C': {C}")
