import pandas as pd
import json

# Versão corrigida e otimizada para frontend
while True:
    try:
        # Dados de entrada (com tratamento básico de erros)
        novo_aluno = {
            "Aluno": input("Nome do aluno: ").strip(),
            "Bimestre1": max(0, min(10, float(input("Nota B1 (0-10): ")))),
            "Bimestre2": max(0, min(10, float(input("Nota B2 (0-10): ")))),
            "Bimestre3": max(0, min(10, float(input("Nota B3 (0-10): ")))),
            "Bimestre4": max(0, min(10, float(input("Nota B4 (0-10): "))))
        }

        # Criação do DataFrame
        df = pd.DataFrame([novo_aluno])
        df["Média"] = df[["Bimestre1", "Bimestre2", "Bimestre3", "Bimestre4"]].mean(axis=1).round(2)

        # Exportação (com tratamento de encoding)
        with open("notas.json", "w", encoding='utf-8') as f:
            f.write(df.to_json(orient="records", indent=2, force_ascii=False))
        
        df.to_csv("notas.csv", index=False, encoding='utf-8-sig')  # CSV com BOM para Excel

        print("\n✅ Dados salvos em 'notas.json' e 'notas.csv'!")
        break

    except ValueError:
        print("\n Erro: Insira apenas números nas notas (0-10)! Tente novamente.\n")
    except Exception as e:
        print(f"\n Erro inesperado: {str(e)}")
        break