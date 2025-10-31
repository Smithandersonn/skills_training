#    DESAFIO AVANÇADO FINAL:
#    Transforme em um sistema completo:
#    Pergunte quantas notas o aluno tem
#    Use essa quantidade no range()
#    Adicione função verificar_aprovacao(media)
#    Mostre todas as notas + média + situação

def calc(notas):
    soma = sum(notas)
    quantidade = len(notas)
    media = soma/quantidade
    return media

def aprovacao(resultado):
    if resultado >=7:
        return "Aprovado(a)"
    else:
        return "Reprovado(a)!"
    
print("Insira os dados abaixo!")

quantidade_notas = int(input(f"\nQuantidades de notas?: "))
aluno = input("Digite o nome do Aluno (a): ")

notas = []
indice = 1

for i in range(quantidade_notas):
    nota = float(input(f"Digite a {indice}º nota: "))
    indice = indice + 1
    notas.append(nota)

resultado = calc(notas)
situacao = aprovacao(resultado)

print(f"{resultado:.2f}")
print(f"O Aluno(a): {aluno} foi:{situacao}")

