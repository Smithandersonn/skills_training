#Backend (Python/Pandas) → Processa os dados e gera um arquivo (CSV/JSON) para o frontend.
import pandas as pd
import json

# Dados de exemplo (ou input do usuário)

novo_aluno = {
    "Aluno": input("Nome do aluno: "),  # Texto (string)
    "Bimestre1": float(input("Nota B1: ")),  # Converter para float
    "Bimestre2": float(input("Nota B2: ")),
    "Bimestre3": float(input("Nota B3: ")),
    "Bimestre4": float(input("Nota B4: "))
        }

df = pd.DataFrame([novo_aluno]) #Cria o DataFrame
df["Média"] = df[["Bimestre1", "Bimestre2", "Bimestre3", "Bimestre4"]].mean(axis=1).round(2)

'''
pd.DataFrame(novo_aluno) cria o DataFrame a partir do dicionário.
df.mean(axis=1) calcula a média por linha (axis=1) 
round(2) arredonda para 2 casas decimais.
'''

# Exporta para JSON (ideal para frontend)
df.to_json("notas.json", orient="records", indent=2, force_ascii=False)

"""
notas.json é o nome do arquivo de saída.
orient="records" organiza os dados como uma lista de registros (dicionários).
indent=2 formata o JSON com indentação para melhor legibilidade.
force_ascii=False permite caracteres especiais (como acentos) no JSON.
exibir a palavra média com acento ao exportar para JSON.
"""
# Opcional: Exporta para CSV (se preferir)
df.to_csv("notas.csv", index=False)
"""
notas.csv é o nome do arquivo de saída.
index=False evita que o índice do DataFrame seja salvo no CSV.
"""


#incluir depois,  Input Dinâmico (opcional), Adicionar Status (Aprovado/Reprovado),Validação dos Dados,Ordenar por Média