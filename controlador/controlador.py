from modelo.modelo import Person
import vistas.vistas as vistas

def showAll(archivo):
    data = Person.getAll(archivo)
    if data == "Error":
        return vistas.presetarErrorArchivo(archivo)

    vistas.showAllView(data)
    generarPago(data)

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
    print(horarios)
    pago = 0
    for hora in horarios:
        dia = hora[0:2]
        separarHoras = hora[2:]
        dataHoras = separarHoras.split('-')

        if len(dataHoras) != 2:
            return "Error"

        if dataHoras[1] == '00:00':
            dataHoras[1] == '24:00'
        
        horaInicio = dataHoras[0].split(":")
        horaFin = dataHoras[1].split(":")

        if (len(horaInicio) != 2 or len(horaFin) != 2):
            return "Error"

        if (dia != "MO") and (dia != "TU") and (dia != "WE") and (dia != "TH") and (dia != "FR") and (dia != "SA") and (dia != "SU"):  
            return "Error"

        if int(horaInicio[0]) > 24 or int(horaFin[0]) > 24:
            return "Error"

        valorHora = obtenerPagoHora(horaInicio, horaFin, dia)
        if valorHora == "Error":
            return "Error"

        pago = calcularPago(horaInicio, horaFin, valorHora) + pago
    return pago

def calcularPago(inicio, fin, valor):
    if (int(inicio[0]) < 0) or (int(inicio[1]) < 0) or (int(fin[0]) < 0) or (int(fin[1]) < 0):
        return "Error"

    diffHoras = int(fin[0]) - int(inicio[0])
    pago = diffHoras * valor
    return pago

def obtenerPagoHora(horaInicio, horaFin, dia):
    
    if (dia == "MO") or (dia == "TU") or (dia == "WE") or (dia == "TH") or (dia == "FR"):
        
        if (int(horaInicio[0]) >= 0) and (int(horaFin[0]) <= 9):
            if (int(horaInicio[0]) == 0) and (int(horaInicio[1]) >= 1):
                if (int(horaFin[0]) == 9) and (int(horaFin[1]) == 0):
                    return 25
            return 25
        
        if (int(horaInicio[0]) >= 9) and (int(horaFin[0]) <= 18):
            if (int(horaInicio[0]) == 9) and (int(horaInicio[1]) >= 1):
                if (int(horaFin[0]) == 18) and (int(horaFin[1]) == 0):
                    return 15
            return 15

        if (int(horaInicio[0]) >= 18) and (int(horaFin[0]) <= 24):
            if (int(horaInicio[0]) == 18) and (int(horaInicio[1]) >= 1):
                if (int(horaFin[0]) == 24) and (int(horaFin[1]) == 0):
                    return 20
            return 20
        
    if (dia == "SA") or (dia == "SU"):

        if (int(horaInicio[0]) >= 0) and (int(horaFin[0]) <= 9):
            if (int(horaInicio[0]) == 0) and (int(horaInicio[1]) >= 1):
                if (int(horaFin[0]) == 9) and (int(horaFin[1]) == 0):
                    return 30
            return 30

        if (int(horaInicio[0]) >= 9) and (int(horaFin[0]) <= 18):
            if (int(horaInicio[0]) == 9) and (int(horaInicio[1]) >= 1):
                if (int(horaFin[0]) == 18) and (int(horaFin[1]) == 0):
                    return 20
            return 20

        if (int(horaInicio[0]) >= 18) and (int(horaFin[0]) <= 24):
            if (int(horaInicio[0]) == 18) and (int(horaInicio[1]) >= 1):
                if (int(horaFin[0]) == 24) and (int(horaFin[1]) == 0):
                    return 25
            return 25
    else:
        return "Error"    

def start():
    archivo = vistas.startView()
    return showAll(archivo)


