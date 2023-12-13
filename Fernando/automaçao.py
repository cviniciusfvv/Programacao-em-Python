from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#nav = webdriver.Chrome(executable_path=r' C:/User/oscar.junior/Documents)
nav= webdriver.Chrome()
nav.get('https//professoroscarjr.000webhostapp.com/delivery/index.php')
time.sleep(1)
user = nav.find_element (By.ID,'email')
user.send_keys ('oscar@gmail.com')
senha = nav.find_element(By.ID,'senha_id')
senha.send_keys('1234')
time.sleep(1)
nav.find_element(By.Name,'entrar').click()

time.sleep(10)