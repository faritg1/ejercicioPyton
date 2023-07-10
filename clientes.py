import core
import os
diccCliente = {"data":[]}
"""
Metodo para cargar informacion de clientes:
Si el archivo de recursos no existe lo crea de forma
automatica con la estructura inicia del diccionario vacio
diccCliente = {"data":[]}
"""
def LoadInfoCliente():
    global diccCliente
    if (core.checkFile("clientes.json")):
        diccCliente = core.LoadInfo("clientes.json")
    else:
        core.crearInfo("clientes.json",diccCliente)

def MainMenu():
    os.system("clear")
    isCliRun = True
    if(core.checkFile("clientes.json")):
        diccCliente = core.LoadInfo("clientes.json")
    os.system("clear")
    print('+','-'*55,'+')
    print("|{:^16}{}{:^15}|".format(' ','ADMINISTRACION DE CLIENTES',' '))
    print('+','-'*55,'+')
    print("1. Registrar")
    print("2. Buscar cliente")
    print("3. Editar cliente")
    print("4. Eliminar cliente")
    print("5. Regresar menu principal")
    opcion =int(input(": "))
    if (opcion == 1):
        data ={
            "id":input("Ingrese el Id del cliente :"),
            "nombre":input("Ingrese el Nombre del cliente :"),
            "email":input("Ingrese el Email del cliente :"),
        }
        
        core.crearInfo("clientes.json",data)
        
    elif (opcion == 2):
        os.system("clear")
        print('+','-'*49,'+')
        print("|{:^16}{}{:^15}|".format(' ','BUSCADOR DE CLIENTES',' '))
        print('+','-'*49,'+')
        cliSearch = input("Ingrese el codigo del cliente a buscar: ")
        for i,item in enumerate(diccCliente["data"]):
            if cliSearch == item["id"]:
                print(f'Id cliente : {item["id"]}')
                print(f'Nombre cliente : {item["nombre"].upper()}')
                print(f'Email cliente : {item["email"]}')
                input("")

    elif (opcion == 3):
        os.system("clear")
        print('+','-'*49,'+')
        print("|{:^16}{}{:^15}|".format(' ','EDICION DE CLIENTES',' '))
        print('+','-'*49,'+')
        cliSearch = input("Ingrese el codigo del cliente a editar:")
        for i,item in enumerate(diccCliente["data"]):
            if cliSearch in item["id"]:
                item["nombre"] = input("Ingrese en nuevo nombre o presione enter para omitir :") or item["nombre"]
                item["email"] = input("Ingrese en nuevo email o presione enter para omitir :") or item["email"]
                core.EditarData("clientes.json",diccCliente)
                
    elif (opcion == 4):
        os.system("clear")
        print('+','-'*49,'+')
        print("|{:^16}{}{:^15}|".format(' ','ELIMINACION DE CLIENTES',' '))
        print('+','-'*49,'+')
        cliSearch = input("Ingrese el codigo del cliente a eliminar:")
        for i,item in enumerate(diccCliente["data"]):
            if cliSearch == item["id"]:
                itemDel = diccCliente["data"].pop(i)
                core.EditarData("clientes.json",diccCliente)
                # os.system("pause")
                # core.crearInfo("clientes.json",itemDel)

    elif (opcion == 5):
        isCliRun = False
    if (isCliRun):
        MainMenu()

    
