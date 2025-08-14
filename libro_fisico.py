from MaterialBiblioteca import MaterialBiblioteca

class LibroFisico(MaterialBiblioteca):
    def __init__(self, titulo, autor, codigo, numeroEjemplar):
        super().__init__(titulo, autor, codigo)
        self.numeroEjemplar = numeroEjemplar

    def prestarMaterial(self):
        pass

    def devolverMaterial(self):
        pass

    def informacionGeneral(self):
        return f'Titulo: {self.titulo} Autor: {self.autor} Ejemplares: {self.numeroEjemplar}'