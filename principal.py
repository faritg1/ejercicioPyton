import clientes
import compras
import ventas
import productos
import proveedores
import os
if __name__ == "__main__":
    isActivate = True
    opcion=0
    dataproductos={'data':[]}
    dataproveedores={'data':[]}
    datacompras={'data':[]}
    dataventas={'data':[]}
    while isActivate:
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^20}{}{:^24}|".format(' ','Menu Pricipal',' '))
        print('+','-'*55,'+')
        print("1. Gestion de clientes")
        print("2. Gestion de producto")
        print("3. Gestion de Proveedores")
        print("4. Gestion de Compras")
        print("5. Gestion de ventas")
        print("6. Terminar")
        opcion = int(input(": "))
        if (opcion == 1):
            clientes.LoadInfoCliente()
            clientes.MainMenu()
        elif (opcion == 2):
            productos.loadInfoProduct()
            productos.mainMenu()
        elif (opcion == 3):
            proveedores.loadInfoProveedor()
            proveedores.MainMenu()
        elif (opcion == 4):
            compras.LoadInfoCompra()
            compras.MainMenu()
        elif (opcion == 5):
            ventas.MainMenu()
        elif (opcion == 6):
            isActivate = False
        else:
            print("Opcion no valida....")
            os.system("pause")

