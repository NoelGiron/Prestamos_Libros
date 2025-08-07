# Prestamos_Libros
Una biblioteca universitaria necesita una aplicación que permita registrar y gestionar el préstamo de sus materiales bibliográficos de forma sencilla.

# Enunciado 
El enunciado debe contar con una clase base llamada MaterialBiblioteca, esta representa un material genérico de la biblioteca.

## Clase
 
## MaterialBiblioteca

### Atributos
* Título
* Autor
* Código único (generado automaticamente una cadena de 8 caracteres alfanuméricos)
* Estado del préstamo (disponible o prestado)

### Métodos
* Prestar el material
* Devolverlo
* Mostrar su información general

## SubClases

## Libro Físico
hereda de MaterialBiblioteca este tipo de libro puede ser prestado por un máximo de 7 días

### Atributos
* número de ejemplar

## Libro Digital
hereda de MaterialBiblioteca este tipo de libro puede ser prestado por un máximo de 3 días

### Atributos
* tamaño: este atributo adicional indicaa el tamaño del archivo en MB

## Menú
Para hacer funcional el sistema, debe implementarse un menú interactivo en consola.

* Registar nuevos materiales en la biblioteca, ya sean libros físicos o digitales 
* Gestionar los materiales ya registrados, permitiendo prestar, devolver o consultar información de cada uno 

El programa debe mantenerse en ejecución hasta que el usuario decida salir.