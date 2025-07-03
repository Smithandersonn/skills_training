#Desafio da Calculadora Python
def calc():
    while True: 
        #Exibindo Menu de Opções
        print ("\nDesafio da Calculadora Python")
        print ("\nEscolha uma Expressão Numérica:")
        print ("1.Adição")
        print ("2.Subtração")
        print ("3.Multiplicação")
        print ("4.Divisão")
        print ("5.Potenciação")
        print ("6.Radiciação")
        print ("0.Sair")

        opcao = input("\nDigite o numero de sua escolha:")
        if opcao == ("0"):
            print ("\nFechando Calculadora...")
            break

        #Verificando se a opção é válida
        if opcao in ['1', '2', '3', '4', '5', '6']:
            try:
                valor1 =float(input("Digite o Primeiro Valor:"))
                if opcao != '6':
                    valor2 =float(input("Digite o Segundo Valor:"))

                    #Operações Matemáticas
                    #SOMA
                    if opcao == '1':
                        resultado = valor1 + valor2
                        print (f"\nO Resultado da soma {valor1:g} + {valor2:g} é: {resultado:g}")
                    #SUBTRAÇÃO
                    if opcao == "2":
                        resultado = valor1 - valor2
                        print (f"\nO Resultado da subtração {valor1:g} - {valor2:g} é: {resultado:g}")
                    #MULTIPLICAÇÃO
                    elif opcao == "3":
                        resultado = valor1 * valor2
                        print (f"\nO Resultado da multiplicação {valor1:g} x {valor2:g} é: {resultado:g}")
                    #DIVISÃO
                    elif opcao == "4":
                        if valor2 == 0:
                            print("\nErro: Divisão por zero não é permitida!")
                        else:
                            resultado = valor1 / valor2
                        print (f"\nO Resultado da divisão {valor1:g} / {valor2:g} é: {resultado:g}")
                    #POTENCIAÇÃO
                    elif opcao == "5":
                        resultado = valor1 ** valor2
                        print (f"\nO Resultado da potenciação {valor1:g} ^ {valor2:g} é: {resultado:g}")
                #RADICIAÇÃO
                elif opcao == "6":    
                    if valor1 < 0:
                            print("\nErro: Não é possível calcular a raiz quadrada de um número negativo!")
                    else:
                        resultado = valor1 ** 0.5
                        print (f"\nO Resultado da radiciação {valor1:g} ** 0.5 é: {resultado:g}")

                    #Perguntar se o usuário deseja realizar outra operação
                    continuar = input("\n Deseja Realizar outra operação s/n?:").lower()
                    if continuar != "s":
                        print ("\nFechando Calculadora...")
                        break   

            except ValueError:
                print("Erro: Digite valores numéricos válidos!")
        else:
            print("Opção inválida! Digite um número de 1 a 6.")

#Iniciando a Calculadora
calc()