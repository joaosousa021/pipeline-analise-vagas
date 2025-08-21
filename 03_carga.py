
import pandas as pd
import sqlite3

print("Iniciando a carga para o banco de dados...")

conn = sqlite3.connect('vagas.db')

df = pd.read_csv('vagas_processadas.csv')

df.to_sql('vagas', conn, if_exists='replace', index=False)

print("\nDados carregados com sucesso na tabela 'vagas' do banco de dados 'vagas.db'.")

print("\nVerificando 5 primeiras vagas no banco de dados:")
df_do_banco = pd.read_sql('SELECT * FROM vagas LIMIT 5', conn)
print(df_do_banco)

conn.close()