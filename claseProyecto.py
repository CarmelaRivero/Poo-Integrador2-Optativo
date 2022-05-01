class Proyecto:
    #Atributos
    __idProyecto = ''
    __titulo = ''
    __palabrasClave = ''
    __puntaje = 0

    def __init__(self,id='',tit='',palabras='',punt=0):
        self.__idProyecto = id
        self.__titulo = tit
        self.__palabrasClave = palabras
        self.__puntaje = punt

    def getId(self):
        return self.__idProyecto
    def setPuntaje(self,puntos):
        self.__puntaje = puntos
    def getPuntaje(self):
        return self.__puntaje
    def getTitulo(self):
        return self.__titulo
    def getPClave(self):
        return self.__palabrasClave

    def __gt__(self,otro):
        if type(otro) == Proyecto:
            punt1 = self.__puntaje
            punt2 = otro.getPuntaje()
            return punt1 > punt2
        else:
            print('Se deben comprar objetos de tipo Proyecto')
            return None
