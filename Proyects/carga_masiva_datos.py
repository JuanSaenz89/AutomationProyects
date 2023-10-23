from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome("webdriver//chromedriver.exe") # Ingresar ruta de web driver
driver.get('') # Ruta del formulario
df = pd.read_csv('db.csv', encoding= 'latin-1') # Ruta del CSV



for row, datos in df.iterrows():
    index = datos['ID']
    nombre = datos['Nombre']
    paterno = datos['ApePaterno']
    # Cargar las columnas de el csv
    driver.find_element('xpath','ruta_del_xpath').send_keys(index)
    driver.find_element('xpath','ruta_del_xpath').send_keys(nombre)
    driver.find_element('xpath','ruta_del_xpath').send_keys(paterno)
