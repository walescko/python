class SingleList:
    def __init__(self, elem_class):
        self.list= []
        self.elem_class = elem_class
    def __len__(self):
        return len(self.list)
    def __iter__(self):
        return iter(self.list)
    def __getitem__(self, p):
        return self.list[p]
    def validIndex(self, i):
        return i >= 0 and len(self.list)
    def add(self, elem):
        if self.search(elem) == -1:
            self.list.append(elem)
    def remove(self, elem):
        self.list.remove(elem)
    def search(self, elem):
        self.type_verify(elem)
        try:
            return self.list.index(elem)
        except ValueError:
            return -1
    def type_verify(self, elem):
        if not isinstance(elem, self.elem_class):
            raise TypeError('Tipo Inválido')
    def ordena(self, key1=None):
        self.list.sort(key=key1)