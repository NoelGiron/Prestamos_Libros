from ListaEnlazada import *
from LibroDigital import *
from libro_fisico import *

listaFisica = ListaEnlazada();
listaDigital = ListaEnlazada();

def Menu():
    print("<------------------Menu--------------------->")
    print("< 1) Registrar nuevo Material--------------->")
    print("< 2) Gestionar los materiales registrados--->")
    print("< 3) Salir---------------------------------->")
    print("<------------------------------------------->")

def Gestion():
    print("1) Prestar libro")
    print("2) Devolver libro")
    print("3) Consultar informacion")
    print("4) Regresar")

def consultaInformacion():
    print("<-----------------Lista de libros fisícos--------------->")
    listaFisica.imprimir();
    print("<------------------------------------------------------->")
    print("<-----------------Lista de libros digitales------------->")
    listaDigital.imprimir();
    print("<------------------------------------------------------->")

def Registro():
    print("1) Registrar libro físico")
    print("2) Registrar libro digital")
    print("3) Regresar")
    opcion = int(input("Ingrese una de las opciones: "))
    if opcion == 1:      
        print("1) Ingrese un nuevo libro fisico")
        registroLibroFisico();
    elif opcion == 2:
        print("2) Ingrese un nuevo libro digital")
        registroLibroDigital();  
    elif opcion == 3:
        pass
    else:
        print("Opción no váldia, intente de nuevo")

def registroLibroFisico():
    titulo = input("Ingrese el titulo del libro: ");
    autor = input("Ingrese el nombre del autor: ");
    codigo = input("Ingrese el codigo del libro: ");
    numero = int(input("Ingrese el numero de copias del libro: "));
    nuevoLibroFisico = LibroFisico(titulo, autor, codigo, numero);
    listaFisica.insertar(nuevoLibroFisico);
    listaFisica.imprimir();

def registroLibroDigital():
    titulo = input("Ingrese el titulo del libro: ");
    autor = input("Ingrese el nombre del autor: ");
    codigo = input("Ingrese el codigo del libro: ");
    numero = int(input("Ingrese el peso del libro: "));
    nuevoLibroDigital = libroDigital(titulo, autor, codigo, numero);
    listaDigital.insertar(nuevoLibroDigital);
    listaDigital.imprimir();

def prestarLibro():
    print("<-----------------Lista de libros fisícos--------------->")
    listaFisica.imprimir();
    print("<------------------------------------------------------->")
    libro = int(input("Seleccione el libro que quiere prestar: "))
    libroPrestado = listaFisica.recorrer(libro)
    ejemplarActual = libroPrestado.get()
    if ejemplarActual != 0:
        libroPrestado.set(ejemplarActual - 1)
    else:
        print("Este libro ya se puede prestar");
    print(libroPrestado.numeroEjemplar);

if __name__=="__main__":
    pregunta = True
    while pregunta:
        Menu()
        opcion = int(input("ingrese una de las opciones: "))

        if opcion == 1:
            Registro()

        elif opcion == 2:
            Gestion()
            opcion = int(input("ingrese una de las opciones: "))
            
            if opcion == 1:
                prestarLibro()
            
            elif opcion == 2:
                print("Se a devuelto el libro")
            
            elif opcion == 3:
                consultaInformacion()

            elif opcion == 4:
                pass
                
            else:
                print("Opción no váldia, intente de nuevo")

        elif opcion == 3:
            break

        else:
            print("Opción no váldia, intente de nuevo")