from modelo.modelo import Person
import vistas.vistas as vistas
import constantes

def generarPago(data):
    separarNombreHoras = data.split('=')

    if len(separarNombreHoras) < 2:
        return vistas.presentarErrorEstructura()

    horarios = separarNombreHoras[1].split(",")
    nombre = separarNombreHoras[0]
    pago = obtenerPago(horarios)
    if pago == "Error":
        return vistas.presentarErrorEstructura()
    persona = Person()
    persona.nombre = nombre
    persona.pago = pago
    return vistas.presentarResultado(persona)

def obtenerPago(horarios):
    pago = 0
    for hora in horarios:
        dia = hora[0:2]
        separarHoras = hora[2:]
        dataHoras = separarHoras.split('-')

        if len(dataHoras) != 2:
            return "Error"

        if dataHoras[1] == '00:00':
            dataHoras[1] == '24:00'
        
        vistas.mostrarData(dia,dataHoras)
        horaInicio = dataHoras[0].split(":")
        horaFin = dataHoras[1].split(":")

        if (dia in constantes.SEMANA or dia in constantes.FIN_SEMANA):
            
            if (len(horaInicio) != 2 or len(horaFin) != 2):
                return "Error"

            if int(horaInicio[0]) > 24 or int(horaFin[0]) > 24:
                return "Error"
        
            if int(horaInicio[1]) > 59 or int(horaFin[1]) > 59:
                return "Error"
            
            valorHora = obtenerPagoHora(horaInicio, horaFin, dia)
            
            if valorHora == "Error":
                return "Error"
            
            pago = calcularPago(horaInicio, horaFin, valorHora) + pago
        else:
            return "Error"

        

    return pago

def calcularPago(inicio, fin, valor):
    if (int(inicio[0]) < 0) or (int(inicio[1]) < 0) or (int(fin[0]) < 0) or (int(fin[1]) < 0):
        return "Error"

    if (int(fin[1]) >= int(inicio[1])):    
        diffHoras = int(fin[0]) - int(inicio[0])
        pago = diffHoras * valor
        return pago

    if (int(inicio[1]) != int(fin[1])):
        diffHoras = int(fin[0]) - int(inicio[0]) -1
        pago = diffHoras * valor
        return pago

    

def obtenerPagoHora(horaInicio, horaFin, dia):
    
    if dia in constantes.SEMANA:
        
        if (int(horaInicio[0]) >= constantes.HORARIO_DIA[0]) and (int(horaFin[0]) <= constantes.HORARIO_DIA[2]):
            if (int(horaInicio[0]) == constantes.HORARIO_DIA[0]) and (int(horaInicio[1]) >= constantes.HORARIO_DIA[1]):
                if (int(horaFin[0]) == constantes.HORARIO_DIA[2]) and (int(horaFin[1]) == constantes.HORARIO_DIA[3]):
                    return 25
            return 25
        
        if (int(horaInicio[0]) >= constantes.HORARIO_TARDE[0]) and (int(horaFin[0]) <= constantes.HORARIO_TARDE[2]):
            if (int(horaInicio[0]) == constantes.HORARIO_TARDE[0]) and (int(horaInicio[1]) >= constantes.HORARIO_TARDE[1]):
                if (int(horaFin[0]) == constantes.HORARIO_TARDE[2]) and (int(horaFin[1]) == constantes.HORARIO_TARDE[3]):
                    return 15
            return 15

        if (int(horaInicio[0]) >= constantes.HORARIO_NOCHE[0]) and (int(horaFin[0]) <= constantes.HORARIO_NOCHE[2]):
            if (int(horaInicio[0]) == constantes.HORARIO_NOCHE[0]) and (int(horaInicio[1]) >= constantes.HORARIO_NOCHE[1]):
                if (int(horaFin[0]) == constantes.HORARIO_NOCHE[2]) and (int(horaFin[1]) == constantes.HORARIO_NOCHE[3]):
                    return 20
            return 20
        
    if dia in constantes.FIN_SEMANA:

        if (int(horaInicio[0]) >= constantes.HORARIO_DIA[0]) and (int(horaFin[0]) <= constantes.HORARIO_DIA[2]):
            if (int(horaInicio[0]) == constantes.HORARIO_DIA[0]) and (int(horaInicio[1]) >= constantes.HORARIO_DIA[1]):
                if (int(horaFin[0]) == constantes.HORARIO_DIA[2]) and (int(horaFin[1]) == constantes.HORARIO_DIA[3]):
                    return 30
            return 30

        if (int(horaInicio[0]) >= constantes.HORARIO_TARDE[0]) and (int(horaFin[0]) <= constantes.HORARIO_TARDE[2]):
            if (int(horaInicio[0]) == constantes.HORARIO_TARDE[0]) and (int(horaInicio[1]) >= constantes.HORARIO_TARDE[1]):
                if (int(horaFin[0]) == constantes.HORARIO_TARDE[2]) and (int(horaFin[1]) == constantes.HORARIO_TARDE[3]):
                    return 20
            return 20

        if (int(horaInicio[0]) >= constantes.HORARIO_NOCHE[0]) and (int(horaFin[0]) <= constantes.HORARIO_NOCHE[2]):
            if (int(horaInicio[0]) == constantes.HORARIO_NOCHE[0]) and (int(horaInicio[1]) >= constantes.HORARIO_NOCHE[1]):
                if (int(horaFin[0]) == constantes.HORARIO_NOCHE[2]) and (int(horaFin[1]) == constantes.HORARIO_NOCHE[3]):
                    return 25
            return 25
    else:
        return "Error"    