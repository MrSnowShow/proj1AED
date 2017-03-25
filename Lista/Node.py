class Node:

    def __init__(self, pais, codPais, ano, val):
        self.pais = pais
        self.codPais = codPais
        self.ano = int(ano)
        self.val = float(val)

        self.next = None

    def getPais(self):
        return self.pais

    def getCodPais(self):
        return self.codPais

    def getAno(self):
        return self.ano

    def getVal(self):
        return self.val

    def setPais(self, pais):
        self.pais = pais

    def setCodPais(self, codPais):
        self.codPais = codPais

    def setAno(self, ano):
        self.ano = ano

    def setVal(self, val):
        self.val = val

    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next = next

    def editNode(self, novoPais=None, novoCodPais=None, novoAno=None, novoVal=None, novoNext = None):
        if novoPais:
            self.setPais(novoPais)

        if novoCodPais:
            self.setCodPais(novoCodPais)

        if novoAno:
            self.setAno(novoAno)

        if novoVal:
            self.setVal(novoVal)

        if novoNext:
            self.setNext(novoNext)