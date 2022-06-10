from genericpath import exists


class sistemaT:
    def __init__(self) -> None:
        self.lenguajes_ejecutables = ["LOCAL"]
        self.traductores = []
        self.programas = {}
        self.interpretadores = []
    
    def crear_programa(self, nombre:str, lenguaje:str):
        if nombre in self.programas.keys(): 
            print("Ya existe el programa") 
            return
        
        self.programas[nombre] = lenguaje
    
    def crear_inteprete(self, lenguaje_base:str, lenguaje_objetivo: str):
        self.interpretadores.append((lenguaje_base,lenguaje_objetivo))
        self.determinar_lenguajes_ejecutables()
    
    def crear_traductor(self, lenguaje_origen: str, lenguaje_base: str, lenguaje_destino: str):
        self.traductores.append((lenguaje_origen,lenguaje_base,lenguaje_destino))
        self.determinar_nuevos_traductores()

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
    
    def determinar_nuevos_traductores(self):
        cont = 0
        while True and cont < 10:
            seguir = False
            saltar = False
            for i in self.traductores:             
                if i[1] not in self.lenguajes_ejecutables: 
                    for j in self.traductores:
                        if j[0] == i[0] and j[1] in self.lenguajes_ejecutables and j[2] == i[2]:
                            """ 
                            print("existe un traductor en un lenguaje que conozco")
                            print(i,j)
                            input()
                            """
                            saltar = True 
                            break
                    
                    if saltar: continue

                    for j in self.traductores:
                        if j[0] == i[1] and j[1] in self.lenguajes_ejecutables and j[2] in self.lenguajes_ejecutables:
                            self.traductores.append((i[0],j[2],i[2]))
                            """ 
                            print("Creo un nuevo traductor:")
                            print(i,j)
                            input()
                            """
                            seguir = True
            cont += 1
            if seguir == False: break
    
    def ejecutar_programa(self,nombre):
        if self.programas[nombre] in self.lenguajes_ejecutables: return True

        for tra in self.traductores:
            if tra[0] == self.programas[nombre] and tra[1] in self.lenguajes_ejecutables and tra[2] in self.lenguajes_ejecutables:
                return True
        
        return False

        

