import MaterialBiblioteca

class libroDigital(MaterialBiblioteca):
    def __init__(self, titulo, autor, codigo, peso):
        super().__init__(titulo, autor, codigo)
        self.peso = peso
    
    def prestarMaterial(self):
        pass

    def devolverMaterial(self):
        pass

    def informacionGeneral(self):
        return f'Titulo: ${self.titulo} Autor: ${self.autor} Ejemplares: ${self.peso}'