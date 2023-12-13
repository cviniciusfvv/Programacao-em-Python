from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

nav = webdriver.Chrome()
nav.get('https://professoroscarjr.000webhostapp.com/delivery/index.php')
time.sleep(1)

cadastrar = nav.find_element(By.XPATH, '/html/body/div[1]/form/div/input').click()
time.sleep(1)

nome = nav.find_element(By.ID, 'fnome')
nome.send_keys('PP')
time.sleep(1)

email = nav.find_element(By.ID, 'email_id')
email.send_keys('pp@gmail.com')
time.sleep(1)

senha1 = nav.find_element(By.NAME, 'pass')
senha1.send_keys('712156')
time.sleep(1)

senha2 = nav.find_element(By.NAME, 'pass2')
senha2.send_keys('712156')
time.sleep(1)

local = nav.find_element(By.ID, 'country')
local.send_keys('USA')
time.sleep(1)

bcadastrar = nav.find_element(By.XPATH, '/html/body/div[1]/form/input[5]').click()
time.sleep(1)

user = nav.find_element(By.ID, 'email')
user.send_keys('PP')
senha = nav.find_element(By.ID, 'senha_id')
senha.send_keys('712156')
time.sleep(1)
senha = nav.find_element(By.NAME, 'entrar').click()

time.sleep(10)

