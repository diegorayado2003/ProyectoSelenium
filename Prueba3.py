from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Inicializar el navegador web (en este caso, Chrome)
driver = webdriver.Chrome()

# URL de la página web a probar
url = "https://www.walmart.com.mx/inicio" #https://ferjcabrera.github.io/TECH-ILA/
driver.get(url)

time.sleep(3)

def contar_mostrar_elementos_no_Interactuables():
    ##Imagenes= driver.find_elements(By.CSS_SELECTOR, "input[type='search']" or "input[type='text']")
    Imagenes = driver.find_elements(By.TAG_NAME, "img")

    print("Elementos no interactuables encontrados:")
    print(f"Imagenes: {len(Imagenes)}")
    for elemento in Imagenes:
        print(f"- Tipo: {elemento.tag_name},\n source: {elemento.get_attribute('src')} \n descripcion: {elemento.get_attribute('alt')}")
    


# Función para contar y mostrar todos los elementos
def contar_mostrar_elementos_Interactuables():
    barras_de_busqueda = driver.find_elements(By.CSS_SELECTOR, "input[type='search']" or "input[type='text']")
    botones = driver.find_elements(By.TAG_NAME, "button")
    inputs = driver.find_elements(By.TAG_NAME, "input")
    selectores = driver.find_elements(By.TAG_NAME, "select")
    hyperlinks = driver.find_elements(By.TAG_NAME, "a")
    

    print("Elementos interactuables encontrados:")
    print(f"Barras de búsqueda: {len(barras_de_busqueda)}")
    for elemento in barras_de_busqueda:
        print(f"- Tipo: {elemento.tag_name}, Valor: {elemento.get_attribute('value')}, PlacheHolder: {elemento.get_attribute('placeholder')}")

    print(f"Botones: {len(botones)}")
    for boton in botones:
        print(f"- Tipo: {boton.tag_name}, Texto: {boton.text}")

    print(f"Inputs: {len(inputs)}")
    for input in inputs:
        print(f"- Tipo: {input.tag_name}, Texto: {input.text} PlacheHolder: {input.get_attribute('placeholder')}")

    print(f"Hyperlinks: {len(hyperlinks)}")
    for hyperlink in hyperlinks:
        print(f"- Tipo: {hyperlink.tag_name}, Texto> {hyperlink.text}")

    print(f"Selectores: {len(selectores)}")
    for selector in selectores:
        print(f"- Tipo: {selector.tag_name}")
        opciones = selector.find_elements(By.TAG_NAME, "option")
        for opcion in opciones:
            print(f"  - Opción: {opcion.text}")

    if not barras_de_busqueda:
        print("No se encontraron barras de búsqueda.")
    if not botones:
        print("No se encontraron botones.")
    if not inputs:
        print("No se encontraron inputs.")
    if not hyperlinks:
        print("No se encontraron hyperlinks")
    if not selectores:
        print("No se encontraron selectores.")

# Ejecutar la función para contar y mostrar elementos
contar_mostrar_elementos_no_Interactuables()
contar_mostrar_elementos_Interactuables()

time.sleep(30)

# Cerrar el navegador al finalizar
driver.quit()