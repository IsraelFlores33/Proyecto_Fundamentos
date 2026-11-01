#random para los porcentajes
import random

# Lista de los tipos de becas, el promedio minimo y el porcentaje maximo
catalogo_becas = [
    ["Beca socioeconómica", 85, 60],
    ["Beca al Talento académico", 90, 70],
    ["Prestamo educativo", 80, 50],
    ["Beca al talento estudiantil", 85, 50],
    ["Beca al talento emprendedor", 85, 60],
    ["Beca al talento creativo", 85, 60],
    ["Beca al Talento transformador", 90, 80],
    ["Lideres del mañana", 95, 100]
]

historial_solicitudes = []

#Función para presentar la opción 1 con el catalogo de becas
def mostrar_catalogo_becas():
    print("\n CATÁLOGO DE BECAS")
    i = 1
    for beca in catalogo_becas:
        nombre = beca[0]
        promedio = beca[1]
        porcentaje = beca[2]
        print(i, ".", nombre, "- Promedio mínimo:", promedio, "- Máx:", porcentaje, "%")
        i = i + 1

#Función para mostrar las becas y seleccionar una de interes
def p_tipo_beca():
    mostrar_catalogo_becas()
    opcion = int(input("\nIngresa el número de la beca: "))
    indice = opcion - 1
    
    if 0 <= indice < len(catalogo_becas):
        return indice
    else:
        print("Número de opción no válido.")
        return None

#Evalua a los futuros alumnos y les da un valor al azar de la beca que eligio 
def evaluar_solicitud(indice_beca, promedio, semestre, nombre_aspirante):
    
    beca = catalogo_becas[indice_beca]
    nombre = beca[0]
    prom_min = beca[1]
    tope_beca = beca[2]
    
    if nombre == "Lideres del mañana":
        if promedio >= prom_min and semestre <= 4:
            print("\n¡FELICIDADES", nombre_aspirante,  "Estas aprobado a la beca Lideres mañana.")
            historial_solicitudes.append([nombre_aspirante, nombre, promedio, semestre, "100%"])
        else:
            print("\n No cumples con el promedio de 95 o estás en un semestre muy avanzado.")
    
    elif promedio >= prom_min:
        porcentaje = random.randint(10, tope_beca)
        print("\n¡FELICIDADES", nombre_aspirante, "! Solicitud aprobada para", nombre, "con", porcentaje, "%")
        historial_solicitudes.append([nombre_aspirante, nombre, promedio, semestre, str(porcentaje) + "%"])
    else:
        print("\n Tu promedio (", promedio, ") es menor al mínimo requerido (", prom_min, ").\n")

#Función para mostrar el historial de solicitudes, y dar un folio aleatorio al alumno
def mostrar_historial():
    
    if not historial_solicitudes:
        print("\nNo hay solicitudes registradas todavía.")
        return

    print("\n Historial de solicitudes")
    
    folios = list(range(5001, 5001 + len(historial_solicitudes)))
    random.shuffle(folios)
    
    contador = 0
    for sol in historial_solicitudes:
        alumno = sol[0]
        beca = sol[1]
        porcentaje = sol[4]
        
        print("Folio:", folios[contador], "| Alumno:", alumno, "| Beca:", beca, "| Asignado:", porcentaje)
        contador = contador + 1

def main():
    
    print (" ████ ███  ████ █████ █████ █   █  ███     ████  █████    ████  █████  ███   ███   ████    ███ █████ █████  ████ █   █ ")
    print ("█      █  █       █   █     ██ ██ █   █    █   █ █        █   █ █     █     █   █ █         █    █   █     █     ██ ██ ")
    print (" ███   █   ███    █   ████  █ █ █ █████    █   █ ████     ████  ████  █     █████  ███      █    █   ████   ███  █ █ █ ")
    print ("    █  █      █   █   █     █   █ █   █    █   █ █        █   █ █     █     █   █     █     █    █   █         █ █   █ ")
    print ("████  ███ ████    █   █████ █   █ █   █    ████  █████    ████  █████  ███  █   █ ████     ███   █   █████ ████  █   █ ")
    
    flag = True
    while flag:
        print("1. Consultar requisitos de becas")
        print("2. Registrar solicitud de beca")
        print("3. Ver historial de solicitudes")
        print("4. Salir")
    
        opcion = input("\nSelecciona una opción: ")
    
    
        match opcion:
            case "1":
                mostrar_catalogo_becas()
                
            case "2":
                nombre_usr = input("Nombre completo del aspirante: ")
                indice_beca = p_tipo_beca()
            
                if indice_beca is not None:
                    semestre = int(input("¿Cuál es tu semestre? "))
                    promedio = float(input("¿Cuál es tu promedio? "))
                    evaluar_solicitud(indice_beca, promedio, semestre, nombre_usr)
                
            case "3":
                mostrar_historial()
            
            case "4":
                print("\nGracias por usar el sistema de becas. ¡Hasta luego!")
                flag = False
            
            case _:
                print("\nOpción no válida. Ingresa un número del 1 al 4.")
                
                
main()
