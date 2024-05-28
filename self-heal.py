from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
import time
from datetime import datetime
import psycopg2
from fuzzywuzzy import fuzz

# Inicializar el navegador web (en este caso, Chrome)
driver = webdriver.Firefox()

# URL de la página web a probar
url = "https://ferjcabrera.github.io/TECH-ILA/"
driver.get(url)

# para iniciar conexión con bd
conn = psycopg2.connect(host="localhost", dbname="selenium_prueba", user="postgres", 
                        password="", port="5432")

cur = conn.cursor()

time.sleep(3)

# Crear o abrir el archivo CSV en modo de escritura
with open('objetos.csv', 'w', newline='') as archivo_csv:

    # Definir las columnas del CSV
    campos = ['id_prueba', 'nombre', 'tipo', 'fecha']
    # Crear el escritor CSV
    escritor_csv = csv.DictWriter(archivo_csv, fieldnames=campos)
    # Escribir la cabecera
    escritor_csv.writeheader()

    # Función para obtener la fecha y la hora
    def obtener_fecha_hora():
        now = datetime.now()
        fecha_hora = now.strftime("%Y-%m-%d %H:%M:%S")
        return fecha_hora

    # Función para crear el id de los objetos
    def crear_id():
        now = datetime.now()
        fecha_hora_sin_espacios = now.strftime("P%H:%M:")
        id = fecha_hora_sin_espacios.replace('-', '').replace(':', '').replace(' ', '')
        return id

    # Función para contar y mostrar todos los elementos
    def contar_mostrar_elementos_Interactuables():
        barras_de_busqueda = driver.find_elements(By.CSS_SELECTOR, "input[type='search']" or "input[type='text']")
        botones = driver.find_elements(By.TAG_NAME, "button")
        inputs = driver.find_elements(By.TAG_NAME, "input")
        selectores = driver.find_elements(By.TAG_NAME, "select")
        hyperlinks = driver.find_elements(By.TAG_NAME, "a")

        print("Elementos interactuables encontrados:")
        print(f"\nBarras de búsqueda: {len(barras_de_busqueda)}")
        for elemento in barras_de_busqueda:
            tipo = elemento.tag_name
            nombre = elemento.get_attribute('placeholder')
            id_prueba = crear_id()
            print(f"- Tipo: {elemento.tag_name}, Valor: {elemento.get_attribute('value')}, Placeholder: {elemento.get_attribute('placeholder')}")
            escritor_csv.writerow({'id_prueba': crear_id(), 'nombre': elemento.get_attribute('placeholder'), 'tipo': elemento.tag_name})
            comando_insertar = f"INSERT INTO objetos(nombre, tipo, pruebaid) VALUES ('{nombre}', '{tipo}', '{id_prueba}')"
            cur.execute(comando_insertar)

        print(f"\nBotones: {len(botones)}")
        for boton in botones:
            tipo = boton.tag_name
            nombre = boton.text
            id_prueba = crear_id()
            print(f"- Tipo: {boton.tag_name}, Texto: {boton.text}")
            escritor_csv.writerow({'id_prueba': crear_id(), 'nombre': boton.text, 'tipo': boton.tag_name})
            comando_insertar = f"INSERT INTO objetos(nombre, tipo, pruebaid) VALUES ('{nombre}', '{tipo}', '{id_prueba}')"
            cur.execute(comando_insertar)

        print(f"\nInputs: {len(inputs)}")
        for input in inputs:
            tipo = input.tag_name
            nombre = input.get_attribute('placeholder')
            id_prueba = crear_id()
            print(f"- Tipo: {input.tag_name}, Texto: {input.text}, Placeholder: {input.get_attribute('placeholder')}")
            escritor_csv.writerow({'id_prueba': crear_id(), 'nombre': input.get_attribute('placeholder'), 'tipo': input.tag_name})
            comando_insertar = f"INSERT INTO objetos(nombre, tipo, pruebaid) VALUES ('{nombre}', '{tipo}', '{id_prueba}')"
            cur.execute(comando_insertar)

        print(f"\nHyperlinks Totales: {len(hyperlinks)}")
        for hyperlink in hyperlinks:
            tipo = hyperlink.tag_name
            nombre = hyperlink.text
            id_prueba = crear_id()
            if hyperlink.text != "":
                print(f"- Tipo: {hyperlink.tag_name}, Texto: {hyperlink.text}")
                escritor_csv.writerow({'id_prueba': crear_id(), 'nombre': hyperlink.text, 'tipo': hyperlink.tag_name})
                comando_insertar = f"INSERT INTO objetos(nombre, tipo, pruebaid) VALUES ('{nombre}', '{tipo}', '{id_prueba}')"
                cur.execute(comando_insertar)

        print(f"\nSelectores: {len(selectores)}")
        for selector in selectores:
            print(f"- Tipo: {selector.tag_name}")
            escritor_csv.writerow({'id_prueba': crear_id(), 'nombre': '', 'tipo': selector.tag_name})
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
            print("No se encontraron hyperlinks.")
        if not selectores:
            print("No se encontraron selectores.")

        return barras_de_busqueda, botones, inputs, selectores, hyperlinks

    barras_de_busqueda, botones, inputs, selectores, hyperlinks = contar_mostrar_elementos_Interactuables()

    def crear_prueba():
        print("Se está ejecutando la prueba")
        expected_placeholder = "Searchbar"
        for elemento in barras_de_busqueda:
            found_placeholder = elemento.get_attribute('placeholder')
            similarity = fuzz.partial_ratio(found_placeholder, expected_placeholder)
            if similarity > 60:  # threshold for similarity
                user_input = input(f"Placeholder similar found: '{found_placeholder}' (expected: '{expected_placeholder}'). Do you want to proceed? (yes/no): ")
                if user_input.lower() == "yes":
                    elemento.send_keys("Hola")
                    elemento.send_keys(Keys.RETURN)
                    print(f"Se puso el dato correcto en la barra de búsqueda con placeholder '{found_placeholder}'")
                else:
                    print(f"El usuario decidió no continuar con el placeholder '{found_placeholder}' (expected: '{expected_placeholder}')")
            else:
                print(f"Placeholder '{found_placeholder}' no es suficientemente similar a '{expected_placeholder}'")

    crear_prueba()


    print("\nSE CREO UN REPORTE DE TODOS LOS OBJETOS CORRECTAMENTE")

# aplicar cambios y cerrar conexión con bd
conn.commit()
cur.close()
conn.close()
print("Se mandó todo a la base de datos")

time.sleep(8)

# Cerrar el navegador al finalizar
driver.quit()
