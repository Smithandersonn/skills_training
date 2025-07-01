#Desacio da Calculadora Python
print ("Escolha uma Expressão Numérica:")
print ("1.Adição")
print ("2.Subtração")
print ("3.Multiplicação")
print ("4.Divisão")
print ("5.Potenciação")
print ("6.Radiciação")
    
opcao = input("Digite o numéro de sua escolha:")

if opcao in ['1', '2', '3', '4', '5', '6']:
    try:
        valor1 =float(input("Digite o Primeiro Valor:"))
        if opcao != '6':
            valor2 =float(input("Digite o Segundo Valor:"))
        if opcao == '1':
            resultado = valor1 + valor2
            print (f"o Resoltado da soma é: {resultado:g}")
    except ValueError:
        print("Erro: Digite valores numéricos válidos!")
else:
    print("Opção inválida! Digite um número de 1 a 6.")