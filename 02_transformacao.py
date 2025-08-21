import pandas as pd
import re
import spacy
from spacy.matcher import PhraseMatcher

print("Iniciando a transformação dos dados...")

print("Carregando modelo de NLP (spaCy)...")
nlp = spacy.load("pt_core_news_sm")

df = pd.read_csv('vagas_brutas.csv')

df = df.dropna(subset=['descricao']) 
df = df.drop_duplicates(subset=['titulo', 'empresa', 'descricao'])
df['descricao_limpa'] = df['descricao'].apply(lambda texto: re.sub(r'\s+', ' ', str(texto)).strip())

skills_list = [
    'python', 'sql', 'power bi', 'tableau', 'aws', 'azure', 'gcp', 
    'spark', 'airflow', 'docker', 'kafka', 'mongodb', 'postgresql'
]


matcher = PhraseMatcher(nlp.vocab, attr='LOWER')

patterns = [nlp.make_doc(text) for text in skills_list]
matcher.add("SKILL_MATCHER", patterns)

results = []

print("Processando descrições com o modelo de NLP para extrair skills...")
for doc in nlp.pipe(df['descricao_limpa'].str.lower(), disable=["parser", "ner"]):
    matches = matcher(doc)
    
    found_skills = set()
    for match_id, start, end in matches:
        
        span = doc[start:end]
        found_skills.add(span.text)
    
    results.append(found_skills)


for skill in skills_list:
    df[f'tem_{skill}'] = [1 if skill in found_set else 0 for found_set in results]


df.to_csv('vagas_processadas.csv', index=False)

print("\nTransformação finalizada! Dados limpos e enriquecidos com NLP salvos em 'vagas_processadas.csv'.")
print("Veja as primeiras linhas do resultado corrigido:")
print(df.head())