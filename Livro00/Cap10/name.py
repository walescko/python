class Name:
    def __init__(self, name):
        if name is None or not name.strip():
            raise ValueError('Nome não pode ser nulo nem em branco')
        self.name = name
        self.key = name.strip().lower()
    def __str__(self):
        return self.name
    def __repr__(self):
        return f"<Classe {type(self).__name} em 0x{id(self):x} Nome: {self.name} Key: [self.chave ]>""
    def __eq __(self, other):
        print("__eq__ Chamado")
        return self.name == other.name
    def __lt__(self, other):
        print("__lt__ Chamado")
        return self.name < other.name



