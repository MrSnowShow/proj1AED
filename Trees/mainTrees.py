import csv
from mainRoot import MainRoot


def readCsv(file):
    l = MainRoot()
    f = csv.reader(open(file))
    i = 0
    a = []
    for d in f:
        a.append(d)

    dados = []
    for d in a:
        dados.append(d[0].split(';'))

    inicio = dados.pop(0)

    for i in range(len(inicio)):
        if ('"' in inicio[i]):
            inicio[i] = inicio[i][1:-1]

    no = []
    for d in dados:
        nPais = d[0]
        if ('"' in d[1]):
            d[1] = d[1][1:-1]
        code = d[1]
        s = 2
        while s < len(d):
            if (d[s] != ''):
                if ('"' in d[s]):
                    d[s] = d[s][1:-1]
                l.add(nPais, code, inicio[s], d[s])
            s += 1
    return l


def remover(l,pais=None, codPais=None, ano=None, val=None):
    if (not l.checkTreesEmpty()):
        l.remover(pais, codPais, ano, val)


def procurar(l, pais=None, codPais=None, ano=None, val=None):
    #ls = []
    (ls, tName) = l.search(pais, codPais, ano, val)

    if ls:
        print(ls.printNode(tName))


def inserir(l, pais, codPais, ano, val):
    l.add(pais, codPais, ano, val)


def editar(l,pais=None, codPais=None, ano=None, val=None, npais=None, ncodPais=None, nano=None, nval=None):
    l.edit(pais, codPais, ano, val, npais, ncodPais, nano, nval)


def main():
    l = readCsv('dados.csv')

    """
    print('\t\t\t*******Antes***********')
    procurar(l, pais = "Aruba", codPais = None, ano = None, val = None)
	"""

main()
