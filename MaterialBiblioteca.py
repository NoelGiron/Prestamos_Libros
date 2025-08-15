from abc import ABC, abstractmethod
import random
import string

class MaterialBiblioteca(ABC):
    def __init__(self, titulo, autor, codigo):
        self.titulo = titulo
        self.autor = autor
        self.__codigo = codigo
        self.estado = True

    def set_codigoUnico(self):
        caracteres = string.ascii_letters + string.digits
        self.__codigo = ''.join(random.choice(caracteres) for _ in range(8))

    @abstractmethod
    def prestarMaterial(self):
        pass
    
    @abstractmethod     
    def devolverMaterial(self):
        pass
    
    @abstractmethod     
    def __str__(self):
        pass
    


