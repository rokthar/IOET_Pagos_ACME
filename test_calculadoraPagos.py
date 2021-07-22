import controlador.controlador as controlador

def test_calcularPagoCorrecto():
    assert controlador.obtenerPago(['MO10:00-12:00', 'TU10:00-12:00', 'TH01:00-03:00', 'SA14:00-18:00', 'SU20:00-21:00']) == 215

def test_calcularPago_Minutos():
    assert controlador.obtenerPago(['MO10:00-12:00', 'TU10:00-12:00', 'TH01:00-03:00', 'SA14:00-18:00', 'SU20:10-21:10']) == 215

def test_calcularPago_DiferenciaMinutos_MayorInicio():
    assert controlador.obtenerPago(['MO10:00-12:00', 'TU10:00-12:00', 'TH01:00-03:00', 'SA14:00-18:00', 'SU20:10-21:00']) == 190

def test_calcularPago_DiferenciaMinutos_MayorFin():
    assert controlador.obtenerPago(['MO10:00-12:00', 'TU10:00-12:00', 'TH01:00-03:00', 'SA14:00-18:00', 'SU20:00-21:10']) == 215

def test_calcularPago_sinDia():
    assert controlador.obtenerPago(['10:00-12:00', '10:00-12:00', '01:00-03:00', '14:00-18:00', '20:00-21:00']) == "Error"

def test_calcular_diaIncorrecto():
    assert controlador.obtenerPago(['MO10:00-12:00', 'TU10:00-12:00', 'TH01:00-03:00', 'SA14:00-18:00', 'ST20:00-21:00']) == "Error"

def test_calcularPago_malSeparador():
    assert controlador.obtenerPago(['MO10:00|12:00', 'TU10:00|12:00', 'TH01:00|03:00', 'SA14:00|18:00', 'SU20:00|21:00']) == "Error"

def test_calcularPago_malFormatoHora():
    assert controlador.obtenerPago(['MO10.00-12:00', 'TU10:00-12:00', 'TH01:00-03:00', 'SA14:00-18:00', 'SU20:00-21:00']) == "Error"

def test_calcular_mas24Horas():
    assert controlador.obtenerPago(['MO10:00-12:00', 'TU10:00-12:00', 'TH01:00-03:00', 'SA14:00-18:00', 'SU20:00-25:00']) == "Error"

def test_calcular_horaNegativa():
    assert controlador.obtenerPago(['MO10:00-12:00', 'TU10:00-12:00', 'TH01:00-03:00', 'SA14:00-18:00', 'SU-20:00-21:00']) == "Error"

def test_diaCorrecto():
    assert controlador.obtenerPagoHora(["10","00"],["12","00"],"MO") == 15

def test_diaIncorrecto():
    assert controlador.obtenerPagoHora(["10","00"],["12","00"],"YU") == "Error"