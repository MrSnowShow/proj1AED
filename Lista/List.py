from Node import Node

class List:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head

        i = 0

        while(current != None):
            i+=1

            current = current.getNext()
        return i

    def remove(self, pais = None, codPais = None, ano = None, val = None):

        current = self.head
        previous = None
        igual = False

        if(current == None):
            return False

        while(current != None):

            if pais:
                if current.getPais() == pais:
                    igual = True
                else: igual = False

            if codPais:
                if current.getCodPais() == codPais:
                    igual = True
                else: igual = False
            if ano:
                if current.getAno() == ano:
                    igual = True
                else:
                    igual = False
            if ano:
                if current.getVal() == val:
                    igual = True
                else:
                    igual = False
            if igual:
                if (previous == None):
                    self.head = current.getNext()
                else:
                    previous.setNext(current.getNext())

            previous = current
            current = current.getNext()
        return False

    def add(self, pais, codPais, ano, val):

        temp = Node(pais, codPais, ano, val)
        current = self.head
        previous = None
        if(current == None):
            self.head = temp
            return True

        while current != None and current.getPais() < pais:
            previous = current
            current = current.getNext()

        if(previous == None):
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(previous.getNext())
            previous.setNext(temp)
        return True

    def searchPais(self, lNode, pais):
        l = []
        if len(lNode) > 0:
           for current in lNode:
               if current.getPais() == pais:
                   l.append(current)
        else:
            current = self.head
            while current != None and (current.getPais() <= pais):
                if current.getPais() == pais:
                    l.append(current)
                current = current.getNext()
        return l



    def searchCodPais(self, lNode, codPais):
        l = []
        if len(lNode) > 0:
           for current in lNode:
               if current.getCodPais() == codPais:
                   l.append(current)
        else:
            current = self.head
            while current != None:
                if current.getCodPais() == codPais:
                    l.append(current)
                current = current.getNext()
        return l


    def searchAno(self, lNode, ano):
        l = []
        if len(lNode) > 0:
            for current in lNode:
                if current.getAno() == ano:
                    l.append(current)
        else:
            current = self.head
            while current != None:
                if current.getAno() == ano:
                    l.append(current)
                current = current.getNext()

        return l


    def searchVal(self, lNode, val):
        l = []
        if len(lNode) > 0:
            for current in lNode:
                if current.getVal() == val:
                    l.append(current)
        else:
            current = self.head
            while current != None:
                if current.getVal() == val:
                    l.append(current)
                current = current.getNext()


        return l


    def search(self, pais = None, codPais = None, ano = None, val = None):

        lNode = []

        if pais:
            lNode = self.searchPais(lNode, pais)
            if len(lNode) == 0:
                return lNode

        if codPais:
            lNode = self.searchCodPais(lNode, codPais)
            if len(lNode) == 0:
                return lNode

        if ano:
            lNode = self.searchAno(lNode, ano)
            if len(lNode) == 0:
                return lNode

        if val:
            lNode = self.searchVal(lNode, val)
            if len(lNode) == 0:
                return lNode

        return lNode


    def printNode(self, lNode):

        for node in lNode:
            if node:
                print('**********')
                print('')
                print('Pais: ', node.getPais())
                print('Código: ', node.getCodPais())
                print('Ano: ', node.getAno())
                print('Taxa: ', node.getVal())


    def printList(self):
        current = self.head
        while current != None:
            print('**********')
            print('')
            print('Pais: ', current.getPais())
            print('Código: ', current.getCodPais())
            print('Ano: ', current.getAno())
            print('Taxa: ', current.getVal())

            current = current.getNext()


    def edit(self, pais = None, codPais = None, ano = None, val = None, nPais = None, nCodPais = None, nAno = None, nVal = None):
        ls = self.search(pais, codPais, ano, val)
        for n in ls:
            if nPais:
                pais = nPais
            else:
                pais = n.getPais()

            if nCodPais:
                codPais = nCodPais
            else:
                codPais = n.getCodPais()

            if nAno:
                ano = nAno
            else:
                ano = n.getAno()

            if nVal:
                val = nVal
            else:
                val=n.getVal()

            self.remove(n.getPais(), n.getCodPais(), n.getAno(), n.getVal())
            self.add(pais, codPais, ano, val)