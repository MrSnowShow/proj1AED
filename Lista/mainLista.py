import csv
from List import List


def readCsv(file):
    l = List()
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
        if('"' in inicio[i]):
            inicio[i] = inicio[i][1:-1]

    no = []
    for d in dados:
        nPais = d[0]
        if('"' in d[1]):
            d[1] = d[1][1:-1]
        code = d[1]
        s = 2
        while s < len(d):
            if(d[s] != ''):
                if ('"' in d[s]):
                    d[s] = d[s][1:-1]
                l.add(nPais, code, inicio[s], d[s])
            s += 1

    return l

def remover(l, pais=None, codPais=None, ano=None, val=None):
    l.remove(pais, codPais, ano, val)


def procurar(l, pais=None, codPais=None, ano=None, val=None):
    ls = []
    ls = l.search(pais, codPais, ano, val)

    if ls:
    	l.printNode(ls)


def inserir(l, pais, codPais, ano, val):
    l.add(pais, codPais, ano, val)


def editar(l, pais=None, codPais=None,  ano=None, val=None, npais=None, ncodPais=None, nano=None, nval=None):
    l.edit(pais, codPais, ano, val, npais, ncodPais, nano, nval)


def main():
    l = readCsv('dados.csv')
    while (1):
        print("0: Sair")
        print("1: Procurar")
        print("2: Inserir")
        print("3: Editar")
        print("4: Remover")
        option = eval(input("Insira a opcao que deseja: "))
        if option == 0:
            print("Programa terminado.")
            exit()
        elif option == 1:
            print("Para os seguintes pedidos preencha corretamente os dados que pretende ter como base da sua pesquisa e deixe em branco os restantes.")
            pais = str(input("Insira o pais: "))
            if pais == "":
                pais = None
            codigo = str(input("Insira o codigo: "))
            if codigo == "":
                codigo = None
            ano = str(input("Insira o ano: "))
            if ano == "":
                ano = None
            else:
                ano = int(ano)
            valor = str(input("Insira o valor: "))
            if valor == "":
                valor = None
            else:
                valor = float(valor)
            procurar(l=l, codPais=codigo, pais=pais, ano=ano, val=valor)
            print("\n(Resultados)\n")
        elif option == 2:
            print("Para os seguintes pedidos preencha corretamente os dados que pretende ter como base da sua pesquisa e deixe em branco os restantes.")
            pais = str(input("Insira o pais: "))
            if pais == "":
                pais = None
            codigo = str(input("Insira o codigo: "))
            if codigo == "":
                codigo = None
            ano = str(input("Insira o ano: "))
            if ano == "":
                ano = None
            else:
                ano = int(ano)
            valor = str(input("Insira o valor: "))
            if valor == "":
                valor = None
            else:
                valor = float(valor)
            inserir(l=l, codPais=codigo, pais=pais, ano=ano, val=valor)
            print("\nInserido.\n")
        elif option == 3:
            print("Para os seguintes pedidos preencha corretamente os dados que pretende ter como base da sua pesquisa e deixe em branco os restantes.")
            pais = str(input("Insira o pais: "))
            if pais == "":
                pais = None
            codigo = str(input("Insira o codigo: "))
            if codigo == "":
                codigo = None
            ano = str(input("Insira o ano: "))
            if ano == "":
                ano = None
            else:
                ano = int(ano)
            valor = str(input("Insira o valor: "))
            if valor == "":
                valor = None
            else:
                valor = float(valor)
            npais = str(input("Insira o novo pais: "))
            if npais == "":
                npais = None
            ncodigo = str(input("Insira o novo codigo: "))
            if ncodigo == "":
                ncodigo = None
            nano = str(input("Insira o novo ano: "))
            if nano == "":
                nano = None
            else:
                nano = int(nano)
            nvalor = str(input("Insira o novo valor: "))
            if nvalor == "":
                nvalor = None
            else:
                nvalor = float(nvalor)
            editar(l=l, codPais=codigo, pais=pais, ano=ano, val=valor, ncodPais=ncodigo, npais=npais, nano=nano,
                   nval=nvalor)
            print("\nAlterado.\n")
        elif option == 4:
            print("Para os seguintes pedidos preencha corretamente os dados que pretende ter como base da sua pesquisa e deixe em branco os restantes.")
            pais = str(input("Insira o pais: "))
            if pais == "":
                pais = None
            codigo = str(input("Insira o codigo: "))
            if codigo == "":
                codigo = None
            ano = str(input("Insira o ano: "))
            if ano == "":
                ano = None
            else:
                ano = int(ano)
            valor = str(input("Insira o valor: "))
            if valor == "":
                valor = None
            else:
                valor = float(valor)
            remover(l=l, codPais=codigo, pais=pais, ano=ano, val=valor)
            print("\nRemovido.\n")
        else:
            print("Insira uma opcao correta: ")
    
main()