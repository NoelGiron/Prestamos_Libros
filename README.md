# Prestamos_Libros
Una biblioteca universitaria necesita una aplicación que permita registrar y gestionar el préstamo de sus materiales bibliográficos de forma sencilla

# Enunciado 
El enunciado debe de contar con una clase base llamada MaterialBiblioteca, esta representa un material generico de la biblioteca 

## Clase
 
## MaterialBiblioteca

### Atributos
* Titulo
* Autor
* Codigo unico (generado automaticamente  una cadea de 8 caracteres alfanumericos)
* Estado del prestamo (disponible o prestado)

### Metodos
* Prestar el material
* Devolverlo
* Mostrar su informacion general

## SubClases

## Libro Fisico
hereda de MaterialBiblioteca este tipo de libro puede ser prestado por un maximo de 7 dias

### Atributos
* numero de ejemplar

## Libro Digital
hereda de MaterialBiblioteca este tipo de libro puede ser prestado por un maximo de 3 dias

### Atributos
*tamaño este atributo adicional inidia el tamaño del arthcio (en MB)

## Menu
Para hacer funcional el sistema, debe implementarse un menu interactivo en consola

* Registar nuevos materiales en la biblioteca, ya se libros fisicos o digitales 
* Gestionar los materiales ya registrados, permitiendo prestar, devolver o consultar informacion de cda uno 

el programa debe de mantenerse en ejecucion hasta que el usuario decida salir.