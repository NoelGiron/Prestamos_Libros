from abc import ABC, abstractmethod
import random
import string

class MaterialBiblioteca(ABC):
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.__codigo = None
        self.estado = True
        self.set_codigoUnico()

    def set_codigoUnico(self):
        caracteres = string.ascii_letters + string.digits
        self.__codigo = ''.join(random.choice(caracteres) for _ in range(8))

    def get_codigo(self):
        return self.__codigo
    
    @abstractmethod
    def prestarMaterial(self):
        pass
    
    @abstractmethod     
    def devolverMaterial(self):
        pass
    
    @abstractmethod     
    def __str__(self):
        pass
    


