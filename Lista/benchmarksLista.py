import csv
import random
import matplotlib.pyplot as plt
from timeit import default_timer as timer
from List import List
from mainLista import readCsv
from mainLista import procurar, inserir, editar, remover

def readCountries(file):
    countries = []
    codes = []
    with open(file) as f:
        reader = csv.reader(f)
        for row in reader:
            for col in row:
                countries.append((col.split(';')[0]))
                codes.append((col.split(';')[1][1:4:])) # [1:4:] para tirar as aspas "PRT" --> PRT
    return (countries[1::], codes[1::])

def generateRandoms(l, countries):
    (testPais, testCod) = countries # Tuplo com paises em [0] e codigos em [1]
    
    randomIndex = random.randrange(0, len(testPais))
    randomPais = testPais[randomIndex]
    randomCod = testCod[randomIndex]
    
    auxListaPaises = l.search(randomPais, None, None, None)
    if (len(auxListaPaises) > 0):
        randomIndexPais = random.randrange(0, len(auxListaPaises))
        randomYear = auxListaPaises[randomIndexPais].getAno()    
        randomVal = l.search(randomPais, None, randomYear)[0].getVal()        
    else:
        randomYear = random.randrange(1960, 2016)
        randomVal = random.uniform(0, 100)
    return (randomPais, randomCod, randomYear, randomVal)
    
def timeProcurar(l, randoms):
    start = timer()
    procurar(l, pais=randoms[0], codPais=randoms[1], ano=randoms[2], val=randoms[3])
    end = timer()
    
    return (end-start)*1000

def timeInserir(l, randoms):
    randomYear = random.randrange(1960, 2016)
    randomVal = random.uniform(0, 100)
    
    start = timer()
    inserir(l, pais=randoms[0], codPais=randoms[1], ano=randomYear, val=randomVal)
    end = timer()
    
    return (end-start)*1000

def timeRemover(l, randoms):
    start = timer()
    remover(l, pais=randoms[0], codPais=randoms[1], ano=randoms[2], val=randoms[3])
    end = timer()
    
    return (end-start)*1000
        
def timeEditar(l, randoms):
    randVal = random.uniform(0, 100)
    
    start = timer()
    editar(l, pais=randoms[0], codPais=randoms[1], ano=randoms[2], val=randoms[3], nval=randVal)
    end = timer()

    return (end-start)*1000
        
def testing():
    l = readCsv('dados.csv')
    l2 = readCsv('dados.csv')
    l3 = readCsv('dados.csv')
    l4 = readCsv('dados.csv')
    tuploPaises = readCountries('dados.csv') # Usado como argumento para criar randoms
    
    temposPro = [0]
    temposIns = [0]
    temposRem = [0]
    temposEdi = [0]
    
    ciclos = 3000
    for i in range(ciclos):
        randoms = generateRandoms(l, tuploPaises)
        temposPro.append(temposPro[-1] + timeProcurar(l, randoms))
        temposIns.append(temposIns[-1] + timeInserir(l2, randoms))
        temposRem.append(temposRem[-1] + timeRemover(l3, randoms))
        temposEdi.append(temposEdi[-1] + timeEditar(l4, randoms))
        
    print("Tempo medio procurar() - ", temposPro[-1] / (len(temposPro)-1), "ms")
    print("Tempo medio inserir() - ", temposIns[-1] / (len(temposIns)-1), "ms")
    print("Tempo medio remover() - ", temposRem[-1] / (len(temposRem)-1), "ms")    
    print("Tempo medio editar() - ", temposEdi[-1] / (len(temposEdi)-1), "ms")   
    
    plt.plot(temposPro[1::], 'r-')
    plt.plot(temposIns[1::], 'g-')
    plt.plot(temposRem[1::], 'b-')
    plt.plot(temposEdi[1::], 'y-')
    plt.ylabel('Time (ms)')
    plt.xlabel('Operations (n)')
    plt.show()
    
testing()