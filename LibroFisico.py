import MaterialBiblioteca

class libroFisico(MaterialBiblioteca):
    def __init__(self, titulo, autor, codigo, numeroEjemplar):
        super().__init__(titulo, autor, codigo)
        self.numeroEjemplar = numeroEjemplar

    def prestarMaterial(self):
        pass

    def devolverMaterial(self):
        pass

    def informacionGeneral(self):
        pass