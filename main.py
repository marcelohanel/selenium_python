from selenium import webdriver
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome()
navegador.get("https://ri.magazineluiza.com.br/")
navegador.find_element(By.XPATH, '//*[@id="Form1"]/header/div/div/div/div[2]/ul/li[3]/a').click()
navegador.find_element(By.XPATH, '//*[@id="Form1"]/div[12]/div/div/div/div/ul[3]/li[2]/a').click()
navegador.find_element(By.XPATH, '//*[@id="jG0yVjiX2kOm1P0ZMgEFyw=="]').click()
