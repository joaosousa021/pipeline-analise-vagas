import pandas as pd
import re

print("Iniciando a transformação dos dados...")

df = pd.read_csv('vagas_brutas.csv')

df = df.drop_duplicates(subset=['titulo', 'empresa', 'descricao'])

df['descricao'] = df['descricao'].apply(lambda texto: re.sub(r'\s+', ' ', str(texto)).strip())

df['descricao_limpa'] = df['descricao'].str.lower()

skills_list = [
    'python', 'sql', 'power bi', 'tableau', 'aws', 'azure', 'gcp', 
    'spark', 'airflow', 'docker', 'kafka', 'mongodb', 'postgresql'
]

for skill in skills_list:
    df[f'tem_{skill}'] = df['descricao_limpa'].apply(lambda x: 1 if skill in x else 0)


df = df.drop(columns=['descricao_limpa'])


df.to_csv('vagas_processadas.csv', index=False)

print("\nTransformação finalizada! Dados limpos e enriquecidos salvos em 'vagas_processadas.csv'.")
print("Veja as primeiras linhas do resultado corrigido:")
print(df.head())