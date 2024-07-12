from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Definindo Navegador
servico = Service(ChromeDriverManager().install()) # Verifica a versão e instala a atual
navegador = webdriver.Chrome(service=servico)

# Entrando no site
navegador.get("https://pypy.pipedrive.com/")

# Cooldown
time.sleep(2)

# Realizando o login
username = navegador.find_element(By.NAME, "login")
username.send_keys("nevesic681@bacaki.com")
password = navegador.find_element(By.NAME, 'password')
password.send_keys("010903Lucas")
time.sleep(2)
password.send_keys(Keys.RETURN)

# Cooldown
time.sleep(2)

# Acessando KPIs
navegador.get("https://pypy.pipedrive.com/progress/insights")
time.sleep(13)
botao_novo_KPI = navegador.find_element(By.CSS_SELECTOR, 'button[data-test="add-new-item-button"]')
botao_novo_KPI.click()
time.sleep(2)
botao_criar_KPI = navegador.find_element(By.XPATH, '//button[span[text()="Relatório"]]') # cui5-button__label
botao_criar_KPI.click()



# Fim
time.sleep(7)