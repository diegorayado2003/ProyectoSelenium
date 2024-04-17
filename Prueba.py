from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Crear un objeto webdriver utilizando el navegador Chrome
driver = webdriver.Chrome()

# Obtener la página web
driver.get("https://www.walmart.com.mx")

# Esperar un tiempo para que se cargue completamente la página (en este caso, 10 segundos)
time.sleep(10)

# Intentar identificar y guardar elementos en la página
try:
    # Encontrar el campo de búsqueda utilizando diferentes selectores
    search_field = driver.find_element(By.CSS_SELECTOR, "input[type='search']")
    # Imprimir el texto del campo de búsqueda en la consola
    print("Barra de busqueda encontrada", search_field.get_attribute("placeholder"))

    # Encontrar el botón de búsqueda utilizando diferentes selectores
    search_button = driver.find_element(By.CSS_SELECTOR, "button[type='search']")
    # Imprimir el valor del botón de búsqueda en la consola
    print("Valor del botón de búsqueda:", search_button.text)

    # Encontrar el enlace de inicio de sesión utilizando diferentes selectores
    login_link = driver.find_element(By.CSS_SELECTOR, "a[href*='login']")
    # Imprimir el texto del enlace de inicio de sesión en la consola
    print("Texto del enlace de inicio de sesión:", login_link.text)

    # Encontrar otros elementos de interés utilizando diferentes selectores y métodos
    # ...

    # Solicitar al usuario que presione Enter para cerrar el navegador
    input("Presiona Enter para cerrar el navegador...")
except Exception as e:
    # Si ocurre algún error durante la identificación de elementos, imprimir el mensaje de error en la consola
    print("Error al identificar los elementos:", e)

# Cerrar el navegador después de que el usuario presione Enter
driver.quit()
