class TNode:

    def __init__(self, pais, codPais, ano, val, left = None, right = None, parent = None):


        self.pais = pais
        self.codPais = codPais
        self.ano = int(ano)
        self.val = float(val)
        self.parent = parent
        self.left = left
        self.right = right


    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getParent(self):
        return self.parent

    def setLeft(self, no):
        self.left = no

    def setRight(self, no):
        self.right = no

    def setParent(self, no):
        self.parent = no

    def getPais(self):
        return self.pais

    def getCodPais(self):
        return self.codPais

    def getAno(self):
        return self.ano

    def getVal(self):
        return self.val

    def setPais(self, nPais):
        self.pais = nPais

    def setCodPais(self, cCodPais):
        self.codPais = cCodPais

    def setAno(self, nAno):
        self.ano = nAno

    def setVal(self, nVal):
        self.val = nVal




    def printNode(self):

        s = '\n+++\n'

        s = s + 'Pais: ' + self.pais + '\nCódigo: ' + self.codPais +'\nAno: ' + str(self.ano) + '\nTaxa: ' + str(self.val)

        return s