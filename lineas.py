database = open('Juan.txt', 'r')
mensaje = database.readlines()
for linea in mensaje:   
    lineas = linea.replace(" ", "")
    # data = lineas.replace("\n","")
    print (lineas)