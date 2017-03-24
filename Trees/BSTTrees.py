import sys
from Tnodes import TNode

class bst:

    def __init__(self, name):
        self.name = name
        self.root = None

    def getTName(self):
        return self.name

    def insere(self, n):

        if not self.root:
            self.root = n
            return n
        else:
            return self.add(n)

    def search(self, pais = None, codPais = None, ano = None, val = None):

        root = self.root
        tName = self.name
        if pais:
            key= pais
            pais = None
        elif codPais:
            key=codPais
            codPais = None
        elif ano:
            key=ano
            ano = None
        elif val:
            key = val
            val = None

        while root:
            if self.cmp(tName, root, key) == 0:
                return root
            if self.cmp(tName, root, key) < 0:
                root = root.getLeft()
            else:
                root = root.getRight()

    def strCmp(sefl, str1, str2):

        if str1 == str2:
            return True
        return False

    def cmp(self, tName, node, key):
        if tName == 'pais':

            if node.getPais() > key:
                return -1
            elif node.getPais() < key:
                return 1
            else:
                return 0

        elif tName == 'codPais':
            if node.getCodPais() > key:
                return -1
            elif node.getCodPais() < key:
                return 1
            else:
                return 0
        elif tName == 'ano':
            if node.getAno() > key:
                return -1
            elif node.getAno() < key:
                return 1
            else:
                return 0
        elif tName == 'val':
            if node.getVal() > key:
                return -1
            elif node.getVal() < key:
                return 1
            else:
                return 0

    def treeCmp(self, tName, node, tNode):

        if tName == 'pais':
            if node.getPais() < tNode.getPais():
                return -1
            elif node.getPais() > tNode.getPais():
                return 1
            else:
                return 0

        elif tName == 'codPais':
            if node.getCodPais() < tNode.getCodPais():
                return -1
            elif node.getCodPais() > tNode.getCodPais():
                return 1
            else:
                return 0
        elif tName == 'ano':
            if node.getAno() < tNode.getAno():
                return -1
            elif node.getAno() > tNode.getAno():
                return 1
            else:
                return 0
        elif tName == 'val':
            if node.getVal() < tNode.getVal():
                return -1
            elif node.getVal() > tNode.getVal():
                return 1
            else:
                return 0

    def add(self, no):

        root = self.root
        tName = self.name
        while root != None:

            if self.treeCmp(tName, no, root) < 0:
                if root.getLeft():
                    root = root.getLeft()
                else:
                    no.setParent(root)
                    root.setLeft(no)
                    return no
            elif self.treeCmp(tName, no, root) > 0:
                if root.getRight():
                    root = root.getRight()
                else:
                    no.setParent(root)
                    root.setRight(no)
                    return no
            elif self.treeCmp(tName, no, root) == 0:
                return root

    def getRoot(self):
        return self.root

    def remover(self, r):

        if r.getLeft() == r.getRight() == None:

            if r.getParent().getLeft() == r:

                r.getParent().setLeft(None)
            else:

                r.getParent().setRight(None)
        elif r.getLeft():

            if r.getParent().getLeft() == r:

                r.getLeft().setParent(r.getParent())
                r.getParent().setLeft(r.getLeft())
            elif r.getParent().getRight() == r:

                r.getLeft().setParent(r.getParent())
                r.getParent().setRight(r.getLeft())
            else:

                lf = r.getLeft()
                r.setLeft(None)
                self.replace(lf, r)

        elif r.getRight():

            if r.getParent().getLeft() == r:
                r.getRight().setParent(r.getParent())
                r.getParent().setLeft(r.getRight())

            elif r.getParent().getRight() == r:
                r.getRight().setParent(r.getParent())
                r.getParent().setRight(r.getRight())
            else:
                lf = r.getRight()
                r.setRight(None)
                self.replace(lf, r)
        else:
            subs = self.sub(r)
            self.removeSub(subs)
            r.setPais(subs.getPais())
            r.setCodPais(subs.getCodPais())
            r.setAno(subs.getAno())
            r.setVal(subs.getVal())

    def sub(self, node):

        subs = None

        if node.getRight():
            subs = node.getRight()
            while subs.getLeft():
                subs = subs.getLeft()

        return subs

    def removeSub(self, r):

        if not (r.getLeft() and r.getRight()):

            if r.getParent().getLeft() == r:

                r.getParent().setLeft(None)
            else:
                r.getParent().setRight(None)
        elif r.getLeft():

            if r.getParent().getLeft() == r:

                r.getLeft().setParent(r.getParent())
                r.getParent().setLeft(r.getLeft())
            elif r.getParent().getRight() == r:

                r.getLeft().setParent(r.getParent())
                r.getParent().setRight(r.getLeft())
            else:

                lf = r.getLeft()
                r.setLeft(None)
                self.replace(lf, r)

        else:

            if r.getParent().getLeft() == r:

                r.getRight().setParent(r.getParent())
                r.getParent().setLeft(r.getRight())

            elif r.getParent().getRight() == r:

                r.getRight().setParent(r.getParent())
                r.getParent().setRight(r.getRight())
            else:

                rg = r.getRight()
                r.setRight(None)
                self.replace(rg, r)

    def replace(self, fromNode, toNode):

        toNode.setPais(fromNode.getPais())
        toNode.setCodPais(fromNode.getCodPais())
        toNode.setAno(fromNode.getAno())
        toNode.setVal(fromNode.getVal())
        toNode.setParent(fromNode.getParent())
        toNode.setLeft(fromNode.getLeft())
        toNode.setRight(fromNode.getRight())
        if toNode.getLeft():
            toNode.getLeft().setParent(toNode)
        if toNode.getRight():
            toNode.getRight().setParent(toNode)



