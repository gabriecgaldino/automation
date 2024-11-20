import os
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

load_dotenv()

folder = r'C:\Users\gabriel.galdino\Desktop\Project\automation'
file = 'black_list.csv'
complete_path = os.path.join(folder, file)

def is_valid_cpf(cpf):
    return len(cpf) == 11 and cpf.isdigit()

if not os.path.exists(complete_path):
    print(f'Arquivo não localizado, verifique se o modelo está disponível.')
else:
    try:
        with open(complete_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            linhas = list(reader)

        new_data = input('Informe o CPF do cliente: ')
        if not is_valid_cpf(new_data):
            print("CPF inválido. Tente novamente.")
            exit()

        for linha in linhas:
            linha['CPF'] = str(new_data)

        with open(complete_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=linhas[0].keys(), delimiter=';')
            writer.writeheader()
            writer.writerows(linhas)

        print(f'Documento atualizado com sucesso!')

    except Exception as e:
        print(f'Ocorreu um erro: {e}')


option = Options()
option.add_argument("--headless")
option.add_argument("--disable-gpu")
option.add_argument("--no-sandbox")
option.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=option)
wait = WebDriverWait(driver, 10)
try:
    url = os.getenv("TRADEAPP_URL")
    driver.get(url)

    campo_login = wait.until(EC.presence_of_element_located((By.NAME, "login")))
    campo_login.send_keys(os.getenv("TRADEAPP_USERNAME"))

    campo_senha = driver.find_element(By.NAME, 'password')
    campo_senha.send_keys(os.getenv("TRADEAPP_PASSWORD"))

    button_login = driver.find_element(By.CLASS_NAME, 'ladda-label')
    button_login.click()

    select_type = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="select2-selection__placeholder"]')))
    select_type.click()

    select_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[contains(@id, "BLACK-WHITE-LIST")]')))
    select_option.click()

    input_upload = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
    input_upload.send_keys(complete_path)

    button = driver.find_element(By.ID, "enviar-upload")
    button.click()

    button_confirm = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="confirm btn btn-lg btn-primary"]')))
    button_confirm.click()

    print('Parabéns, upload de arquivo realizado com sucesso!')

except Exception as e:
    print(f"Ocorreu um erro: {e}")

finally:
    driver.quit()
