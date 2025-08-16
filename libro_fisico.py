from MaterialBiblioteca import MaterialBiblioteca

class LibroFisico(MaterialBiblioteca):
    def __init__(self, titulo, autor, codigo, numeroEjemplar):
        super().__init__(titulo, autor, codigo)
        self.numeroEjemplar = numeroEjemplar

    def get(self):
        return self.numeroEjemplar
    
    def set(self, numero):
        self.numeroEjemplar = numero

    def prestarMaterial(self):
        ejemplarOriginal = self.numeroEjemplar
        ejemplarActual = ejemplarOriginal - 1
        if ejemplarActual != -1:
            print(f'Se a prestado el libro: {self.titulo}')
            self.numeroEjemplar = ejemplarActual
        else:
            print("Este libro ya no se puede prestar")

    def devolverMaterial(self):
        ejemplarOriginal = self.numeroEjemplar
        ejemplarActual = ejemplarOriginal + 1
        if ejemplarActual != self.numeroEjemplar:
            print(f'Se a regresado el libro: {self.titulo}')
            self.numeroEjemplar = ejemplarActual
        else:
            print("Este libro ya no se puede devolver")

    def __str__(self):
        return f'Titulo: {self.titulo} Autor: {self.autor} Ejemplares: {self.numeroEjemplar}'