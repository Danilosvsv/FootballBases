from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Link da liga que será gerada o webscrapping
link = 'https://www.flashscore.com.br/futebol/brasil/serie-a/resultados/'

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(link)

# Automatizar quantidade de clicks?

driver.find_element_by_link_text('Mostrar mais jogos').click()
driver.find_element_by_link_text('Mostrar mais jogos').click()

content = driver.page_source
soup = BeautifulSoup(content)

sTipoPartida1 = []
sTipoPartida2 = []
for i in range(len(soup.find_all("div", {"class": "event__match event__match--static event__match--twoLine"}))):
    sTipoPartida1.append(soup.find_all("div", {"class": "event__match event__match--static event__match--twoLine"})[i])
for i in range(len(soup.find_all("div", {"class": "event__match event__match--static event__match--last event__match--twoLine"}))):
    sTipoPartida2.append(soup.find_all("div", {"class": "event__match event__match--static event__match--last event__match--twoLine"})[i])

sPartidasHtml = sTipoPartida1+sTipoPartida2

test = str(sPartidasHtml).split(' ')
f = []
for i in range(len(test)):
    if(test[i][0:3]=='id='):
        dado = test[i].split('id="g_1_')[1]
        id_padrao = ''.join(char for char in dado if char.isalnum())
        f.append(id_padrao)
urls= []
for i in range (len(f)):
    url = 'https://www.flashscore.com.br/jogo/'+f[i]+'/#/resumo-de-jogo/estatisticas-de-jogo/0'
    urls.append(url)

clube_mandante = []
clube_visitante = []
placar_mandante = []
placar_visitante = []
posse_de_bola_mandante = []
posse_de_bola_visitante = []
tentativas_de_gol_mandante = []
tentativas_de_gol_visitante = []
finalizacoes_mandante =[]
finalizacoes_visitante =[]
chutes_fora_mandante = []
chutes_fora_visitante = []
chutes_bloqueados_mandante =[]
chutes_bloqueados_visitante =[]
faltas_cobradas_mandante =[]
faltas_cobradas_visitante =[]
escanteios_mandante = []
escanteios_visitante = []
impedimentos_mandante = []
impedimentos_visitante = []
laterais_cobrados_mandante = []
laterais_cobrados_visitante = []
defesas_de_goleiro_mandante = []
defesas_de_goleiro_visitante = []
faltas_mandante = []
faltas_visitante = []
cartoes_vermelhos_mandante = []
cartoes_vermelhos_visitante = []
cartoes_amarelos_mandante = []
cartoes_amarelos_visitante = []
total_de_passes_mandante = []
total_de_passes_visitante = []
passes_completados_mandante = []
passes_completados_visitante = []
desarmes_mandante = []
desarmes_visitante = []
ataques_mandante = []
ataques_visitante = []
ataques_perigosos_mandante = []
ataques_perigosos_visitante = []
placar_mandante = []
placar_visitante = []
clube_mandante = []
clube_visitante = []

for i in range(len(urls)):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(urls[i])
    time.sleep(0.200)

    content = driver.page_source
    soup = BeautifulSoup(content)

    base = []
    for i in range (len(soup.find_all('div', class_='stat__category'))):
        base.append(soup.find_all('div', class_='stat__category')[i].text)
    base_padronizada = []
    for i in range(len(base)):
        string_semnum = ''.join([i for i in base[i] if not i.isdigit()])
        string_semcaracterespecial = ''.join(char for char in string_semnum if char.isalnum())
        base_padronizada.append(string_semcaracterespecial);
   

    placar_mandante.append(soup.find_all('div', class_='detailScore__wrapper')[0].text.split("-")[0])
    placar_visitante.append(soup.find_all('div', class_='detailScore__wrapper')[0].text.split("-")[1])
    clube_mandante.append(soup.find_all('title')[0].text.split("|")[1].split(" - ")[0].strip())
    clube_visitante.append(soup.find_all('title')[0].text.split("|")[1].split(" - ")[1].strip())
                           
    for i in range (len(base)):
        if base_padronizada[i]=='Possedebola':
            posse_de_bola_mandante.append(base[i].split("Posse de bola")[0])
            posse_de_bola_visitante.append(base[i].split("Posse de bola")[1])
        elif base_padronizada[i]=='Tentativasdegol':
            tentativas_de_gol_mandante.append(base[i].split("Tentativas de gol")[0])
            tentativas_de_gol_visitante.append(base[i].split("Tentativas de gol")[1])
        elif base_padronizada[i]=='Finalizações':
            finalizacoes_mandante.append(base[i].split("Finalizações")[0])
            finalizacoes_visitante.append(base[i].split("Finalizações")[1])
        elif base_padronizada[i]=='Chutesfora':
            chutes_fora_mandante.append(base[i].split("Chutes fora")[0])
            chutes_fora_visitante.append(base[i].split("Chutes fora")[1])
        elif base_padronizada[i]=='Chutesbloqueados':
            chutes_bloqueados_mandante.append(base[i].split("Chutes bloqueados")[0])
            chutes_bloqueados_visitante.append(base[i].split("Chutes bloqueados")[1])
        elif base_padronizada[i]=='Faltascobradas':
            faltas_cobradas_mandante.append(base[i].split("Faltas cobradas")[0])
            faltas_cobradas_visitante.append(base[i].split("Faltas cobradas")[1])
        elif base_padronizada[i]=='Escanteios':
            escanteios_mandante.append(base[i].split("Escanteios")[0])
            escanteios_visitante.append(base[i].split("Escanteios")[1])
        elif base_padronizada[i]=='Impedimentos':
            impedimentos_mandante.append(base[i].split("Impedimentos")[0])
            impedimentos_visitante.append(base[i].split("Impedimentos")[1])
        elif base_padronizada[i]=='Lateraiscobrados':
            laterais_cobrados_mandante.append(base[i].split("Laterais cobrados")[0])
            laterais_cobrados_visitante.append(base[i].split("Laterais cobrados")[1])
        elif base_padronizada[i]=='Defesasdogoleiro':
            defesas_de_goleiro_mandante.append(base[i].split("Defesas do goleiro")[0])
            defesas_de_goleiro_visitante.append(base[i].split("Defesas do goleiro")[1])
        elif base_padronizada[i]=='Faltas':
            faltas_mandante.append(base[i].split("Faltas")[0])
            faltas_visitante.append(base[i].split("Faltas")[1])
#         elif base_padronizada[i]=='Cartõesvermelhos':
#             cartoes_vermelhos_mandante.append(base[i].split("Cartões vermelhos")[0])          
#             cartoes_vermelhos_visitante.append(base[i].split("Cartões vermelhos")[1])               
#         elif base_padronizada[i]=='Cartõesamarelos':
#             cartoes_amarelos_mandante.append(base[i].split("Cartões amarelos")[0])
#             cartoes_amarelos_visitante.append(base[i].split("Cartões amarelos")[1])      
        elif base_padronizada[i]=='Totaldepasses':
            total_de_passes_mandante.append(base[i].split("Total de passes")[0])
            total_de_passes_visitante.append(base[i].split("Total de passes")[1])
        elif base_padronizada[i]=='Passescompletados':
            passes_completados_mandante.append(base[i].split("Passes completados")[0])
            passes_completados_visitante.append(base[i].split("Passes completados")[1])
        elif base_padronizada[i]=='Desarmes':
            desarmes_mandante.append(base[i].split("Desarmes")[0])
            desarmes_visitante.append(base[i].split("Desarmes")[1])
        elif base_padronizada[i]=='Ataques':
            ataques_mandante.append(base[i].split("Ataques")[0])
            ataques_visitante.append(base[i].split("Ataques")[1])
        elif base_padronizada[i]=='AtaquesPerigosos':
            ataques_perigosos_mandante.append(base[i].split("Ataques Perigosos")[0])
            ataques_perigosos_visitante.append(base[i].split("Ataques Perigosos")[1])

#  if(len(cartoes_vermelhos_mandante)<(i+1)):
#                 cartoes_vermelhos_mandante.append('0')
#  if(len(cartoes_vermelhos_visitante)<(i+1)):
#                 cartoes_vermelhos_visitante.append('0')

#   if(len(cartoes_amarelos_mandante)<(i+1)):
#                 cartoes_amarelos_mandante.append('0')
#             if(len(cartoes_amarelos_visitante)<(i+1)):
#                 cartoes_amarelos_visitante.append('0')   

df = pd.DataFrame({'clube_mandante':clube_mandante,
               'clube_visitante':clube_visitante,
               'placar_mandante':placar_mandante,
               'placar_visitante':placar_visitante,
               'posse_de_bola_mandante':posse_de_bola_mandante,
               'posse_de_bola_visitante':posse_de_bola_visitante,
               'tentativas_de_gol_mandante':tentativas_de_gol_mandante,
               'tentativas_de_gol_visitante':tentativas_de_gol_visitante,
               'chutes_fora_mandante':chutes_fora_mandante,
               'chutes_fora_visitante':chutes_fora_visitante,
               'chutes_bloqueados_mandante':chutes_bloqueados_mandante,
               'chutes_bloqueados_visitante':chutes_bloqueados_visitante,
               'faltas_cobradas_mandante':faltas_cobradas_mandante,
               'faltas_cobradas_visitante':faltas_cobradas_visitante,
               'escanteios_mandante':escanteios_mandante,
               'escanteios_visitante':escanteios_visitante,
#                'impedimentos_mandante':impedimentos_mandante,
#                'impedimentos_visitante':impedimentos_visitante,
               'laterais_cobrados_mandante':laterais_cobrados_mandante,
               'laterais_cobrados_visitante':laterais_cobrados_visitante,
               'defesas_de_goleiro_mandante':defesas_de_goleiro_mandante,
               'defesas_de_goleiro_visitante':defesas_de_goleiro_visitante,
               'faltas_mandante':faltas_mandante,
               'faltas_visitante':faltas_visitante,
#                'cartoes_amarelos_mandante':cartoes_amarelos_mandante,
#                'cartoes_amarelos_visitante':cartoes_amarelos_visitante,
#                'cartoes_vermelhos_mandante':cartoes_vermelhos_mandante,
#                'cartoes_vermelhos_visitante':cartoes_vermelhos_visitante,
               'total_de_passes_mandante':total_de_passes_mandante,
               'total_de_passes_visitante':total_de_passes_visitante,
               'passes_completados_mandante':passes_completados_mandante,
               'passes_completados_visitante':passes_completados_visitante,
               'desarmes_mandante':desarmes_mandante,
               'desarmes_visitante':desarmes_visitante,
               'ataques_mandante':ataques_mandante,
               'ataques_visitante':ataques_visitante,
               'ataques_perigosos_mandante':ataques_perigosos_mandante,
               'ataques_perigosos_visitante':ataques_perigosos_visitante,
               'urls':urls})   

# return df
df.to_csv('Brasileirao_SerieA2022_Atualizado.csv')