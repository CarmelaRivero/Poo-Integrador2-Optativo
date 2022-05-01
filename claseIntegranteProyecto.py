class IntegranteProyecto:
    #Atributos
    __idProyecto = ''
    __apellidNombre = ''
    __dni = ''
    __catInvestigacion = ''
    __rol = ''

    #Metodos
    def __init__(self,id='',apNom = '', dni = '', cat='',rol = ''):
        self.__idProyecto = id
        self.__apellidNombre = apNom
        self.__dni = dni
        self.__catInvestigacion = cat
        self.__rol = rol

    def getId(self):
        return self.__idProyecto
    def getCategoria(self):
        return self.__catInvestigacion
    def getRol(self):
        return self.__rol
