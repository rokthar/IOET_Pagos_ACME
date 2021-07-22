class Person(object):

    def __init__(self, nombre = None, pago = None):
        self.nombre = nombre
        self.pago = pago

    @classmethod
    def getAll(self, archivo):
        try:
            database = open(archivo+'.txt', 'r')
            mensaje = database.readlines()
            return mensaje
        except:
            mensaje = "Error"
            return mensaje