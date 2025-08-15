from Estructuras.ListaEnlazada import ListaEnlazada
from LibroDigital import libroDigital
from libro_fisico import LibroFisico

listaFisica = ListaEnlazada();
listaDigital = ListaEnlazada();

def Menu():
    print("<------------------Menu--------------------->")
    print("< 1) Registrar nuevo Material--------------->")
    print("< 2) Gestionar los materiales registrados--->")
    print("< 3) Salir---------------------------------->")
    print("<------------------------------------------->")

def menuRegistro():
    print("1) Registrar libro físico")
    print("2) Registrar libro digital")
    print("3) Regresar")
    opcion = int(input("Ingrese una de las opciones: "))
    if opcion == 1:      
        print("1) Ingrese un nuevo libro fisico")
        libro1 = LibroFisico("soledad", "Garcia", "1234m3l", 23);
        print(libro1.informacionGeneral());
    elif opcion == 2:
        print("2) Ingrese un nuevo libro digital")
        libro2 = libroDigital("cubmres", "Manuel", "f12few", 45);
        print(libro2.informacionGeneral());           
    elif opcion == 3:
        pass
    else:
        print("Opción no váldia, intente de nuevo")

if __name__=="__main__":
    pregunta = True
    while pregunta:
        Menu()
        opcion = int(input("ingrese una de las opciones: "))

        if opcion == 1:
            menuRegistro()

        elif opcion == 2:
            print("1) Prestar libro")
            print("2) Devolver libro")
            print("3) Consultar informacion")
            print("4) Regresar")
            opcion = int(input("ingrese una de las opciones: "))
            
            if opcion == 1:
                print("Se a prestado un libro")
            
            elif opcion == 2:
                print("Se a devuelto el libro")
            
            elif opcion == 3:
                print("Esta es la informacion del libro")

            elif opcion == 4:
                pass
                
            else:
                print("Opción no váldia, intente de nuevo")

        elif opcion == 3:
            break

        else:
            print("Opción no váldia, intente de nuevo")