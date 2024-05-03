from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time
from datetime import datetime

# Inicializar el navegador web (en este caso, Chrome)
driver = webdriver.Chrome()

# URL de la página web a probar
url = "https://ferjcabrera.github.io/TECH-ILA/" #https://ferjcabrera.github.io/TECH-ILA/
driver.get(url)

time.sleep(3)

# Crear o abrir el archivo CSV en modo de escritura
with open('objetos.csv', 'w', newline='') as archivo_csv:
    # Definir las columnas del CSV
    campos = ['id_prueba','nombre', 'tipo', 'fecha']
    # Crear el escritor CSV
    escritor_csv = csv.DictWriter(archivo_csv, fieldnames=campos)
    # Escribir la cabecera
    escritor_csv.writeheader()

    def obtener_fecha_hora():
        now = datetime.now()
        fecha_hora = now.strftime("%Y-%m-%d %H:%M:%S")
        return fecha_hora

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
            print(f"- Tipo: {elemento.tag_name}, Valor: {elemento.get_attribute('value')}, PlacheHolder: {elemento.get_attribute('placeholder')}")
            escritor_csv.writerow({'id_prueba': crear_id(),'nombre': elemento.get_attribute('value'), 'tipo': elemento.tag_name, 'fecha': obtener_fecha_hora()})
            #Ingresar dato en la barra de busqueda por placeholder, por si hay mas de una barra de busqueda
            if elemento.get_attribute('placeholder') == "Search...":
                elemento.send_keys("Hola")
                print("Se puso el dato correcto en la barra de busqueda")
            else:
                print("No se ecntontro la barra de busqueda con ese palceholder")


        print(f"\nBotones: {len(botones)}")
        boton_encontrado = False
        for boton in botones:
            print(f"- Tipo: {boton.tag_name}, Texto: {boton.text}")
            escritor_csv.writerow({'id_prueba': crear_id(),'nombre': boton.text, 'tipo': boton.tag_name})

            #Dar click al boton por medio del texto 
            if boton.text == "Login":
                boton_encontrado = True
                boton.click
        if not boton_encontrado:
            print("No se encontró un botón con el texto especificado.")

        


        print(f"\nInputs: {len(inputs)}")
        input_encontrado = False
        for input in inputs:            
                print(f"- Tipo: {input.tag_name}, Texto: {input.text} PlacheHolder: {input.get_attribute('placeholder')}")
                escritor_csv.writerow({'id_prueba': crear_id(),'nombre': input.get_attribute('placeholder'), 'tipo': input.tag_name})
                #Poner Balor en algun input dependiendo de el text
                if input.text == "Cualquier Cosa":
                    input_encontrado = True
                    input.send_keys("Cualquier Cosa")
                print("Se enecontraron los inputs en otros objetos como la barra de busqueda")
        if not input_encontrado:
            print("No se econtro el Input especificado")



        print(f"\nHyperlinks Totales: {len(hyperlinks)}")
        hyperlink_encontrado = False
        for hyperlink in hyperlinks:
            if hyperlink.text != "":
                print(f"- Tipo: {hyperlink.tag_name}, Texto: {hyperlink.text}")
                escritor_csv.writerow({'id_prueba': crear_id(),'nombre': hyperlink.text, 'tipo': hyperlink.tag_name})
                if hyperlink.text =="Home":
                    hyperlink_encontrado = True
                    hyperlink.click
        if not hyperlink_encontrado:
            print("No se econtro el Hyperlink especificado")
    

        print(f"\nSelectores: {len(selectores)}")
        for selector in selectores:
            print(f"- Tipo: {selector.tag_name}")
            escritor_csv.writerow({'id_prueba': crear_id(),'nombre': '', 'tipo': selector.tag_name})

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
    contar_mostrar_elementos_Interactuables()


    print("\nSE CREO UN REPORTE DE TODOS LOS OBJETOS CORRECTAMENTE")





time.sleep(10)

# Cerrar el navegador al finalizar
driver.quit()