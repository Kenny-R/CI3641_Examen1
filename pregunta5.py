from sistemaT import sistemaT
def main():
    sistema = sistemaT()
    print("""
    Bienvenido a la simulacion SistemaT.

    Instruciones Disponibles:
        - DEFINIR <tipo> [<argumentos>]
        - EJECUTABLE <nombre>
        - SALIR
    
    Tipos disponibles:
    - PROGRAMA <nombre> <lenguaje>
        Representa un programa identificado por <nombre> y escrito en <lenguaje>
    - INTERPRETE <lenguaje_base> <lenguaje>
        Representa a un interprete para <lenguaje> escrito en <lenguaje_base>
    - TRADUCTOR <lenguaje_origen> <lenguaje_base> <lenguaje_destino>
        Representa a un traductor, desde <lenguaje_origen> hacia <lenguaje_destino> escrito en <lenguaje_base>
    """)
    while True:
        instruccion = input('$>')

        instruccion =[i for i in instruccion.split(" ") if i != ""] 

        if instruccion[0] == "DEFINIR":
            if len(instruccion) < 2:
                print("Error con la longitud de la instruccion")
                continue 
            
            if instruccion[1] == "PROGRAMA":
                if len(instruccion) != 4:
                    print("Error con la longitud de la instruccion")
                    continue
                
                if instruccion[1] in sistema.programas.keys():
                    print("El programa ya existe")
                else:
                    sistema.crear_programa(instruccion[2],instruccion[3])
                    print(f"Se definio el programa '{instruccion[2]}', ejecutable en '{instruccion[3]}'")
            
            elif instruccion[1] == "INTERPRETE":
                if len(instruccion) != 4:
                    print("Error con la longitud de la instruccion")
                    continue
                
                sistema.crear_inteprete(instruccion[2],instruccion[3])
                print(f"Se definio un interprete para '{instruccion[3]}', escrito en '{instruccion[2]}'")

            
            elif instruccion[1] == "TRADUCTOR":
                if len(instruccion) != 5:
                    print("Error con la longitud de la instruccion")
                    continue
                
                sistema.crear_traductor(instruccion[2],instruccion[3],instruccion[4])
                print(f"Se definio un traductor de '{instruccion[2]}' hacia '{instruccion[4]}', escrito en '{instruccion[3]}'")
            
            else:
                print("Tipo no disponible\n")
                print("Tipos disponibles:\n- PROGRAMA <nombre> <lenguaje>\n- INTERPRETE <lenguaje_base> <lenguaje>\n- TRADUCTOR <lenguaje_origen> <lenguaje_base> <lenguaje_destino>") 
        elif instruccion[0] == "EJECUTABLE": 
            if len(instruccion) != 2:
                print("Error con la longitud de la instruccion")
                continue
            
            if instruccion[1] not in sistema.programas.keys():
                print("No existe el programa.")
                continue

            if sistema.ejecutar_programa(instruccion[1]):
                print(f"Si, es posible ejecutar el programa '{instruccion[1]}'")
            else:
                print(f"No es posible ejecutar el programa '{instruccion[1]}'")

        elif instruccion[0] == "SALIR":
            print("Hasta luego.")
            break
        else:
            print("Instruccion no permitida.\n")
            print("Instruciones Disponibles:\n- DEFINIR <tipo> [<argumentos>]\n- EJECUTABLE <nombre>\n- SALIR")

main()