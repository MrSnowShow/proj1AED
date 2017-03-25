import sys
from Tnode import TNode

class bst:

    def __init__(self):
        self.root = None

    def insere(self, pais, codPais, ano, val):
        n = TNode(pais, codPais, ano, val)

        if not self.root:
            self.root = n
        else:
            self.add(n)

    def searchCodPais(self, l, codPais):
        root = self.root
        while root:

            if root.getCodPais() == codPais:
                l.append(root)

            if codPais < root.getCodPais():
                root = root.getLeft()
            else:
                root = root.getRight()

        return l

    def cmp(self, r, pais = None, ano = None, val = None):
        eq = True

        if pais and r.getPais() != pais:
            eq = False
        if ano and r.getAno() != ano:
            eq = False
        if val and r.getVal() != val:
            eq = False

        return eq

    def searchAll(self, l, pais = None, ano = None, val = None):
        ls = []
        eq = False

        if len(l) > 0:
            for r in l:

                if self.cmp(r, pais, ano, val):
                    ls.append(r)
        else:
            ls = self.doSearch(self.root, pais, ano, val)
        return ls

    def doSearch(self, root, pais = None, ano = None, val = None):
        sys.setrecursionlimit(10000)
        l = []
        if root:
            l = self.doSearch(root.getLeft(), pais, ano, val)

            if self.cmp(root, pais, ano, val):
                l.append(root)

            l = l + self.doSearch(root.getRight(), pais, ano, val)
        return l

    def search(self, codPais = None, pais = None, ano = None, val = None):
        l = []

        if codPais:
            l = self.searchCodPais(l, codPais)


        if pais or ano or val:
            l = self.searchAll(l, pais, ano, val)

        return l

    def add(self, no):

        root = self.root

        while root != None:

            if no.getCodPais() < root.getCodPais():
                if root.getLeft():
                    root = root.getLeft()
                else:
                    no.setParent(root)
                    root.setLeft(no)
                    return
            else:
                if root.getRight():
                    root = root.getRight()
                else:
                    no.setParent(root)
                    root.setRight(no)
                    return
        return

    def getRoot(self):
        return self.root

    def edit(self, codPais = None, pais = None, ano = None, val = None, ncodPais = None, npais = None, nano = None, nval = None):

        l = []

        l = self.search(codPais, pais, ano, val)


        if len(l) > 0:
            for r in l:
                self.removeNode(r)
                if ncodPais:
                    r.setCodPais(ncodPais)

                if npais:
                    r.setPais(npais)

                if nano:
                    r.setAno(nano)

                if nval:
                    r.setVal(nval)



                self.insere(r.getPais(), r.getCodPais(), r.getAno(), r.getVal())

            return True
        return False

    def removeNode(self, r):
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

    def remover(self, codPais = None, pais = None, ano = None, val = None):

        l = []

        l = self.search(codPais, pais, ano, val)

        for r in l:

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




