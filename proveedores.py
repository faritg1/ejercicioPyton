import core
import os

diccProveedor = {"data":[]}

def loadInfoProveedor():
    global diccProveedor
    if (core.checkFile("proveedor.json")):
        diccProveedor = core.LoadInfo("proveedor.json")
    else: 
        core.crearInfo("proveedor.json",diccProveedor)

def MainMenu():
    os.system("clear")
    isProveeRun = True
    os.system("clear")
    print('+','-'*55,'+')
    print("|{:^14}{}{:^14}|".format(' ','ADMINISTRACION DE PROVEEDORES',' '))
    print('+','-'*55,'+')
    print("1. Registrar")
    print("2. Buscar")
    print("3. Editar")
    print("4. Eliminar")
    print("5. Regresar menu principal")
    opcion =int(input(": "))
    if (opcion == 1):
        data ={
            "id":input("Ingrese el Id del proveedor :"),
            "nombre":input("Ingrese el Nombre del proveedor :"),
            "email":input("Ingrese el Email del proveedor :"),
        }
        diccProveedor["data"].append(data)
        core.crearInfo("proveedor.json",data)
    elif (opcion == 2):
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^16}{}{:^15}|".format(' ','BUSCAR PROVEEDOR',' '))
        print('+','-'*55,'+')

        proveeSearch = input("Ingrese el codigo del proveedor a buscar: ")

        for i,item in enumerate(diccProveedor["data"]):
            if proveeSearch == item["id"]:
                print(f'Id del proveedor: {item["id"]}')
                print(f'Nombre del proveedor: {item["nombre"]}')
                print(f'Email del proveedor: {item["email"]}')
                input("")
    elif (opcion == 3):
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^16}{}{:^15}|".format(' ','EDITAR PROVEEDOR',' '))
        print('+','-'*55,'+')

        proveeSearch = input("Ingrese el codigo del proveedor a editar: ")

        for i,item in enumerate(diccProveedor["data"]):
            if proveeSearch == item["id"]:
                item["nombre"] = item("Ingrese el nuevo nombre del proveedor o presione ENTER para omitir") or item["nombre"]
                item["email"] = item("Ingrese el nuevo email del proveedor o presione ENTER para omitir") or item["email"]

                core.EditarData("proveedores.json",diccProveedor)
    elif (opcion == 4):
        os.system("clear")
        print('+','-'*49,'+')
        print("|{:^16}{}{:^15}|".format(' ','ELIMINACION DE PROVEDDOR',' '))
        print('+','-'*49,'+')

        proveeSearch = input("Ingrese el codigo del proveedor a eliminar: ")
        for i,item in enumerate(diccProveedor["data"]):
            if proveeSearch in item["id"]:
                itemDel = diccProveedor["data"].pop(i)
                core.EditarData("proveedores.json",diccProveedor)
                input("Eliminado correctamente")
    elif (opcion == 5):
        isProveeRun = False
    if (isProveeRun):
        MainMenu()

