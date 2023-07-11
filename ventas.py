import core
import os
import clientes

diccVenta = {"data":[]}

"""
Ventas : El programa debe permitir controlar las ventas a clientes la información que se tiene en
cuenta en el proceso de venta es la siguiente: Nro factura venta, fecha venta, Nro Id del cliente, Nombre
del cliente, total de factura y el detalle de venta (Cod producto, Cantidad vendida, valor unitario)
"""

def LoadInfoVenta():
    global diccVenta
    if (core.checkFile("venta.json")):
        diccVenta = core.LoadInfo("venta.json")
    else:
        core.crearInfo("venta.json",diccVenta)

def MainMenu():
    os.system("clear")
    isVentaRun = True
    if(core.checkFile("venta.json")):
        diccVenta = core.LoadInfo("venta.json")
    os.system("clear")
    print('+','-'*55,'+')
    print("|{:^16}{}{:^17}|".format(' ','ADMINISTRACION DE VENTAS',' '))
    print('+','-'*55,'+')
    print("1. Registrar Venta")
    print("2. Buscar Venta")
    print("3. Devolución")
    print("4. Anular factura Venta")
    print("5. Regresar menu principal")
    opcion =int(input(": "))
    if (opcion == 1):
        os.system("clear")
        print('+','-'*49,'+')
        print("|{:^16}{}{:^15}|".format(' ','REGISTRAR VENTA DEL CLIENTE',' '))
        print('+','-'*49,'+')

        #ARREGLAR!!!

        cliVenta = input("Ingrese el codigo del cliente:")

        for i,item in enumerate(clientes.diccCliente["data"]):
            if cliVenta == item["id"]:
                data ={
            "id":input("Ingrese el Id del cliente :"),
            "nombre":input("Ingrese el Nombre del cliente :"),
            "email":input("Ingrese el Email del cliente :"),
            }
                core.crearInfo("venta.json",data)
            else:
                return print("NO SE ENCONTRO"),input("")
    elif (opcion == 2):
        pass
    elif (opcion == 3):
        pass
    elif (opcion == 4):
        pass
    elif (opcion == 5):
        isVentaRun = False
    if (isVentaRun):
        MainMenu()