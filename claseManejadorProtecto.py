import re
from claseProyecto import Proyecto

class ManejadorProyecto:
    #Atributos
    __lista = []

    #Metodos
    def __init__(self):
        self.__lista = []

    def addProyecto(self,id,tit,pClave):
        #Valido ingreso de datos (todos de tipos string)
        if type(id) == str and type(tit) == str and type(pClave) == str:
            #id con formato 22X123 (dos digitos - letra - tres digitios)
            if re.search(r'[\d]{2}[A-Z]{1}[\d]{3}',id) != None:
                proyecto = Proyecto(id,tit,pClave)
                self.__lista.append(proyecto)
            else:
                print('Error: id de proyecto con formato incorrecto.')
        else:
            print('Error: El proyecto no se puede agregar a la lista.')

    def getIds(self):
        ids = []
        for proyecto in self.__lista:
            ids.append(proyecto.getId())
        return ids

    def setPuntajes(self,puntajes):
        for i in range(len(puntajes)):
            self.__lista[i].setPuntaje(puntajes[i])

    #Lista los datos de los proyectos ordenado por puntaje
    def rankin(self):
        self.__lista.sort(reverse = True) #Ordeno de mayor a menor puntaje
        print('{:9}{:70}{:40}{:8}'.format('ID','Titulo','Palabras Clave','Puntaje'))
        for proyecto in self.__lista:
            id = proyecto.getId()
            titulo = proyecto.getTitulo()
            pClave = proyecto.getPClave()
            Puntaje = proyecto.getPuntaje()
            print('{:8}{:70}{:40}{:3}'.format(id,titulo,pClave,Puntaje))
