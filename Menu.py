from Phones import Phones 
import os 

class Menu:
    
    def __init__():
        
        print ("Seleccione")
        print ("1.- para listar los modelos phones")
        print ("2.- para agregar modelo")
        print ("3.- para salir del sistema")
        valor = int (input("...\n"))

        if valor == 0:
            print ("hasta pronto :)")
        elif valor == 1:
            os.sytem ('clear')
            print ("listando modelos")
            Phones.list_all()
            Menu.post_listar_Modelos()
        
        elif valor ==2:
            print ("solicitando datos de phones\n")
            Model : input("ingrese modelo del Phone")
            Phone = Phone(Model)
            print("Phones Guardado con exito\n")
        else:
            print ("no se reconoce el comando")
            Menu.__init()


    def post_listar_peliculas():
        print("ingrese el ID de phone a modificar")
        print("ingrese 0 para exit")
        value = input("\n")
        if value == 0:
            print("hasta pronto:)")
        else :
            print (f'se va modificar la pelicula con ID {value}')



Menu.__init__()