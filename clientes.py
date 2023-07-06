import core
import os
def CreateData(*args):
    return core.LoadInfo("clientes.json")

def MainMenu():
    os.system("clear")
    isCliRun = True
    os.system("clear")
    print('+','-'*55,'+')
    print("|{:^50}{}{:^30}|".format(' ','ADMINISTRACION DE CLIENTES',' '))
    print('+','-'*55,'+')

    print("1. Crear cliente")
    print("2. Buscar cliente")
    print("3. Editar cliente")
    print("4. Regresar menu principal")
    opcion =int(input(":)_"))
    if (opcion == 1):
        pass
    elif (opcion == 2):
        pass
    elif (opcion == 3):
        pass
    elif (opcion == 4):
        isCliRun = False
    if (isCliRun):
        MainMenu()

    
