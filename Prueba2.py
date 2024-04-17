from selenium import webdriver
from selenium.webdriver.common.by import By

# Inicializar el navegador web (en este caso, Chrome)
driver = webdriver.Chrome()

# URL de la página web a probar
url = "http://localhost:8080"
driver.get(url)

# Función para encontrar y mostrar todos los elementos
def mostrar_elementos():
    print("Barras de búsqueda:")
    barras_de_busqueda = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
    for elemento in barras_de_busqueda:
        print(f"Tipo: {elemento.tag_name}, Texto: {elemento.get_attribute('value')}")

    print("\nBotones:")
    botones = driver.find_elements(By.TAG_NAME, "input")
    for boton in botones:
        print(f"Tipo: {boton.tag_name}, Texto: {boton.text}")

    print("\nSelectores:")
    selectores = driver.find_elements(By.TAG_NAME, "select")
    for selector in selectores:
        print(f"Tipo: {selector.tag_name}")
        opciones = selector.find_elements(By.TAG_NAME, "option")
        for opcion in opciones:
            print(f"- Opción: {opcion.text}")

    if not barras_de_busqueda:
        print("No se encontraron barras de búsqueda.")
    if not botones:
        print("No se encontraron botones.")
    if not selectores:
        print("No se encontraron selectores.")

# Ejecutar la función para mostrar elementos
mostrar_elementos()

# Cerrar el navegador al finalizar
driver.quit()
