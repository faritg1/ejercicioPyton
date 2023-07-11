import core
import os
import productos

diccCompra = {"data":[]}

"""
Compras : El programa debe permitir controlar las compras de los productos. La información que se
maneja en las compras es: Nro documento de compra, fecha de compra.Valor compra,cantidad comprada.
"""
def LoadInfoCompra():
    global diccCompra
    if (core.checkFile("compra.json")):
        diccCompra = core.LoadInfo("compra.json")
    else:
        core.crearInfo("compra.json",diccCompra)

def MainMenu():
    os.system("clear")
    isCompraRun = True
    if(core.checkFile("compra.json")):
        diccCompra = core.LoadInfo("compra.json")
    os.system("clear")
    print('+','-'*55,'+')
    print("|{:^16}{}{:^17}|".format(' ','ADMINISTRACION DE COMPRAS',' '))
    print('+','-'*55,'+')
    print("1. Registrar Compra")
    print("2. Buscar Compra")
    print("3. Devolución")
    print("4. Anular factura de compra")
    print("5. Regresar menu principal")
    opcion =int(input(": "))
    if (opcion == 1):
        data = {
            "id": input("Ingrese el id de la compra: "),
            "nroDocCompra": input("Ingrese el numero de la compra: "),
            "fechaCompra": input("Ingrese la fecha de compra: "),
            "valorCompra": float(input("Ingrese el valor de compra: ")),
            "cantidadCompra": int(input("Ingrese la cantidad de compra: ")),
            "estado": True
        }

        core.crearInfo("compra.json",data)

    elif (opcion == 2):
        os.system("clear")
        print('+','-'*49,'+')
        print("|{:^16}{}{:^15}|".format(' ','BUSCADOR DE Compras',' '))
        print('+','-'*49,'+')

        compraSearch = input("Ingrese el codigo de la compra a buscar: ")

        for i,item in enumerate(diccCompra["data"]):
            if compraSearch == item["id"]:
                print(f'Id de la compra: {item["id"]}')
                print(f'Numero de documento de la compra: {item["nroDocCompra"]}')
                print(f'Fecha de la compra: {item["fechaCompra"]}')
                print(f'Valor de la compra: {item["valorCompra"]}')
                print(f'Cantidad de la compra: {item["cantidadCompra"]}')
                print(f'estado de la compra: {item["estado"]}')
                input("")

    elif (opcion == 3):
        pass
    elif (opcion == 4):
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^16}{}{:^15}|".format(' ','Anular factura de compra',' '))
        print('+','-'*55,'+')

        compraSearch = input("ingrese el codigo de la compra: ")
        for i,item in enumerate(diccCompra["data"]):
            if compraSearch == item["id"]:
                print("1.Generar Factura\n2.Anular Factura")
                diccCompra["data"][i]["estado"] = True if int(input(":")) == 1 else False 
                core.EditarData("compra.json",diccCompra)

    elif (opcion == 5):
        isCompraRun = False
    if (isCompraRun):
        MainMenu()