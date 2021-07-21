def showAllView(data):
    print (data)

def startView():
    print ('CALCULADORA DE PAGOS\n')
    print ('Ingrese el nombre del archivo .txt a analizar')
    archivo = input()
    return archivo


def presentarResultado(persona):
    print ("El importe a pagar a "+persona.nombre+" es de "+str(persona.pago))
    print("\n")

def presetarErrorArchivo(mensaje):
    print('El archivo '+mensaje+' no existe')

def presentarErrorEstructura():
    print('El archivo no cumple con la estructura indicada')