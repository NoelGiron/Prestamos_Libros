from abc import ABC, abstractmethod

class MaterialBiblioteca(ABC):
    def __init__(self, titulo, autor, codigo, estado):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.estado = True
    
    @abstractmethod
    def prestarMaterial(self):
        pass

    def devolverMaterial(self):
        pass

    def informacionGeneral(self):
        pass


