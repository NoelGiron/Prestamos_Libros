from MaterialBiblioteca import MaterialBiblioteca

class LibroFisico(MaterialBiblioteca):
    def __init__(self, titulo, autor, numeroEjemplar):
        super().__init__(titulo, autor)
        self.numeroEjemplar = numeroEjemplar
        self.numeroDisponible = numeroEjemplar
        self.__codigo = None
        self.set_codigoUnico()

    def prestarMaterial(self):
        if  self.numeroDisponible > 0:
            print(f'Se a prestado el libro: {self.titulo}')
            self.numeroDisponible -= 1
        else:
            print("Este libro ya no se puede prestar")

    def devolverMaterial(self):
        if self.numeroDisponible < self.numeroEjemplar:
            print(f'Se a regresado el libro: {self.titulo}')
            self.numeroDisponible += 1
        else:
            print("Este libro ya no se puede devolver")

    def __str__(self):
        return f'Titulo: {self.titulo} Autor: {self.autor} Codigo: {self.get_codigo()} Ejemplares: {self.numeroDisponible}'