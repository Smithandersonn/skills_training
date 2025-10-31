#    🚀 EXERCÍCIOS DE CONSOLIDAÇÃO - TODOS OS CONCEITOS
#    📝 EXERCÍCIO 1: SISTEMA DE NOTAS COMPLETO
#    Crie um programa com funções para:
#    Calcular média de uma lista de notas
#    Verificar se aluno foi aprovado (média >= 7)
#    Retornar situação do aluno

#    Requisitos:
#    Use loops para entrada de notas
#    Funções com parâmetros e retorno
#    Listas para armazenar notas
# a Função sum, soma todos os valores dentro da lista
# a função len, fala quantos itens tem dentro da lista

def cal_media(notas):
    soma = sum (notas)
    quantidade = len(notas)
    media = soma/quantidade
    return media

aluno = input("Informe o nome do aluno: ")

notas = []
orden = 1

for i in range(4):
    nota = float(input(f"Digite a {orden} nota: "))
    notas.append(nota)
    orden = orden + 1

resultado = cal_media(notas)
if resultado >=7:
    print(f"O Aluno(a) {aluno}, foi Aprovado! : {resultado}")
else:
      print(f"O Aluno(a) {aluno}, foi Reprovado! : {resultado}")