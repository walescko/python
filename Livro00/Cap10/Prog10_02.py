#Programa 10.2 0 Chave como propriedade apenas para leitura(nome.py)
from functools import total_ordering

@total_ordering
class Name:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
    def __repr__(self):
        return f"<Classe {type(self).__name__} em 0x{id(self):x} Nome: {self.name} Key: {self.chave}>"
    def __eq__(self, other):
        return self.name == other.name
    def __lt__(self, other):
        return self.name < other.name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if value is None or not value.strip():
            raise ValueError("Nome não pode ser nulo nem em branco")
        self.__name = value
        self.__key = Name.CreateKey(value)
    @property
    def key(self):
        return self.__key
    @staticmethod
    def CreateKey(name):
        return name.strip().lower()



