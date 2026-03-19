def registrar_evento(historial):
    #Pedir al usuario los siguientes datos mediante consola:
    #• Tipo de evento: o Sospechoso/Confirmado
    #• porcentaje_afectado (0-100).
    #• Duración en días.
    #• Provincia.
    #• Cantón.
    #• Fecha (texto)
    #• epizootia_primates (s/n).
    #• viaje_zona_riesgo (s/n)
    # si => True 
    # no => False

    # Esto recoge los datos
    tipo = input("Tipo de evento: (Sospechoso / Confirmado) ")
    porcentaje_afectados = input("Porcentaje de afectados: (0 - 100) ")
    duracion = input("Duración en días: ")
    provincia = input("Provincia")
    canton = input("Canton")
    fecha = input("Fecha: (dd/mm/yy) ")
    epizootia_primates = input("Epizotia primates: (s/n)")
    viaje_zona_riesgo = input("Viaje zona riesgo: (s/n)") 
    
    # Validaciones
    if tipo == "Sospechoso" or tipo == "Confirmado":
        print(f"Tipo válido: {tipo}")
    else:
        print(f"El tipo: {tipo} no es válido.")
        return []

    try:
        porcentaje_afectados = int(porcentaje_afectados)
    except:
        print("El porcentaje no es un número válido")
        return []
    
    if porcentaje_afectados >= 0 and porcentaje_afectados <= 100:
        print(f"Porcentaje válido: {porcentaje_afectados}")
    else:
        print("Este porcentaje se sale del rango (0-100)")
        return []

    try:
        duracion = int(duracion)
    except:
        print("La duración no es un número entero")
        return []
    
    if duracion > 0:
        print("Duración válida")
    else:
        print("Duración inválida")
        return []
    
    
    if epizootia_primates == "s":
        epizootia_primates = True 
    elif epizootia_primates == "n":
        epizootia_primates = False
    else:
        print(f"{epizootia_primates} no es válido")
        return []


    if viaje_zona_riesgo == "s":
        viaje_zona_riesgo = True 
    elif viaje_zona_riesgo == "n":
        viaje_zona_riesgo = False
    else:
        print(f"{viaje_zona_riesgo} no es válido")
        return []

    # Evento tiene la siguiente forma:
    # evento = [fecha, provincia, canton, tipo_evento, porcentaje_afectado, duracion_dias, epizootia, viaje_zona_riesgo, impacto, recomendaciones]
    # El espacio para impacto y el espacio para recomendaciones 
    # están vacíos en un inicio.
    evento = [fecha, provincia, canton,
              tipo, porcentaje_afectados,
              duracion, epizootia_primates,
              viaje_zona_riesgo, "", []]
    
    # Tanto impacto como recomendaciones son strings
    impacto = evaluar_impacto(evento)
    evento[8] = impacto
    recomendaciones = generar_recomendaciones(evento)
    evento[9] = recomendaciones 
    return evento
    
def evaluar_impacto(evento):
    #Clasificar con los datos
    #registrados por el usuario el evento en
    #leve/moderado/crítico
    
    # Por ahora tenemos:
    # evento = [fecha, provincia, canton,
    #          tipo, porcentaje_afectados,
    #          duracion, epizootia_primates,
    #          viaje_zona_riesgo, "", ""]
    
    # Para eventos críticos (Debe cumplir cualquiera)
    # • porcentaje_afectado > 30 y duración_días > 5
    # • epizootia_primates = True y viaje_zona_riesgo = True
    # • tipo_evento = "Confirmado" y (porcentaje_afectado > 20 o duración_días > 3)
    
    porcentaje_afectados = evento[4]
    duracion = evento[5]
    epizootia_primates = evento[6]
    viaje_zona_riesgo = evento[7]
    tipo = [3]
    
    if porcentaje_afectados > 30 and duracion > 5:
        return "Crítico"

    elif epizootia_primates == True and viaje_zona_riesgo == True:
        return "Crítico"
    
    elif  tipo == "Confirmado" and (porcentaje_afectados > 20 or duracion > 3):
        return "Crítico"
    
    # Para eventos moderados (Si no es crítico y se cumple cualquiera) 
    # • porcentaje_afectado > 15 o duración_días > 2
    # • epizootia_primates = True o viaje_zona_riesgo = True
    
    # La condición "Si no es crítico" ya se cumple, puesto que 
    # si fuera crítico ya habría terminado la función
    if porcentaje_afectados > 15 or duracion > 2:
        return "Moderado"

    elif epizootia_primates == True or viaje_zona_riesgo == True:
        return "Moderado"

    # Para eventos leves
    # Cualquier otro caso
    return "Leve"

def generar_recomendaciones(evento):
    # Producir una lista de
    # acciones sugeridas (ver
    # sección 5). Mostrar al registrar
    # y al consultar un evento las
    # recomendaciones
    # generadas.
    #     5) Mapa de recomendaciones
    # Genere una lista (solo lista) según impacto:
    # Leve:
    # “Monitoreo comunitario”
    # “Educación preventiva contra mosquitos (Aedes/Haemagogus)”
    # Moderada:
    # “Tamizaje de viajeros y contactos”
    # “Búsqueda activa de epizootias en primates”
    # “Refuerzo de comunicación con Áreas de Salud”
    # Crítica:
    # “Alerta sanitaria local”
    # “Jornada intensiva de vacunación en cantón priorizado”
    # “Control de criaderos y acciones intersectoriales”
    # “Coordinación inmediata con vigilancia nacional” 
    impacto = evento[8]
    if impacto == "Leve":
        return ["Monitoreo comunitario", "Educación preventiva contra mosquitos (Aedes/Haemagogus)"] 
    
    elif impacto == "Moderado":
        return ["Tamizaje de viajeros y contactos",
                "Búsqueda activa de epizootias en primates",
                "Refuerzo de comunicación con Áreas de Salud"]
    elif impacto == "Crítico":
        return ["Alerta sanitaria local",
                "Jornada intensiva de vacunación en cantón priorizado",
                "Control de criaderos y acciones intersectoriales",
                "Coordinación inmediata con vigilancia nacional"]

def mostrar_historial(historial):
    # Listar eventos: fecha,
    # provincia/cantón, tipo,
    # impacto. Permitir ver detalle
    # por índice de la lista.
    # evento = [fecha, provincia, canton, tipo_evento, porcentaje_afectado, duracion_dias, epizootia, viaje_zona_riesgo, impacto, recomendaciones]

    # El indice es un indicador para el usuario
    indice = 0
    for evento in historial:
        print(f"======Indice: {indice}=======")
        print(f"Fecha: {evento[0]}")
        print(f"Provincia: {evento[1]} | Cantón: {evento[2]}")
        print(f"Tipo: {evento[3]}")
        print(f"Impacto: {evento[8]}")
        indice = indice + 1

    opcion = input(f"Elija un indice para ver detalles. (0 - {indice - 1}) (Presione cualquier otra tecla para salir): ")

    try:
        # Esta linea va a generar una excepcion cuando el usuario
        # presione otra tecla que no sea un numero
        opcion = int(opcion)

        # Para que el usuario no acceda a un índice que no existe
        if opcion >= 0 and opcion <= indice - 1:
            evento = historial[opcion]
            print("------ DETALLES ------")
            print(f"Fecha: {evento[0]}")
            print(f"Provincia: {evento[1]} | Cantón: {evento[2]}")
            print(f"Tipo: {evento[3]}")
            print(f"Porcentaje afectado: {evento[4]}%")
            print(f"Duración en días: {evento[5]}")
            print(f"Epizotia Primates: {evento[6]}")
            print(f"Viaje zona de Riesgo: {evento[7]}")
            print(f"Impacto: {evento[8]}")
            recomendaciones = evento[9]
            print("Recomendaciones:")
            for recomendacion in recomendaciones:
                print(f"- {recomendacion}")
        else:
            print("Número fuera de rango.")
            return
    
    except:
        return



def reporte_global(historial):
    # Mostrar conteo por
    # tipo_evento y por impacto
    # usando únicamente listas (sin
    # count() ni dict).
    # evento = [fecha, provincia, canton, tipo_evento, porcentaje_afectado, duracion_dias, epizootia, viaje_zona_riesgo, impacto, recomendaciones]
    
    # contadores = [criticos, moderados, leves,
    #                sospechosos, confirmados]
    # Valores iniciales
    contadores = [0, 0, 0, 0, 0]
    
    for evento in historial:
        tipo_evento = evento[3]
        impacto = evento[8]
        
        if tipo_evento == "Sospechoso":
            contadores[3] = contadores[3] + 1
        elif tipo_evento == "Confirmado":
            contadores[4] = contadores[4] + 1
        
        if impacto == "Crítico":
            contadores[0] = contadores[0] + 1 
        elif impacto == "Moderado":
            contadores[1] = contadores[1] + 1 
        elif impacto == "Leve":
            contadores[2] = contadores[2] + 1 

    criticos = contadores[0]
    moderados = contadores[1]
    leves = contadores[2]
    sospechosos = contadores[3]
    confirmados = contadores[4]
    
    print("REPORTE GLOBAL")
    print("Por impacto: ")
    print(f"Casos leves: {leves}")
    print(f"Casos moderados: {moderados}")
    print(f"Casos críticos: {criticos}")

    print("Por tipo: ")
    print(f"Casos sospechosos: {sospechosos}")
    print(f"Casos confirmados: {confirmados}")

def menu_principal():
    # Mostrar opciones:
    # 1) Registrar evento,
    # 2) Consultar historial,
    # 3) Generar reporte global,
    # 4) Salir. Mantenerse en bucle hasta elegir 4.


    # evento = [fecha, provincia, canton, tipo_evento, porcentaje_afectado, duracion_dias, epizootia, viaje_zona_riesgo, impacto, recomendaciones]
    # fecha = evento[0] 
    # duracion_dias = evento[5]
    
    # Guarda todos los eventos
    # historial = [
    #     [fecha, provincia, ..., recomendaciones]
    # ]
    historial = []

    while True: 
        print("1. Registrar evento")
        print("2. Consultar historial")
        print("3. Reporte global")
        print("4. Salir")
        
        # LEER opcion 
        opcion = input("Elección: ")
        
        if opcion == "1":
            evento = registrar_evento(historial)
            if evento == []:
                print("Error con evento")
            else:
                historial.append(evento)

        elif opcion == "2":
            mostrar_historial(historial)
        elif opcion == "3":
            reporte_global(historial)
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Elección inválida.")

menu_principal()
