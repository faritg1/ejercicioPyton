import core
import os

"""
Ventas : El programa debe permitir controlar las ventas a clientes la información que se tiene en
cuenta en el proceso de compra es la siguiente: Nro factura venta, fecha venta, Nro Id del cliente, Nombre
del cliente, total de factura y el detalle de venta (Cod producto, Cantidad vendida, valor unitario)
"""


def MainMenu():
    os.system("clear")
    isCliRun = True
    os.system("clear")
    print('+','-'*55,'+')
    print("|{:^16}{}{:^17}|".format(' ','ADMINISTRACION DE VENTAS',' '))
    print('+','-'*55,'+')
    print("1. Registrar")
    print("2. Buscar")
    print("3. Devolución")
    print("4. Anular factura")
    print("5. Regresar menu principal")
    opcion =int(input(":)_"))
    if (opcion == 1):
        pass
    elif (opcion == 2):
        pass
    elif (opcion == 3):
        pass
    elif (opcion == 4):
        pass
    elif (opcion == 5):
        isCliRun = False
    if (isCliRun):
        MainMenu()