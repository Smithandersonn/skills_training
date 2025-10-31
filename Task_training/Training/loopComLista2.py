# Crie um programa que armazene 3 nomes em uma lista e depois mostre todos.
# Dica: Você vai precisar de:
# Uma lista vazia: nomes = []
# Loop para ler os nomes
# nomes.append(nome) para adicionar
# Outro loop para mostrar
# Mostre seu código quando terminar! 💻✨
# Excelente progresso! Você já domina loops com acumulação! 🚀


nomes =[]
quantidade =int(input("Digite a Quantidade de Nomes desejados: "))
for i in range(quantidade):
    name = input("Insira um nome: ")
    nomes.append(name)

print(f"\nO nomes inseridos são: ")

for nome in nomes:
    print(nome)

