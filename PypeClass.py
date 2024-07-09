class Funil:

    numero_funis = 0

    def __init__(self, nome, id, fases=["vazio"], negs=["vazio"]):
        self.__nome = nome
        self.__id = int(id)
        self.__fases = fases
        self.__negs = negs
        Funil.numero_funis += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if isinstance(valor, str) and valor:
            self.__nome = valor
        else:
            raise ValueError("Nome deve ser uma string não vazia")
    
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, valor):
        if isinstance(valor, str) or isinstance(valor, int) and valor:
            self.__id = valor
        else:
            raise ValueError("ID deve ser uma string não vazia ou número")
        
    @property
    def fases(self):
        return self.__fases

    @fases.setter
    def fases(self, valor):
        if isinstance(valor, list) and valor:
            self.__fases = valor
        else:
            raise ValueError("As fases veem numa lista")
    
    @property
    def negs(self):
        return self.__negs

    @negs.setter
    def negs(self, valor):
        if isinstance(valor, list) and valor:
            self.__negs = valor
        else:
            raise ValueError("Os negócios veem numa lista")

    def __str__(self):
        return f"Nome: {self.nome}\nID: {self.id}\nETAPAS: {self.fases}\n"