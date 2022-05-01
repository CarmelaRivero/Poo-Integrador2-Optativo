import re
from claseIntegranteProyecto import IntegranteProyecto

class ManejadorIntegrantesProyecto:
    #Atributos
    __lista = [] #Lista de integrantes

    def __init__(self):
        self.__lista = []

    def addIntegrante(self,id,nomAp,dni,cat,rol):
        error = False
        #Valido ingreso de datos (todos de tipo string)
        if type(id)==str and type(nomAp)==str and type(dni)==str and type(cat)==str and type(rol)==str:
            #id con formato 22X123 (dos digitos - letra - tres digitios)
            if re.search(r'[\d]{2}[A-Z]{1}[\d]{3}',id) == None:
                error = True
                print('Error: id de proyecto con formato incorrecto.')
            #Nombre y apellido sin numeros o simbolos
            if re.search(r'[\d\_\-\.+*]',nomAp) != None:
                print('Error: El nombre y apellido debe contener solo letras')
                error = True
            #DNI solo con digitos numericos
            if dni.isdigit() == False:
                print('Error: El dni solo debe contener digitos numericos')
                error = True
            #Categorias validas I, II, III, IV, V
            if cat != 'I' and cat != 'II' and cat != 'III' and cat != 'IV' and cat != 'V':
                print('Error: La categoria puede ser I, II, III, IV o V')
                error = True
            #Roles admitidos Director, Codirector, Integrante
            if rol.lower() != 'director' and rol.lower() != 'codirector' and rol.lower() != 'integrante':
                print('Error: Los roles admitidos son director, codirector e integrante')
                error = True
            #Si no hay error agrego integrante a la lista
            if error == False:
                integrante = IntegranteProyecto(id,nomAp,dni,cat,rol)
                self.__lista.append(integrante)
        else:
            print('Error: El proyecto no se puede agregar a la lista.')

    #Un proyecto debe tener como mínimo 3 (tres) integrantes
    #(10 puntos si cumple, -20 si no cumple).
    #Mensaje ‘El Proyecto debe tener como mínimo 3 integrantes’.
    def integrantesMin(self,id):
        cant = 0
        for integrante in self.__lista:
            idInt = integrante.getId()
            if id == idInt:
                cant += 1
        if cant >= 3:
            puntaje = 10
        else:
            puntaje = -20
            print('El Proyecto {} debe tener como minimo 3 integrantes'.format(id))
        return puntaje

    #Un proyecto debe tener  un Director con categoría I o II
    #(10 puntos si cumple, -5 si no cumple).
    #Mensaje ‘El Director del Proyecto debe tener categoría I o II.
    def directorMin(self,id):
        tiene = False
        i = 0
        while tiene == False and i < len(self.__lista):
            idInt = self.__lista[i].getId()
            if id == idInt:
                categoria = self.__lista[i].getCategoria()
                rol = self.__lista[i].getRol()
                if (rol == 'director') and (categoria == 'I' or categoria =='II'):
                    tiene = True
            i +=1
        if tiene:
            puntaje = 10
        else:
            print('El Director del Proyecto {} debe tener categoria I o II'.format(id))
            puntaje = -5
        return puntaje

    #Un proyecto debe tener un codirector con categoría I, II o III
    #(10 puntos si cumple, -5 si no cumple).
    #Mensaje ‘El Codirector del Proyecto debe tener como mínimo categoría III’.
    def codirectorMin(self,id):
        tiene = False
        i = 0
        while tiene == False and i < len(self.__lista):
            idInt = self.__lista[i].getId()
            if id == idInt:
                categoria = self.__lista[i].getCategoria()
                rol = self.__lista[i].getRol()
                if (rol == 'codirector') and (categoria == 'I' or categoria =='II' or categoria == 'III'):
                    tiene = True
            i +=1
        if tiene:
            puntaje = 10
        else:
            print('El Codirector del Proyecto {} debe tener como minimo categoria III'.format(id))
            puntaje = -5
        return puntaje

    #Un Proyecto debe tener una persona con rol de  Director.
    #Mensaje ‘El Proyecto debe tener un Director’
    def tieneDirector(self,id):
        tiene = False
        i = 0
        while tiene == False and i < len(self.__lista):
            idInt = self.__lista[i].getId()
            if id == idInt:
                rol = self.__lista[i].getRol()
                if (rol == 'director'):
                    tiene = True
            i +=1
        puntaje = 0
        if tiene == False:
            print('El Proyecto {} debe tener un Director'.format(id))
            puntaje = -10
        return puntaje

    #Un proyecto debe tener una persona con el rol de Codirector.
    #Mensaje ‘El Proyecto debe tener un Codirector’.
    def tieneCodirector(self,id):
        tiene = False
        i = 0
        while tiene == False and i < len(self.__lista):
            idInt = self.__lista[i].getId()
            if id == idInt:
                rol = self.__lista[i].getRol()
                if (rol == 'codirector'):
                    tiene = True
            i +=1
        puntaje = 0
        if tiene == False:
            print('El Proyecto {} debe tener un Codirector'.format(id))
            puntaje = -10
        return puntaje
