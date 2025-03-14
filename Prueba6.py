from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
import time
from datetime import datetime
import psycopg2 

# Inicializar el navegador web (en este caso, Chrome)
driver = webdriver.Chrome()

# URL de la página web a probar
url = "https://www.mercadolibre.com.mx" #https://ferjcabrera.github.io/TECH-ILA/ #https://www.heb.com.mx
driver.get(url)

# para iniciar conexcion con bd
conn = psycopg2.connect(host ="localhost", dbname="selenium_prueba", user= "postgres", 
                        password ="", port = "5432")

cur = conn.cursor()

time.sleep(7)

# Crear o abrir el archivo CSV en modo de escritura
with open('objetos.csv', 'w', newline='') as archivo_csv:

    # Definir las columnas del CSV
    campos = ['id_prueba','nombre', 'tipo', 'fecha']
    # Crear el escritor CSV
    escritor_csv = csv.DictWriter(archivo_csv, fieldnames=campos)
    # Escribir la cabecera
    escritor_csv.writeheader()

    #Funcion para obtener la fecha y la hora
    def obtener_fecha_hora():
        now = datetime.now()
        fecha_hora = now.strftime("%Y-%m-%d %H:%M:%S")
        return fecha_hora

    #Funcion para obtener crear el id de los objetos
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

            print(f"- Tipo: {elemento.tag_name}, Valor: {elemento.get_attribute('value')}, PlacheHolder: {elemento.get_attribute('placeholder')}")
            escritor_csv.writerow({'id_prueba': crear_id(),'nombre': elemento.get_attribute('placeholder'), 'tipo': elemento.tag_name})
            #añadir objeto a base de datos
            comando_insertar = "INSERT INTO objetos(nombre, tipo, pruebaid) VALUES ( " + " '"  + nombre + "' " + ", '" + tipo + "' , '" + id_prueba + "')"
            #print(comando_insertar)
            cur.execute(comando_insertar)
            #Ingresar dato en la barra de busqueda por placeholder, por si hay mas de una barra de busqueda
            #if elemento.get_attribute('placeholder') == "Search...":
            #    elemento.send_keys("Hola")
            #    print("Se puso el dato correcto en la barra de busqueda")
            #else:
            #   print("No se ecntontro la barra de busqueda con ese palceholder")


        print(f"\nBotones: {len(botones)}")
        #boton_encontrado = False
        for boton in botones:

            tipo = boton.tag_name
            nombre = boton.text
            id_prueba = crear_id()
            
            print(f"- Tipo: {boton.tag_name}, Texto: {boton.text}")
            escritor_csv.writerow({'id_prueba': crear_id(),'nombre': boton.text, 'tipo': boton.tag_name})
            comando_insertar = "INSERT INTO objetos(nombre, tipo, pruebaid) VALUES ( " + " '"  + nombre + "' " + ", '" + tipo + "' , '" + id_prueba + "')"
            cur.execute(comando_insertar)

            #Dar click al boton por medio del texto 
            #if boton.text == "Login":
                ## boton.click
        #if not boton_encontrado:
           # print("No se encontró un botón con el texto especificado.")

        
        print(f"\nInputs: {len(inputs)}")
        input_encontrado = False
        for input in inputs:    

            tipo = input.tag_name
            nombre = input.get_attribute('placeholder')
            id_prueba = crear_id()

            print(f"- Tipo: {input.tag_name}, Texto: {input.text} PlacheHolder: {input.get_attribute('placeholder')}")
            escritor_csv.writerow({'id_prueba': crear_id(),'nombre': input.get_attribute('placeholder'), 'tipo': input.tag_name})
            comando_insertar = "INSERT INTO objetos(nombre, tipo, pruebaid) VALUES ( " + " '"  + nombre + "' " + ", '" + tipo + "' , '" + id_prueba + "')"
            cur.execute(comando_insertar)

            #Poner Balor en algun input dependiendo de el text
            #if input.text == "Cualquier Cosa":
            #    input_encontrado = True
            #    input.send_keys("Cualquier Cosa")
          #  print("Se enecontraron los inputs en otros objetos como la barra de busqueda")
       # if not input_encontrado:
           # print("No se econtro el Input especificado")

        print(f"\nHyperlinks Totales: {len(hyperlinks)}")
        hyperlink_encontrado = False
        for hyperlink in hyperlinks:

            tipo = hyperlink.tag_name
            nombre = hyperlink.text
            href = hyperlink.get_attribute("href")
            id_prueba = crear_id()

            
            print(f"- Tipo: {hyperlink.tag_name}, Texto: {hyperlink.text}, Href: {href}")
            escritor_csv.writerow({'id_prueba': crear_id(),'nombre': hyperlink.text, 'tipo': hyperlink.tag_name})
            comando_insertar = "INSERT INTO objetos(nombre, tipo, pruebaid) VALUES ( " + " '"  + nombre + "' " + ", '" + tipo + "' , '" + id_prueba + "')"
            cur.execute(comando_insertar)

             #   if hyperlink.text =="Home":
             #       hyperlink_encontrado = True
             #       hyperlink.click
       # if not hyperlink_encontrado:
          #  print("No se econtro el Hyperlink especificado")
    
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

        return barras_de_busqueda, botones, inputs, selectores, hyperlinks
    
    

    def crear_prueba():
        print("Se esta ejecutando la prueba")
        for elemento in barras_de_busqueda or inputs:
            if elemento.get_attribute('placeholder') == "Buscar productos, marcas y más…":
                elemento.send_keys("lamaparas")
                elemento.send_keys(Keys.RETURN)
                print("Se puso el dato correcto en la barra de busqueda")

                
            else:
               print("No se ecntontro la barra de busqueda con ese palceholder")

        time.sleep(10)
       
        for hyperlink in hyperlinks:
            hyperlink_encontrado = False
            if hyperlink.text == "Lámpara Tactica Linterna Potente Con Martillo Emergencia Color de la linterna Blanco Color de la luz Negro":
                hyperlink_encontrado = True
                hyperlink.click
                print("Se dio click correctamente")
            if not hyperlink_encontrado:
                print("No se econtro el Hyperlink especificado")
        
        time.sleep(10)
        
    time.sleep(10)
    
      

    
    # Ejecutar la función para contar y mostrar elementos
    barras_de_busqueda, botones, inputs, selectores, hyperlinks = contar_mostrar_elementos_Interactuables()
    crear_prueba()

    
    


    print("\nSE CREO UN REPORTE DE TODOS LOS OBJETOS CORRECTAMENTE")

# aplicar cambios y cerrar conexion con bd
conn.commit()
cur.close()
conn.close()
print("Se mando todo a la base de datos")

time.sleep(5)

# Cerrar el navegador al finalizar
driver.quit()