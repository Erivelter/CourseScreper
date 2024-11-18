from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

driver = webdriver.Chrome()
driver.get("https://sebrae.com.br/sites/PortalSebrae/cursosonline")

def fechar_modal():
    try:
        fechar_modal_localização = driver.find_element(By.XPATH, '//*[@id="location-modal"]/div/div/span')
        fechar_modal_localização.click()
    except NoSuchElementException:
        pass

def veja_mais():
    try:
        veja_mais_localizacao = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="showMore"]'))
)
        veja_mais_localizacao.click()
        time.sleep(2)

    except Exception as e:
        print(f"Erro ao tentar clicar em 'Veja mais': {e}")


def get_information(x):
    try:
        titulo = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="list-cards"]/div[{x}]/div[2]/div[2]'))
        ).text
        duracao = driver.find_element(By.XPATH,f'//*[@id="list-cards"]/div[{x}]/div[2]/div[3]/span[3]').text
        preco = driver.find_element(By.XPATH,f'//*[@id="list-cards"]/div[{x}]/div[2]/div[3]/span[1]').text
        

        informacao = {
                "titulo": titulo,
                "duração": duracao,
                "preço": preco
            }
        return informacao
    except NoSuchElementException:
        print(f"Problema ao coletar informações do curso {x}.")
        return None




fechar_modal()

dados_cursos = {}
for x in range(1,406 ):#o total de cursos que exitem hoje
    if x % 6 == 0:
        veja_mais()
    dados = get_information(x)

    if dados:
        dados_cursos[f'curso_{x}'] = dados
        os.system('cls' if os.name == 'nt' else 'clear') 
        print(f"Progresso: {x} cursos computados")
        time.sleep(0.1)
#print(dados_cursos)
print(f"\nTotal de cursos coletados: {len(dados_cursos)}")
driver.quit()

