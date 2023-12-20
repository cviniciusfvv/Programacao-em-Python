from selenium import webdriver
from selenium.webdriver.common.by import By

while True:
    cd = int(input("Qual opção você quer: 1 - Yu Gi Oh, 2 - Magic, 3 - Pokemon TCG, 0 - sair: ")) #escolha seu card game
    if cd == 0:
        print("Saindo do programa. Até mais!")
        break  # Encerra o loop
    if cd == 1: #Yu Gi Oh
        while True:
            yugioh = int(input("O que você procura sobre Yu Gi Oh: 1 - Cartas, 2 - Booster, 3 - Cartas avulsas, 4 - decks 0 - sair:  "))
            if yugioh == 0:
                print("Saindo do programa. Até mais!")
                break  # Encerra o loop interno
            if yugioh == 1: # cartas
                driver = webdriver.Chrome()
                driver.get('https://www.ligayugioh.com.br/?view=cards/edicoes')
                result = driver.find_element(By.XPATH, '//*[@id="tab-edc"]/tbody \n').text
                print(result)
            if yugioh == 2: # Booster
                driver = webdriver.Chrome()
                driver.get('https://www.ligayugioh.com.br/?view=cards/edicoes')
                result = driver.find_element(By.XPATH, '//*[@id="tab-edc"]/tbody \n').text
                print(result)
            if yugioh == 3: # cartas avulsas
                driver = webdriver.Chrome()
                driver.get('https://www.ligayugioh.com.br/?view=cards/edicoes')
                result = driver.find_element(By.XPATH, '//*[@id="tab-edc"]/tbody \n').text
                print(result)
            if yugioh == 4: # decks
                driver = webdriver.Chrome()
                driver.get('https://www.ligayugioh.com.br/?view=dks/decks')
                result = driver.find_element(By.XPATH, '//*[@id="card-estoque"]/div[3] \n').text
                print(result)
            else:
                print("Opção não existe")
    if cd == 2: #Magic
        while True:
            magic = int(input("O que você procura sobre Magic: 1 - Cartas, 2 - Booster, 3 - Cartas avulsas, 4 - decks 0 - sair:  "))
            if magic == 0:
                print("Saindo do programa. Até mais!")
                break  # Encerra o loop interno
            if magic == 1: # packs
                driver = webdriver.Chrome()
                driver.get('https://www.ligamagic.com.br/?view=cards%2Fsearch&card=booster+pack&tipo=1')
                result = driver.find_element(By.XPATH, '//*[@id="mtg-cards"] \n').text
                print(result)
            if magic == 2: # Booster
                driver = webdriver.Chrome()
                driver.get('https://www.ligamagic.com.br/?view=cards%2Fsearch&card=booster+box&tipo=1')
                result = driver.find_element(By.XPATH, '//*[@id="mtg-cards"]/div[1] \n').text
                print(result)
            if magic == 3: # cartas avulsas
                driver = webdriver.Chrome()
                driver.get('https://www.ligamagic.com.br/?view=leilao/listar')
                result = driver.find_element(By.XPATH, '/html/body/main/div[4]/div \n').text
                print(result)
            if magic == 4: # decks
                driver = webdriver.Chrome()
                driver.get('https://www.ligamagic.com.br/?view=dks/decks')
                result = driver.find_element(By.XPATH, '//*[@id="dks-carrossels"] \n').text
                print(result)
            else:
                print("Opção não existe")
    if cd == 3: #Pokemon tcg
        while True:
            magic = int(input("O que você procura sobre Pokemon TCG: 1 - Cartas, 2 - Booster, 3 - Cartas avulsas, 4 - decks 0 - sair:  "))
            if magic == 0:
                print("Saindo do programa. Até mais!")
                break  # Encerra o loop interno
            if magic == 1: # packs
                driver = webdriver.Chrome()
                driver.get('https://www.ligapokemon.com.br/?view=cards/search&card=categ%3D21+searchprod%3D1')
                result = driver.find_element(By.XPATH, '//*[@id="mtg-cards"] \n').text
                print(result)
            if magic == 2: # Booster
                driver = webdriver.Chrome()
                driver.get('https://www.ligapokemon.com.br/?view=cards/search&card=categ%3D10+searchprod%3D1')
                result = driver.find_element(By.XPATH, '//*[@id="mtg-cards"] \n').text
                print(result)
            if magic == 3: # cartas avulsas
                driver = webdriver.Chrome()
                driver.get('https://www.ligapokemon.com.br/?view=cards/variacao&show=alta')
                result = driver.find_element(By.XPATH, '//*[@id="card-estoque"]/div[3] \n').text
                print(result)
            if magic == 4: # decks
                driver = webdriver.Chrome()
                driver.get('https://www.ligapokemon.com.br/?view=cards/search&card=categ%3D24+searchprod%3D1')
                result = driver.find_element(By.XPATH, '//*[@id="mtg-cards"] \n').text
                print(result)
            else:
                print("Opção não existe")
    else:
        print("Opção não existe")          