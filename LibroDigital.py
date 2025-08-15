from MaterialBiblioteca import MaterialBiblioteca
class libroDigital(MaterialBiblioteca):
    def __init__(self, titulo, autor, codigo, peso):
        super().__init__(titulo, autor, codigo)
        self.peso = peso
    
    def prestarMaterial(self):
        pass

    def devolverMaterial(self):
        pass

    def __str__(self):
        return f'Titulo: {self.titulo} Autor: {self.autor} Peso: {self.peso}MB'