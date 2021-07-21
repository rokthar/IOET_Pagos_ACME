class Person(object):

    def __init__(self, nombre = None, pago = None):
        self.nombre = nombre
        self.pago = pago

    @classmethod
    def getAll(self, archivo):
        try:
            database = open(archivo+'.txt', 'r')
            mensaje = database.read()
            return mensaje.replace(" ", "")
        except:
            mensaje = "Error"
            return mensaje