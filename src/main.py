import os
from get_information import dados_cursos
import pandas as pd


df_curso = pd.DataFrame(dados_cursos).T

# Salvar o DataFrame como um arquivo Excel
df_curso.to_excel('data/curso_sebrae.xlsx', index=True)

print("Arquivo salvo com sucesso em 'data/curso_sebrae.xlsx'")
