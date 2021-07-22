import controlador.controlador as controlador
from modelo.modelo import Person
import vistas.vistas as vista

def start():
    archivo = vista.iniciarSistema()
    return mostrarInformacion(archivo)

def mostrarInformacion(archivo):
    data = Person.obtenerInformacion(archivo)
    if data == "Error":
        return vista.presetarErrorArchivo(archivo)
    
    for lineas in data: 
        linea = lineas.replace(" ","")
        controlador.generarPago(linea)
        
if __name__ == "__main__":
    start()