import core
import os 

diccProducto = {"data":[]}

def loadInfoProduct():
    global diccProducto
    if (core.checkFile("productos.json")):
        diccProducto = core.LoadInfo("productos.json")
    else: 
        core.crearInfo("productos.json",diccProducto)

def mainMenu():
    os.system("clear")
    isProducRun = True
    if(core.checkFile("productos.json")):
        diccProducto = core.LoadInfo("productos.json")
    os.system("clear")
    print('+','-'*55,'+')
    print("|{:^16}{}{:^15}|".format(' ','ADMINISTRACION DE PRODUCTOS',' '))
    print('+','-'*55,'+')
    print("1. Registrar")
    print("2. Buscar")
    print("3. Editar")
    print("4. Activar o Inactivar")
    print("5. Regresar menu principal")
    opcion =int(input(": "))

    if(opcion == 1):
        data = {
            "id":input("Ingrese el Id del producto :"),
            "nombre":input("Ingrese el Nombre del producto :"),
            "stockMin":int(input("Ingrese el Stock minimo :")),
            "stockMax":int(input("Ingrese el Stock maximo :")),
            "cantidad": 0,
            "valorCompra":float(input("Ingrese el valor de compra :")),
            "valorVenta":float(input("Ingrese el valor de venta :")),
            "estado":True
        }

        core.crearInfo("productos.json",data)

    elif(opcion == 2):
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^16}{}{:^15}|".format(' ','BUSCAR PRODUCTO',' '))
        print('+','-'*55,'+')

        producSearch = input("Ingrese el codigo del cliente a buscar: ")

        for i,item in enumerate(diccProducto["data"]):
            if producSearch in item["id"]:
                print(f'Id del producto: {item["id"]}')
                print(f'Nombre del producto: {item["nombre"]}')
                print(f'Stock minimo del producto: {item["stockMin"]}')
                print(f'Stock maximo del producto: {item["stockMax"]}')
                print(f'Valor de compra del producto: {item["valorCompra"]}')
                print(f'VAlor de venta del producto: {item["valorVenta"]}')
                print(f'Estado del producto: {item["estado"]}')
                input("")

    elif(opcion == 3):
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^16}{}{:^15}|".format(' ','EDITAR PRODUCTO',' '))
        print('+','-'*55,'+')

        producSearch = input("Ingrese el codigo del producto a editar: ")

        for i,item in enumerate(diccProducto["data"]):
            if producSearch in item["id"]:
                item["nombre"] = input("Ingrese el nuevo nombre del producto o presione ENTER para omitir: ") or item["nombre"]
                item["stockMin"] = input("Ingrese el nuevo stock minimo del producto o presione ENTER para omitir: ") or item["stockMin"]
                item["stockMax"] = input("Ingrese el nuevo stock maximo del producto o presione ENTER para omitir: ") or item["stockMax"]
                item["valorCompra"] = input("Ingrese el nuevo valor de compra del producto o presione ENTER para omitir: ") or item["valorCompra"]
                item["valorVenta"] = input("Ingrese el nuevo valor de venta del producto o presione ENTER para omitir: ") or item["valorVenta"]
                core.EditarData("productos.json",diccProducto)

    elif(opcion == 4):
        os.system("clear")
        print('+','-'*55,'+')
        print("|{:^16}{}{:^15}|".format(' ','Activar o Inactivar',' '))
        print('+','-'*55,'+')

        producSearch = input("ingrese el codigo del producto: ")
        for i,item in enumerate(diccProducto["data"]):
            if producSearch in item["id"]:
                print("1.Activar\n2.Inactivar")
                diccProducto["data"][i]["estado"] = True if int(input(":")) == 1 else False 
                core.EditarData("productos.json",diccProducto)
    
    elif(opcion == 4):
        isProducRun = False
    
    if(isProducRun):
        mainMenu()



        
