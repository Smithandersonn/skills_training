def calc():
    while True:
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

        continuar = input("\nDeseja fazer outra operação Sim ou Não: ").lower()
        if continuar != "sim":
            print("Fechando Caluladora...")
            break

calc()