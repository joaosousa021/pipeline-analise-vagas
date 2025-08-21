import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

print("Iniciando a extração de vagas...")

dados_vagas = []

for i in range(1, 4):
    url = f"https://programathor.com.br/jobs?page={i}&q=Dados"
    
    print(f"Buscando na página {i}...")

    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        cards_vagas = soup.find_all('div', class_='cell-list')

        for vaga in cards_vagas:
            # Mantendo os seletores da lista de vagas que já funcionavam
            tag_titulo = vaga.find('h3')
            tag_link = vaga.find('a')
            icon_empresa = vaga.find('i', class_='fa-briefcase')
            tag_empresa_span = icon_empresa.parent if icon_empresa else None
            icon_local = vaga.find('i', class_='fa-map-marker-alt')
            tag_local_span = icon_local.parent if icon_local else None

            if tag_titulo and tag_link and tag_empresa_span and tag_local_span:
                titulo = tag_titulo.text.strip()
                empresa = tag_empresa_span.text.strip()
                local = tag_local_span.text.strip()
                link_vaga = "https://programathor.com.br" + tag_link['href']
                
                try:
                    response_vaga = requests.get(link_vaga, headers=headers, timeout=15)
                    response_vaga.raise_for_status()
                    soup_vaga = BeautifulSoup(response_vaga.content, 'html.parser')
                    
                    # --- A CORREÇÃO FINAL E DEFINITIVA ESTÁ AQUI ---
                    # Este é o seletor exato baseado no HTML que você enviou.
                    tag_descricao = soup_vaga.find('div', class_='line-height-2-4')
                    
                    if tag_descricao:
                        descricao = tag_descricao.get_text(separator=' ', strip=True)
                    else:
                        descricao = "Descrição detalhada não encontrada."
                
                except requests.exceptions.RequestException as e:
                    print(f"--> ERRO ao acessar o link da vaga {titulo}: {e}")
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

    except requests.exceptions.RequestException as e:
        print(f"--> ERRO FATAL ao acessar a página {i}: {e}. Pulando para a próxima página.")

df = pd.DataFrame(dados_vagas)
df.to_csv('vagas_brutas.csv', index=False)

print(f"\nExtração finalizada! {len(df)} vagas salvas em 'vagas_brutas.csv'.")