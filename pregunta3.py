from buddySystem import buddySystem as bds
msg1 = """Bienvenido a la similacion del BuddySystem

Instrucciones disponibles:
    - RESERVAR <nombre> <cantidad>
    - LIBERAR <nombre>
    - MOSTRAR
    - SALIR

"""
def main():
    while True:
        try:
            n = int(input("Indique la cantidad de bloque a trabajar(La cantidad debe ser mayor a cero): "))
            print()
            sistema = bds(n)
            break
        except:
            print("Error al iniciar el sistema, vuelva a intentarlo")

    print(msg1)

    while True:
        
        instruccion = input("$>")
        instruccion =[i for i in instruccion.split(" ") if i != ""]

        if instruccion[0] == "RESERVAR":
            if len(instruccion) != 3:
                    print("Error con la longitud de la instruccion")
                    continue
            try:
                cantidad = int(instruccion[2])
            except:
                print("Error con la insturcion, vuelva a intentarlo")
                continue
            
            sistema.reservar_espacio(instruccion[1],cantidad)

        elif instruccion[0] == "LIBERAR":
            if len(instruccion) != 2:
                    print("Error con la longitud de la instruccion")
                    continue
            sistema.liberar_espacio(instruccion[1])
        elif instruccion[0] == "MOSTRAR":
            sistema.mostrar_espacios_libres()
        elif instruccion[0] == "SALIR":
            print("Hasta luego")
            break
        else:
            print("Instruccion no permitida.\n")
main()