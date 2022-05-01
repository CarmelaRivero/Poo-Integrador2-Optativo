import csv
import os
from claseManejadorIntegrantesProyecto import ManejadorIntegrantesProyecto
from claseManejadorProyecto import ManejadorProyecto

def test():
    #Test de ingreso de proyectos
    print('#---Test de ingreso de proyectos---#')
    manejadorTest = ManejadorProyecto()
    proyecto = ['FG3425','titulo proyecto','palabras']
    print('ID con formato incorrecto: ', end = '')
    print(proyecto)
    manejadorTest.addProyecto(proyecto[0],proyecto[1],proyecto[2])
    proyecto = ['23F678','Titulo','Palabras']
    print('Proyecto con datos correctos: ', end = '')
    print(proyecto)
    manejadorTest.addProyecto(proyecto[0],proyecto[1],proyecto[2])
    input('Test finalizado, presion ENTER para continuar...')

    #Test de ingreso de integrantes
    print('#---Test de ingreso de integrantes---#')
    manejadorTest = ManejadorIntegrantesProyecto()
    integrante = ['FG3425','Gomez Juan23 Carlos','321FG23543','F','subdirector']
    print('Integrante con todos los datos incorrectos: ', end = '')
    print(integrante)
    manejadorTest.addIntegrante(integrante[0],integrante[1],integrante[2],integrante[3],integrante[4])
    integrante = ['34P235','Gomez Juan Carlos','32123543','I','director']
    print('Integrante con datos correctos: ', end = '')
    print(integrante)
    manejadorTest.addIntegrante(integrante[0],integrante[1],integrante[2],integrante[3],integrante[4])
    input('Test finalizado, presion ENTER para continuar...')
    os.system('cls')

if __name__ == '__main__':
    integrantes = ManejadorIntegrantesProyecto()
    proyectos = ManejadorProyecto()

    #Funcion test
    op = input('Desea ejecutar la funcion test? [S]i - [N]o: ')
    if op.lower() == 's':
        test()

    #Carga de proyectos
    archivo = open('proyectos.csv')
    reader = csv.reader(archivo,delimiter=';')
    bandera = True
    for fila in reader:
        if bandera:
            bandera = False
        else:
            proyectos.addProyecto(fila[0],fila[1],fila[2])
    archivo.close()

    #Carga de integrantes
    archivo = open('integrantesProyecto.csv')
    reader = csv.reader(archivo,delimiter=';')
    bandera = True
    for fila in reader:
        if bandera:
            bandera = False
        else:
            integrantes.addIntegrante(fila[0],fila[1],fila[2],fila[3],fila[4])
    archivo.close()

    #Calculo de los puntos por proyecto
    ids = proyectos.getIds()
    puntajes = []

    for id in ids:
        #Un proyecto debe tener como minimo 3 integrantes
        puntaje = integrantes.integrantesMin(id)

        #Un proyecto debe tener  un Director con categoría I o II
        puntaje += integrantes.directorMin(id)

        #Un proyecto debe tener un codirector con categoría I, II o III
        puntaje += integrantes.codirectorMin(id)

        #Un Proyecto debe tener una persona con rol de  Director.
        puntaje += integrantes.tieneDirector(id)

        # Un proyecto debe tener una persona con el rol de Codirector
        puntaje += integrantes.tieneCodirector(id)

        puntajes.append(puntaje)

    #Asigno puntajes a los proyectos
    proyectos.setPuntajes(puntajes)
    proyectos.rankin() #Listar los datos de los proyectos
