class TNode:

    def __init__(self, pais = None, codPais = None, ano = None, val = None, left = None, right = None, parent = None):


        self.pais = pais
        self.codPais = codPais
        self.ano = ano
        self.val = val
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


    def getSizeData(self):
        if type(self.pais) is list:
            return len(self.pais)
        elif type(self.codPais) is list:
            return len(self.codPais)
        elif type(self.ano) is list:
            return len(self.ano)
        elif type(self.val) is list:
            return len(self.val)
        else: return 0



    def setValues(self, pais = None, codPais = None, ano = None, val = None):

        if pais:
            if not type(self.pais) is list:
                self.pais = []
                self.pais.append(pais)
            else:
                self.pais.append(pais)

        if codPais:
            if not type(self.codPais) is list:

                self.codPais = []
                self.codPais.append(codPais)
            else:
                self.codPais.append(codPais)
        if ano:
            if not type(self.ano) is list:
                self.ano = []
                self.ano.append(ano)
            else:
                self.ano.append(ano)
        if val:
            if not type(self.val) is list:
                self.val = []
                self.val.append(val)
            else:
                self.val.append(val)

    def printNode(self,tName):

        s = ''

        if tName == 'pais':
            for i in range(self.getSizeData()):

                if type(self.pais) is str:
                    s = s + '\n\nPais: ' + self.pais
                else:
                    s = s + '\n\nPais: ' + self.pais.getPais()

                if self.codPais[i].getCodPais():
                    s = s  + '\nCódigo: ' + self.codPais[i].getCodPais()
                if self.ano[i].getAno():
                    s = s + '\nAno: ' + str(self.ano[i].getAno())
                if self.val[i].getVal():
                    s = s + '\nTaxa: ' + str(self.val[i].getVal())

        elif tName == 'codPais':
            for i in range(self.getSizeData()):
                if self.pais[i].getPais():
                    s = s + '\n\nPais: ' + self.pais[i].getPais()

                if type(self.codPais) is str:
                    s = s + '\nCódigo: ' + self.codPais
                else:
                    s = s + '\nCódigo: ' + self.codPais.getCodPais()

                if self.ano[i].getAno():
                    s = s + '\nAno: ' + str(self.ano[i].getAno())

                if self.val[i].getVal():
                    s = s + '\nTaxa: ' + str(self.val[i].getVal())

        elif tName == 'ano':
            for i in range(self.getSizeData()):

                if self.pais[i].getPais():
                    s = s + '\n\nPais: ' + self.pais[i].getPais()

                if self.codPais[i].getCodPais():
                    s = s  + '\nCódigo: ' + self.codPais[i].getCodPais()

                if type(self.ano) is int:
                    s = s +'\nAno: ' + str(self.ano)
                else:
                    s = s + '\nAno: ' + str(self.ano.getAno())

                if self.val[i].getVal():
                    s = s + '\nTaxa: ' + str(self.val[i].getVal())

        elif tName == 'val':
            for i in range(self.getSizeData()):
                if self.pais[i].getPais():
                    s = s + '\n\nPais: ' + self.pais[i].getPais()

                if self.codPais[i].getCodPais():
                    s = s  + '\nCódigo: ' + self.codPais[i].getCodPais()

                if self.ano[i].getAno():
                    s = s + '\nAno: ' + str(self.ano[i].getAno())
                if type(self.val) is float:
                    s = s + '\nTaxa: ' + str(self.val)
                else:
                    s = s + '\nTaxa: ' + str(self.val.getVal())
        return s


    def getNodeVals(self,tName):
        pais = []
        codPais = []
        ano = []
        val = []

        s = ''

        if tName == 'pais':
            for i in range(self.getSizeData()):

                if type(self.pais) is str:
                    pais.append(self.pais)
                else:
                    pais.append(self.pais.getPais())

                if self.codPais[i].getCodPais():
                    codPais.append(self.codPais[i].getCodPais())
                if self.ano[i].getAno():
                    ano.append(self.ano[i].getAno())
                if self.val[i].getVal():
                    val.append(self.val[i].getVal())

        elif tName == 'codPais':
            for i in range(self.getSizeData()):
                if self.pais[i].getPais():
                    pais.append(self.pais[i].getPais())

                if type(self.codPais) is str:
                    codPais.append(self.codPais)
                else:
                    codPais.append(self.codPais.getCodPais())

                if self.ano[i].getAno():
                    ano.append(self.ano[i].getAno())

                if self.val[i].getVal():
                    val.append(self.val[i].getVal())

        elif tName == 'ano':
            for i in range(self.getSizeData()):

                if self.pais[i].getPais():
                    pais.append(self.pais[i].getPais())

                if self.codPais[i].getCodPais():
                    codPais.append(self.codPais[i].getCodPais())

                if type(self.ano) is int:
                    ano.append(self.ano)
                else:
                    ano.append(self.ano.getAno())

                if self.val[i].getVal():
                    val.append(self.val[i].getVal())

        elif tName == 'val':
            for i in range(self.getSizeData()):
                if self.pais[i].getPais():
                    pais.append(self.pais[i].getPais())

                if self.codPais[i].getCodPais():
                    codPais.append(self.codPais[i].getCodPais())

                if self.ano[i].getAno():
                    ano.append(self.ano[i].getAno())
                if type(self.val) is float:
                    val.append(self.val)
                else:
                    val.append(self.val.getVal())

        return (pais, codPais, ano, val)


