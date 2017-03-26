import csv
import sys
from BST import bst

def readCsv(file):
    l = bst()
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
                l.insere(nPais, code, inicio[s], d[s])
            s += 1
    return l


def remover(l, pais = None, codPais = None, ano = None, val = None):
    l.remover(pais, codPais, ano, val)

def procurar(l, pais = None, codPais = None, ano = None, val = None):
    ls = []
    ls = l.search(pais, codPais, ano, val)
    for r in ls:
        print(r.printNode())

def inserir(l, pais, codPais, ano, val):
    l.insere(pais, codPais, ano, val)

def editar(l, pais = None, codPais = None, ano = None, val = None, npais = None, ncodPais = None, nano = None, nval = None):

    l.edit(pais, codPais, ano, val, ncodPais, npais, nano, nval)


def main():

    l = readCsv('dados.csv')

    print('\t\t\t*******Antes***********')
    procurar(l, pais ="Portugal", codPais = None, ano = None, val = None)

    #procurar(l, pais = None, codPais = None, ano = None, val = None)
    #inserir(l, "Northern Mariana Islands", "MLTA", 2017, 200)
    #remover(l, pais = None, codPais="PRT", ano = None, val = None)
    editar(l, pais = "Portugal", codPais = "PRT", ano = 2000, val = 100, npais = None, ncodPais = None, nano = None, nval = 50)
    print('\t\t\t***********Depois*********')
    procurar(l, pais = None, codPais = "PRT", ano = None, val = None)

    print('*******************')
    

main()