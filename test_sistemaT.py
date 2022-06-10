from sistemaT import sistemaT

def test_1():
    sistema = sistemaT()

    sistema.crear_programa("fibonacci","LOCAL")
    assert sistema.ejecutar_programa("fibonacci") == True # True

    sistema.crear_programa("factorial", "java")
    assert sistema.ejecutar_programa("factorial") == False # False

    sistema.crear_inteprete("C","java")

    sistema.crear_traductor("java","C","C")

    assert sistema.ejecutar_programa("factorial") == False # False

    sistema.crear_inteprete("LOCAL","C")

    assert sistema.ejecutar_programa("factorial") == True # True

    sistema.crear_programa("HolaMundo","Python3")

    sistema.crear_traductor("Python3","wtf42","LOCAL")

    assert sistema.ejecutar_programa("HolaMundo") == False # False

    sistema.crear_traductor("wtf42","C","java")

    assert sistema.ejecutar_programa("HolaMundo") == True # True

test_1()