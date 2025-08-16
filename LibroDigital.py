from MaterialBiblioteca import MaterialBiblioteca
class libroDigital(MaterialBiblioteca):
    def __init__(self, titulo, autor, peso):
        super().__init__(titulo, autor)
        self.peso = peso
        self.__codigo = None
        self.set_codigoUnico()
    
    def prestarMaterial(self):
        pass

    def devolverMaterial(self):
        pass

    def __str__(self):
        return f'Titulo: {self.titulo} Autor: {self.autor} Codigo: {self.get_codigo()} Peso: {self.peso}MB'