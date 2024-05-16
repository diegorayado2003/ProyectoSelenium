from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configura el driver de Selenium (asegúrate de tener el driver correspondiente a tu navegador instalado)
driver = webdriver.Chrome()  # Por ejemplo, para Chrome

# Abre la página de Walmart
driver.get("https://www.heb.com.mx")

# Encuentra todos los elementos <a> (hipervínculos) en la página
links = driver.find_elements(By.TAG_NAME,"a")

# Imprime los enlaces
for link in links:
    print(link.get_attribute("href"))



# Cierra el navegador
time.sleep(30)
driver.quit()
