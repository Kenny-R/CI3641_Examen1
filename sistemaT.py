
"""
Clase que implementa una simulacion de un sistema T
utilizado para comprender el funcionamiento de los 
compiladores.
"""
class sistemaT:
    def __init__(self) -> None:
        self.lenguajes_ejecutables = ["LOCAL"]
        self.traductores = []
        self.programas = {}
        self.interpretadores = []
    
    """
    Permite almacenar una representacion de un programa
    como un par programa-lenguaje

    Parametros:
        nombre: El nombre del programa.
        lenguaje: Lenguaje en el cual esta escrito el programa

    """
    def crear_programa(self, nombre:str, lenguaje:str):
        if nombre in self.programas.keys(): 
            print("Ya existe el programa") 
            return
        
        self.programas[nombre] = lenguaje
    

    """
    Permite almacenar una representacion de un interpretador 
    que permite ejecutar programas escritos en el lenguaje
    objetivo usando el lenguaje base

    Parametros:
        lenguaje_base: Lenguaje el cual se utiliza para 
                       ejecutar programas escritos en el 
                       lenguaje objetivo
        
        lenguaje_objetivo: Lenguaje el cual se quiere 
                           ejecutar
    """
    def crear_inteprete(self, lenguaje_base:str, lenguaje_objetivo: str):
        self.interpretadores.append((lenguaje_base,lenguaje_objetivo))
        self.determinar_lenguajes_ejecutables()
    
    """
    Permite almacenar una representacion de un traductor que 
    permite traducir un programa en el lenguaje de origen hasta
    el lenguaje objetivo usando el lenguaje base

    Parametros:
        lenguaje_origen: Lenguaje original del programa que se quiere
                         traducir
 
        lenguaje_base: Lenguaje que se utilizara para la traduccion
 
        lenguaje_objetivo: Lenguaje al cual se quiere traducir el programa 
    """
    def crear_traductor(self, lenguaje_origen: str, lenguaje_base: str, lenguaje_destino: str):
        self.traductores.append((lenguaje_origen,lenguaje_base,lenguaje_destino))
        self.determinar_nuevos_traductores()

    """
    Permite determinar que lenguajes puede ejecutar la maquina, esto 
    se logra recorriendo la lista de interpretes y verificando si 
    se puede usar con los lenguajes actuales, y si se cumple esta condicion
    se eliminar el interpretador y se añade este lenguaje a la lista de 
    lenguajes ejecutables
    """
    def determinar_lenguajes_ejecutables(self):
        while True:
            seguir = False
            interpretadores_a_eliminar = []
            for i in self.interpretadores:
                if i[1] in self.lenguajes_ejecutables:
                    interpretadores_a_eliminar.append(i)
                    continue
                
                if i[0] in self.lenguajes_ejecutables and i[1] not in self.lenguajes_ejecutables:
                    self.lenguajes_ejecutables.append(i[1])
                    interpretadores_a_eliminar.append(i)
                    seguir = True
            
            for a in interpretadores_a_eliminar:
                self.interpretadores.remove(a)
            
            if seguir == False: break
    
    """
    Permite crear nuevos traductores usando los que ya hay en la lista
    y los lengujaes que se pueden ejecutar en la maquina
    """
    def determinar_nuevos_traductores(self):
        while True:
            seguir = False
            saltar = False
            for i in self.traductores:             
                if i[1] not in self.lenguajes_ejecutables: 
                    for j in self.traductores:
                        if j[0] == i[0] and j[1] in self.lenguajes_ejecutables and j[2] == i[2]:
                            saltar = True 
                            break
                    
                    if saltar: continue

                    for j in self.traductores:
                        if j[0] == i[1] and j[1] in self.lenguajes_ejecutables and j[2] in self.lenguajes_ejecutables:
                            self.traductores.append((i[0],j[2],i[2]))
                            seguir = True
            if seguir == False: break
    
    
    """
    Comprueba si se puede ejecutar el programa directamente usando 
    algun lenguaje de los que puede ejecutar la maquina o usando un
    traductor

    parametro:
        nombre: Nombre del programa a comprobar.
    """
    def ejecutar_programa(self,nombre):
        if self.programas[nombre] in self.lenguajes_ejecutables: return True

        for tra in self.traductores:
            if tra[0] == self.programas[nombre] and tra[1] in self.lenguajes_ejecutables and tra[2] in self.lenguajes_ejecutables:
                return True
        
        return False

        

