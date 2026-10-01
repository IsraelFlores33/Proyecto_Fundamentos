#No estoy muy seguro de como se asigna el porcentaje de becas en el tec así que usaremos un random
import random

#Cual es el tipo de beca que se desea consultar
def p_tipo_beca():
    print ("Estas son las becas que hay")
    print ("Academica 1, Deportiva 2, Socioeconómica 3, Lideres del mañana 4")
    opcion_beca = int(input("¿Cúal es la beca a la que te estas postulando?"))
    
#Opcion tipo beca = o_t_p
    if opcion_beca == 1:
        o_t_b = "Academica"
    elif opcion_beca == 2:
        o_t_b = "Deportiva"
    elif opcion_beca == 3:
        o_t_b = "Socioeconómica"
    elif opcion_beca == 4:
        o_t_b = "Lideres del mañana"
    else:
        o_t_b = "Opción no valida"
        
    return o_t_b

#Aqui se evaluara si la solicitud entra o no
def evaluar_solicitud(tipo_beca,promedio,semestre):
    
    if tipo_beca == "Academica":
        if promedio >= 85:
            beca = random.randint(10,40)
            print ("tu beca esta aprobada y tienes ", beca, " % de beca")
        else:
            print ("Solicitud de beca rechazada no cumples con el promedio minimo")
            
    elif tipo_beca == "Deportiva":
        if promedio >= 80:
            beca = random.randint(10,30)
            print ("tu beca esta aprobada y tienes ", beca, " % de beca")
        else:
            print ("Solicitud de beca rechazada no cumples con el promedio minimo")
        
    elif tipo_beca == "Socioeconómica":
        if promedio >= 90:
            beca = random.randint(10,60)
            print ("tu beca esta aprobada y tienes ", beca, " % de beca")
        else:
            print ("Solicitud de beca rechazada no cumples con el promedio minimo")
    
#Aqui tampoco estoy seguro de los limites de semestre en los que se puede solicitar la beca lideres del mañana
#asi que puse el valor intermedio de 4to senestre

    elif tipo_beca == "Lideres del mañana":
        if promedio >= 95 and semestre <= 4:
            beca = 100
            print ("tu beca esta aprobada y tienes ", beca, " %de beca")
        else:
            print ("Solicitud de beca rechazada no cumples con el promedio minimo o ya estas muy avanzado en los semestres")
        
    else:
        print ("Tipo de beca no reconocida")
        

#Aqui se guarda la información de las becas
def informacion(tipo_beca):
    
    if tipo_beca == "Academica":
        print ("Para esta beca necesitas un promedio minimo de 85 y podras tener hasta 40% de beca")
    elif tipo_beca == "Deportiva":
        print ("Para esta beca necesitas un promedio minimo de 80 y podras tener hasta 30% de beca")
    elif tipo_beca == "Socioeconómica":
        print ("Para esta beca necesitas un promedio minimo de 90 y podras tener hasta 60% de beca")
    elif tipo_beca == "Lideres del mañana":
        print ("Para esta beca necesitas un promedio minimo de 95 y tendras 100% de beca")
    else:
        print ("Beca no reconocida")





#Menu del programa
while True:
    print (" ████ ███  ████ █████ █████ █   █  ███     ████  █████    ████  █████  ███   ███   ████    ███ █████ █████  ████ █   █ ")
    print ("█      █  █       █   █     ██ ██ █   █    █   █ █        █   █ █     █     █   █ █         █    █   █     █     ██ ██ ")
    print (" ███   █   ███    █   ████  █ █ █ █████    █   █ ████     ████  ████  █     █████  ███      █    █   ████   ███  █ █ █ ")
    print ("    █  █      █   █   █     █   █ █   █    █   █ █        █   █ █     █     █   █     █     █    █   █         █ █   █ ")
    print ("████  ███ ████    █   █████ █   █ █   █    ████  █████    ████  █████  ███  █   █ ████     ███   █   █████ ████  █   █ ")
    print ("Tipos de Becas: 1")
    print ("Solicitud de Becas: 2")
    print ("Salir: 3")
#Definimos lo que quiere hacer el usuario    
    opcion_menu = int(input("Selecciona una opción (1,2,3): "))
    
    if opcion_menu == 1:
        tipo_beca = p_tipo_beca()
        info = informacion(tipo_beca)
        
    elif opcion_menu == 2:
        tipo_beca = p_tipo_beca()
        semestre = int(input("¿Cúal es tu semestre?"))
        promedio = float(input("¿Cúal es tu promedio?"))
        estado = evaluar_solicitud(tipo_beca,promedio,semestre)
        
    elif opcion_menu == 3:
        print ("Gracias por utilizar el sistema de becas ITESM")
        print ("Vuelva pronto")
        break
    else:
        print ("Ese es un valor no valido")
        
        
    
    