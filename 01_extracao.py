import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

print("Iniciando a extração de vagas...")

dados_vagas = []

for i in range(1, 4):
    url = f"https://programathor.com.br/jobs?page={i}&q=Dados"
    
    print(f"Buscando na página {i}...")

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        cards_vagas = soup.find_all('div', class_='cell-list')

        for vaga in cards_vagas:
            tag_titulo = vaga.find('h3')
            spans = vaga.find_all('span') 
            tag_link = vaga.find('a')

            
            if tag_titulo and tag_link and len(spans) >= 3:
              
                titulo = tag_titulo.text.strip()
                empresa = spans[1].text.strip()  
                local = spans[2].text.strip()   
                link_vaga = "https://programathor.com.br" + tag_link['href']
                
                response_vaga = requests.get(link_vaga)
                if response_vaga.status_code == 200:
                    soup_vaga = BeautifulSoup(response_vaga.content, 'html.parser')
                    tag_descricao = soup_vaga.find('div', class_='wrapper-content-job-show')
                    if tag_descricao:
                        descricao = tag_descricao.text.strip()
                    else:
                        descricao = "Descrição não encontrada."
                else:
                    descricao = "Não foi possível obter a descrição."

                dados_vagas.append({
                    'titulo': titulo,
                    'empresa': empresa,
                    'local': local,
                    'descricao': descricao
                })
            
            else:
                print("--> AVISO: Um card de vaga foi ignorado por não ter o formato esperado.")

            time.sleep(1)

    else:
        print(f"Erro ao acessar a página {i}. Status code: {response.status_code}")

df = pd.DataFrame(dados_vagas)
df.to_csv('vagas_brutas.csv', index=False)

print(f"\nExtração finalizada! {len(df)} vagas salvas em 'vagas_brutas.csv'.")