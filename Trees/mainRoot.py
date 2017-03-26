from BSTTrees import bst
from Tnodes import TNode
class MainRoot:

    def __init__(self):
        self.tPais = bst('pais')
        self.tCodPais = bst('codPais')
        self.tAno = bst('ano')
        self.tVal = bst('val')

    def getTPais(self):
        return self.tPais

    def getTCodPais(self):
        return self.tCodPais

    def getTAno(self):
        return self.tAno

    def getTVal(self):
        return self.tVal

    def checkTreesEmpty(self):
        if not (self.tPais and self.tCodPais and self.tAno and self.tVal):
            return True
        return False

    def add(self, pais, codPais, ano, val):

        nPais = TNode(pais=pais)
        nPais = self.tPais.insere(nPais)

        nCod = TNode(codPais=codPais)
        nCod = self.tCodPais.insere(nCod)

        nAno = TNode(ano=int(ano))
        nAno = self.tAno.insere(nAno)

        nVal = TNode(val=float(val))
        nVal = self.tVal.insere(nVal)

        nPais.setValues(codPais=nCod, ano=nAno, val=nVal)
        nCod.setValues(pais=nPais, ano=nAno, val=nVal)
        nAno.setValues(pais=nPais, codPais=nCod, val=nVal)
        nVal.setValues(pais=nPais, codPais=nCod, ano=nAno)

    def search(self, pais = None, codPais = None, ano = None, val = None):
        aux = []
        tName = ''
        if pais:
            tName = self.tPais.getTName()
            n = self.tPais.search(pais=pais, codPais = codPais, ano=ano, val=val)
            if n == None:
                return (None, '')

            aux = TNode(pais=n)

            for i in range(n.getSizeData()):
                eq = True
                if codPais and n.getCodPais()[i] and n.getCodPais()[i].getCodPais() != codPais:
                    eq = False

                if ano and n.getAno()[i]:
                    if not n.getAno()[i].getAno() == ano:
                        eq = False

                if val and n.getVal()[i]:
                    if not n.getVal()[i].getVal() == val:
                        eq = False

                if eq:
                    aux.setValues(codPais=n.getCodPais()[i])
                    aux.setValues(ano=n.getAno()[i])
                    aux.setValues(val=n.getVal()[i])



        elif codPais:
            tName = self.tCodPais.getTName()
            n = self.tCodPais.search(pais=pais, codPais=codPais, ano=ano, val=val)

            if n == None:
                return (None, '')

            aux = TNode(codPais=n)
            for i in range(n.getSizeData()):
                eq = True
                if pais and n.getPais()[i] and n.getPais()[i].getPais() != pais:
                    eq = False

                if ano and n.getAno()[i]:
                    if not n.getAno()[i].getAno() == ano:
                        eq = False

                if val and n.getVal()[i]:
                    if not n.getVal()[i].getVal() == val:
                        eq = False


                if eq:
                    aux.setValues(pais=n.getPais()[i])
                    aux.setValues(ano=n.getAno()[i])
                    aux.setValues(val=n.getVal()[i])


        elif ano:
            tName = self.tAno.getTName()
            n = self.tAno.search(pais=pais, codPais=codPais, ano=ano, val=val)

            if n == None:
                return (None, '')
            aux = TNode(ano=n)
            for i in range(n.getSizeData()):
                eq = True
                if pais and n.getPais()[i] and n.getPais()[i].getPais() != pais:
                    eq = False
                if codPais and n.getCodPais()[i]:
                    if not n.getCodPais()[i].getCodPais() == ano:
                        eq = False
                if val and n.getVal()[i]:
                    if not n.getVal()[i].getVal() == val:
                        eq = False


                if eq:
                    aux.setValues(pais=n.getPais()[i])
                    aux.setValues(codPais=n.getCodPais()[i])
                    aux.setValues(val=n.getVal()[i])


        elif val:
            tName = self.tVal.getTName()
            n = self.tVal.search(pais=pais, codPais=codPais, ano=ano, val=val)

            if n == None:
                return (None, '')

            aux = TNode(val=n)
            for i in range(n.getSizeData()):
                eq = True
                if pais and n.getPais()[i] and n.getPais()[i].getPais() != pais:
                    eq = False

                if codPais and n.getCodPais()[i]:
                    if not n.getCodPais()[i].getCodPais() == codPais:
                        eq = False

                if ano and n.getAno[i]:
                    if not n.getAno()[i].getAno() == val:
                        eq = False
                if eq:
                    aux.setValues(pais=n.getPais()[i])
                    aux.setValues(codPais=n.getCodPais()[i])
                    aux.setValues(ano=n.getAno()[i])

        return (aux, tName)

    def verNode(self, node, size, tName):
        if size == 0:
            self.removeNode(node, tName)

    def remover(self, pais = None, codPais = None, ano = None, val = None):
        i = 0
        if pais:
            nPais = self.tPais.search(pais=pais)
            if nPais == None:
                return

            a = nPais.getSizeData()
            while i < a:
                eq = True
                if codPais and nPais.getCodPais()[i].getCodPais() != codPais:
                    eq = False

                if (ano and nPais.getAno()[i].getAno() != ano):
                    eq = False

                if val and nPais.getVal()[i].getVal() != val:
                    eq = False

                if eq:
                    nCodPais = nPais.getCodPais().pop(i)
                    nAno = nPais.getAno().pop(i)
                    nVal = nPais.getVal().pop(i)
                    nCodPais.getPais().remove(nPais)
                    nCodPais.getAno().remove(nAno)
                    nCodPais.getVal().remove(nVal)

                    nAno.getPais().remove(nPais)
                    nAno.getCodPais().remove(nCodPais)
                    nAno.getVal().remove(nVal)

                    nVal.getPais().remove(nPais)
                    nVal.getCodPais().remove(nCodPais)
                    nVal.getAno().remove(nAno)

                    self.verNode(nPais, nPais.getSizeData(), 'pais')
                    self.verNode(nCodPais, nCodPais.getSizeData(), 'codPais')
                    self.verNode(nAno, nAno.getSizeData(), 'ano')
                    self.verNode(nVal, nVal.getSizeData(), 'val')
                    i = 0
                    a -= 1
                else:
                    i += 1



        elif codPais:
            nCodPais = self.tCodPais.search(codPais=codPais)
            if nCodPais == None:
                return
            a = nCodPais.getSizeData()
            while i< a:
                eq = True

                if val and nCodPais.getVal()[i].getVal() == val:
                    eq = False

                if pais and nCodPais.getPais()[i].getPais() != pais:
                    eq = False

                if ano and nCodPais.getAno()[i].getAno() != ano:
                    eq = False

                if eq:
                    nPais = nCodPais.getPais().pop(i)
                    nAno = nCodPais.getAno().pop(i)
                    nVal = nCodPais.getVal().pop(i)

                    nPais.getCodPais().remove(nCodPais)
                    nPais.getAno().remove(nAno)
                    nPais.getVal().remove(nVal)

                    nAno.getPais().remove(nPais)
                    nAno.getCodPais().remove(nCodPais)
                    nAno.getVal().remove(nVal)

                    nVal.getPais().remove(nPais)
                    nVal.getCodPais().remove(nCodPais)
                    nVal.getAno().remove(nAno)

                    self.verNode(nPais, nPais.getSizeData(), 'pais')
                    self.verNode(nCodPais, nCodPais.getSizeData(), 'codPais')
                    self.verNode(nAno, nAno.getSizeData(), 'ano')
                    self.verNode(nVal, nVal.getSizeData(), 'val')
                    i = 0
                    a-=1
                else:
                    i+=1

        elif ano:
            nAno = self.tAno.search(ano=ano)
            if nAno == None:
                return
            a = nAno.getSizeData()
            while i < a:
                eq = True

                if pais and nAno.getPais()[i].getPais() != pais:
                    eq = False

                if codPais and nAno.getCodPais()[i].getCodPais() != codPais:
                    eq = False

                if val and nAno.getVal()[i].getVal() != val:
                    eq = False

                if eq:
                    nPais = nAno.getPais().pop(i)
                    nCodPais = nAno.getCodPais().pop(i)
                    nVal = nAno.getVal().pop(i)

                    nPais.getCodPais().remove(nCodPais)
                    nPais.getAno().remove(nAno)
                    nPais.getVal().remove(nVal)

                    nCodPais.getPais().remove(nPais)
                    nCodPais.getAno().remove(nAno)
                    nCodPais.getVal().remove(nVal)

                    nVal.getPais().remove(nPais)
                    nVal.getCodPais().remove(nCodPais)
                    nVal.getAno().remove(nAno)

                    self.verNode(nPais, nPais.getSizeData(), 'pais')
                    self.verNode(nCodPais, nCodPais.getSizeData(), 'codPais')
                    self.verNode(nAno, nAno.getSizeData(), 'ano')
                    self.verNode(nVal, nVal.getSizeData(), 'val')
                    i = 0
                    a -=1
                else:
                    i+=1

        elif val:
            nVal = self.tVal.search(val=val)
            if nVal == None:
                return
            a = nVal.getSizeData()
            while i < a:
                eq = True
                if (pais and nVal.getPais()[i].getPais() != pais):
                    eq = False
                if codPais and nVal.getCodPais()[i].getCodPais() != codPais:
                    eq = False
                if ano and nVal.getAno()[i].getAno() != ano:
                    eq = False

                if eq:
                    nPais = nVal.getPais().pop(i)
                    nCodPais = nVal.getCodPais().pop(i)
                    nAno = nVal.getAno().pop(i)

                    nPais.getCodPais().remove(nCodPais)
                    nPais.getAno().remove(nAno)
                    nPais.getVal().remove(nVal)

                    nAno.getPais().remove(nPais)
                    nAno.getCodPais().remove(nCodPais)
                    nAno.getVal().remove(nVal)

                    nCodPais.getPais().remove(nPais)
                    nCodPais.getAno().remove(nAno)
                    nCodPais.getVal().remove(nVal)

                    self.verNode(nPais, nPais.getSizeData(), 'pais')
                    self.verNode(nCodPais, nCodPais.getSizeData(), 'codPais')
                    self.verNode(nAno, nAno.getSizeData(), 'ano')
                    self.verNode(nVal, nVal.getSizeData(), 'val')
                    i = 0
                    a-=1
                else:
                    i+=1

    def edit(self, pais = None, codPais = None, ano = None, val = None, novoPais = None, novoCodPais = None, novoAno = None, novoVal = None):
        l = []
        i = 0
        if pais:
            nPais = self.tPais.search(pais=pais)
            if nPais == None:
                return
            a = nPais.getSizeData()
            while i < a:
                eq = True
                if codPais and nPais.getCodPais()[i].getCodPais() != codPais:
                    eq = False

                if ano and nPais.getAno()[i].getAno() != ano:
                    eq = False

                if val and nPais.getVal()[i].getVal() != val:
                    eq = False

                if eq:
                    nCodPais = nPais.getCodPais().pop(i)
                    nAno = nPais.getAno().pop(i)
                    nVal = nPais.getVal().pop(i)
                    vl = self.subValues(nPais, nCodPais, nAno, nVal, novoPais, novoCodPais, novoAno, novoVal)

                    nCodPais.getPais().remove(nPais)
                    nCodPais.getAno().remove(nAno)
                    nCodPais.getVal().remove(nVal)

                    nAno.getPais().remove(nPais)
                    nAno.getCodPais().remove(nCodPais)
                    nAno.getVal().remove(nVal)

                    nVal.getPais().remove(nPais)
                    nVal.getCodPais().remove(nCodPais)
                    nVal.getAno().remove(nAno)

                    self.verNode(nPais, nPais.getSizeData(), 'pais')
                    self.verNode(nCodPais, nCodPais.getSizeData(), 'codPais')
                    self.verNode(nAno, nAno.getSizeData(), 'ano')
                    self.verNode(nVal, nVal.getSizeData(), 'val')
                    self.add(vl[0], vl[1], vl[2], vl[3])
                    i = 0
                    a -= 1
                else:
                    i += 1



        elif codPais:
            nCodPais = self.tCodPais.search(codPais=codPais)
            if nCodPais == None:
                return
            a = nCodPais.getSizeData()
            while i< a:
                eq = True

                if val and nCodPais.getVal()[i].getVal() == val:
                    eq = False

                if pais and nCodPais.getPais()[i].getPais() != pais:
                    eq = False

                if ano and nCodPais.getAno()[i].getAno() != ano:
                    eq = False

                if eq:
                    nPais = nCodPais.getPais().pop(i)
                    nAno = nCodPais.getAno().pop(i)
                    nVal = nCodPais.getVal().pop(i)
                    vl = self.subValues(nPais, nCodPais, nAno, nVal, novoPais, novoCodPais, novoAno, novoVal)
                    nPais.getCodPais().remove(nCodPais)
                    nPais.getAno().remove(nAno)
                    nPais.getVal().remove(nVal)

                    nAno.getPais().remove(nPais)
                    nAno.getCodPais().remove(nCodPais)
                    nAno.getVal().remove(nVal)

                    nVal.getPais().remove(nPais)
                    nVal.getCodPais().remove(nCodPais)
                    nVal.getAno().remove(nAno)

                    self.verNode(nPais, nPais.getSizeData(), 'pais')
                    self.verNode(nCodPais, nCodPais.getSizeData(), 'codPais')
                    self.verNode(nAno, nAno.getSizeData(), 'ano')
                    self.verNode(nVal, nVal.getSizeData(), 'val')
                    self.add(vl[0], vl[1], vl[2], vl[3])
                    i = 0
                    a-=1
                else:
                    i+=1

        elif ano:
            nAno = self.tAno.search(ano=ano)
            if nAno == None:
                return
            a = nAno.getSizeData()
            while i < a:
                eq = True

                if pais and nAno.getPais()[i].getPais() != pais:
                    eq = False

                if codPais and nAno.getCodPais()[i].getCodPais() != codPais:
                    eq = False

                if val and nAno.getVal()[i].getVal() != val:
                    eq = False

                if eq:
                    nPais = nAno.getPais().pop(i)
                    nCodPais = nAno.getCodPais().pop(i)
                    nVal = nAno.getVal().pop(i)
                    vl = self.subValues(nPais, nCodPais, nAno, nVal, novoPais, novoCodPais, novoAno, novoVal)
                    nPais.getCodPais().remove(nCodPais)
                    nPais.getAno().remove(nAno)
                    nPais.getVal().remove(nVal)

                    nCodPais.getPais().remove(nPais)
                    nCodPais.getAno().remove(nAno)
                    nCodPais.getVal().remove(nVal)

                    nVal.getPais().remove(nPais)
                    nVal.getCodPais().remove(nCodPais)
                    nVal.getAno().remove(nAno)

                    self.verNode(nPais, nPais.getSizeData(), 'pais')
                    self.verNode(nCodPais, nCodPais.getSizeData(), 'codPais')
                    self.verNode(nAno, nAno.getSizeData(), 'ano')
                    self.verNode(nVal, nVal.getSizeData(), 'val')
                    self.add(vl[0], vl[1], vl[2], vl[3])
                    i = 0
                    a -=1
                else:
                    i+=1

        elif val:
            nVal = self.tVal.search(val=val)
            if nVal == None:
                return
            a = nVal.getSizeData()
            while i < a:
                eq = True
                if (pais and nVal.getPais()[i].getPais() != pais):
                    eq = False
                if codPais and nVal.getCodPais()[i].getCodPais() != codPais:
                    eq = False
                if ano and nVal.getAno()[i].getAno() != ano:
                    eq = False

                if eq:
                    nPais = nVal.getPais().pop(i)
                    nCodPais = nVal.getCodPais().pop(i)
                    nAno = nVal.getAno().pop(i)
                    vl = self.subValues(nPais, nCodPais, nAno, nVal, novoPais, novoCodPais, novoAno, novoVal)
                    nPais.getCodPais().remove(nCodPais)
                    nPais.getAno().remove(nAno)
                    nPais.getVal().remove(nVal)

                    nAno.getPais().remove(nPais)
                    nAno.getCodPais().remove(nCodPais)
                    nAno.getVal().remove(nVal)

                    nCodPais.getPais().remove(nPais)
                    nCodPais.getAno().remove(nAno)
                    nCodPais.getVal().remove(nVal)

                    self.verNode(nPais, nPais.getSizeData(), 'pais')
                    self.verNode(nCodPais, nCodPais.getSizeData(), 'codPais')
                    self.verNode(nAno, nAno.getSizeData(), 'ano')
                    self.verNode(nVal, nVal.getSizeData(), 'val')
                    self.add(vl[0], vl[1], vl[2], vl[3])
                    i = 0
                    a-=1
                else:
                    i+=1

    def subValues(self, nPais, nCodPais, nAno, nVal, novoPais = None, novoCodPais = None, novoAno = None, novoVal = None):

        if novoPais:
            pais = novoPais
        else:
            pais = nPais.getPais()

        if novoCodPais:
            codPais = novoCodPais
        else:
            codPais = nCodPais.getCodPais()

        if novoAno:
            ano = novoAno
        else:
            ano = nAno.getAno()

        if novoVal:
            val = novoVal
        else:
            val = nVal.getVal()

        return (pais, codPais, ano, val)

    def removeNode(self, r, tName):
        if tName == 'pais':
            self.tPais.remover(r)
        elif tName == 'codPais':

            self.tCodPais.remover(r)
        elif tName == 'ano':
            self.tAno.remover(r)

        elif tName == 'val':
            self.tVal.remover(r)

    def getNodeVals(self, r, tName):
        s = ''
        if tName == 'pais':
            s = s + r.pais + ' ' + r.codPais.getCodPais() + ' ' + str(r.ano.getAno()) + ' ' + \
                str(r.val.getVal())
        elif tName == 'codPais':
            s = s + r.pais.getPais() + ' ' + r.codPais + ' ' + str(r.ano.getAno()) + ' ' + \
                str(r.val.getVal())
        elif tName == 'ano':
            s = s +  r.pais.getPais() + ' ' + r.codPais.getCodPais() + ' ' + str(r.ano) + ' ' + \
                str(r.val.getVal())
        elif tName == 'val':
            s = s + r.pais.getPais() + ' ' + r.codPais.getCodPais() + ' ' + str(r.ano.getAno()) + ' ' + \
                str(r.val)

        return s

    def printNodes(self, l, tName):

        if len(l) > 0:
            for r in l:
                print(r.printNode(tName))