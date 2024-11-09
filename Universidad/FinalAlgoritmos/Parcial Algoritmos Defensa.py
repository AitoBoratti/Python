"""
Una empresa de servicio de internet tiene una central de reclamos para la asistencia técnica a los clientes.
Los tipos de asistencia son: remoto, instalación y presencial.
Se tiene una grilla de trabajo que se confecciona con información proveniente de la central de reclamos, hay una capacidad máxima de 1000 reclamos.
La información es toda numérica: cliente, asistencia (1:remoto, 2:instalacion o 3:presencial), horario de asistencia: ejemplo 1200, 1500, 915, etc. y teléfono.
Los técnicos son 15 y se le van asignando las tareas en la medida que se vaya atendiendo,
y finaliza la jornada cuando no haya más reclamos que atender o llego al máximo (1000).
Los técnicos tienen una planilla de trabajo donde asientan los siguientes detalles: cliente, #técnico, tipo de asistencia y soluciono (si=1 o No=2)
Al final de la jornada de asistencia se reporta al jefe de soporte al cliente la siguiente información:
Cantidad de asistencia de cada tipo
Porcentaje de asistencias por cada técnico resueltas y no resueltas.
"""

from collections import namedtuple

Solicitud = namedtuple('Solicitud', ['cliente_id', 'servicio_tipo', 'hora', 'contacto'])
Asignacion = namedtuple('Asignacion', ['cliente_id', 'tecnico_id', 'servicio_tipo', 'resuelto'])

def crear_solicitudes(cantidad_solicitudes):
    lista_solicitudes = []
    tipo_servicio_actual = 1  
    hora_actual = 800    
    for n in range(1, cantidad_solicitudes + 1):
        cliente_id = n
        servicio_tipo = tipo_servicio_actual
        tipo_servicio_actual += 1
        if tipo_servicio_actual > 3:
            tipo_servicio_actual = 1  
        hora_actual += 15
        if hora_actual >= 1800:  
            hora_actual = 800
        contacto_cliente = "Cliente_" + str(cliente_id)
        lista_solicitudes.append(Solicitud(cliente_id, servicio_tipo, hora_actual, contacto_cliente))
    return lista_solicitudes

def asignar_solicitudes(solicitudes, cantidad_tecnicos):
    lista_asignaciones = []
    tecnico_actual = 1
    for solicitud in solicitudes:
        resuelto = 1 if solicitud.cliente_id % 2 == 0 else 2  
        lista_asignaciones.append(Asignacion(solicitud.cliente_id, tecnico_actual, solicitud.servicio_tipo, resuelto))
        tecnico_actual += 1
        if tecnico_actual > cantidad_tecnicos:
            tecnico_actual = 1 
    return lista_asignaciones

def generar_reporte(asignaciones, cantidad_tecnicos):
    contador_remoto = 0
    contador_instalacion = 0
    contador_presencial = 0
    resueltos_por_tecnico = [0] * cantidad_tecnicos
    no_resueltos_por_tecnico = [0] * cantidad_tecnicos

    for asignacion in asignaciones:
        if asignacion.servicio_tipo == 1:
            contador_remoto += 1
        elif asignacion.servicio_tipo == 2:
            contador_instalacion += 1
        elif asignacion.servicio_tipo == 3:
            contador_presencial += 1
        if asignacion.resuelto == 1:
            resueltos_por_tecnico[asignacion.tecnico_id - 1] += 1
        else:
            no_resueltos_por_tecnico[asignacion.tecnico_id - 1] += 1
            
    print("Cantidad de servicios por tipo:")
    print("Remoto:", contador_remoto, "Instalación:", contador_instalacion, "Presencial:", contador_presencial)
    print("Tareas resueltas y no resueltas por técnico:")
    for i in range(cantidad_tecnicos):
        total_tareas = resueltos_por_tecnico[i] + no_resueltos_por_tecnico[i]
        if total_tareas > 0:
            porcentaje_resueltas = (resueltos_por_tecnico[i] / total_tareas) * 100
            porcentaje_no_resueltas = (no_resueltos_por_tecnico[i] / total_tareas) * 100
            print("Técnico", i + 1, ":", porcentaje_resueltas, "% resueltas,", porcentaje_no_resueltas, "% no resueltas")
        else:
            print("Técnico", i + 1, ": Sin tareas asignadas")

CANTIDAD_SOLICITUDES = 100
CANTIDAD_TECNICOS = 5

solicitudes = crear_solicitudes(CANTIDAD_SOLICITUDES)
asignaciones = asignar_solicitudes(solicitudes, CANTIDAD_TECNICOS)
generar_reporte(asignaciones, CANTIDAD_TECNICOS)