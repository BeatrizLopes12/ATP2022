import matplotlib.pyplot as plt
import csv

filename = "/Users/beatrizlopes/Desktop/tpc/obras.csv"

def leObras(filename):
    file = open(filename, encoding="UTF8")
    file.readline()
    csv_file = csv.reader(file,delimiter=";")

    lista = []
    for obra in csv_file:
        lista.append(tuple(obra))
    return lista

    

def tamanhoObras(obras):#ponto1
    return len(obras)
    

def imprime(obras): #ponto2
    print(f"| {'Nome':20} | {'Descrição':25} | {'Ano':8} | {'Compositor':15} |")
    for nome, desc, ano, _, comp, *_ in obras:
        print(f"| {nome[:20]:20} | {desc[:25]:25} | {ano:8} | {comp[:15]:15} |")

def ordem(tuplo):
    return tuplo[0]


def titAno(obras): #ponto3
    lista = []
    for nome, _, ano, *_ in obras:
        lista.append((nome,ano))
    
    lista.sort(key=ordem)
    return lista


def titAno_2(obras): #ponto4
    lista = []
    for nome, _, ano, *_ in obras:
        lista.append((nome,ano))
    
    lista.sort(key= lambda tuplo: tuplo[1])
    return lista
    


def titporAno(obras):#ponto5
    dici = {}
    for nome, _, ano, *_ in obras:
        if ano in dici.keys():
            dici[ano].append(nome)
        else:
            dici[ano] = [nome]
    return dici


def ordenaCompositores(obras):#ponto6
    lista = []
    for _, _, _, _, compositor, *_ in obras:
        lista.append((compositor))
    
    lista.sort(key= lambda tuplo: tuplo[0])
    return lista
    

def distPeriodo(obras): #ponto 7
    dici = {}
    for _, _, _, periodo, *_ in obras:
        if periodo in dici.keys():
            dici[periodo] = dici[periodo] + 1
        else:
            dici[periodo] = 1
    return dici    

def distAno (obras): #ponto8
    dici2 = {}
    for _, _, ano, *_ in obras:
        if ano in dici2.keys():
            dici2[ano] = dici2[ano] + 1
        else:
            dici2[ano] = 1
    return dici2  

def distCompositores(obras): #ponto 9
    dici3 = {}
    for _, _, _, _, compositor, *_ in obras:
        if compositor in dici3.keys():
            dici3[compositor] = dici3[compositor] + 1
        else:
            dici3[compositor] = 1
    return dici3



def Grafico1(obras): #ponto 10
    
    dici=distPeriodo(obras)
    
    periodo = dici.keys()
    obras = dici.values()

    plt.bar(periodo, obras)
         
    plt.xlabel('periodo')

    plt.ylabel('obras')
     
    plt.title("Distribuicao das obras por periodo")
         
    plt.show()



def Grafico2(obras): #ponto11
    
    dici2 =distAno(obras)
    ano = dici2.keys()
    obras = dici2.values()

    plt.bar(ano, obras)
         
    plt.xlabel('ano')

    plt.ylabel('obras')
     
    plt.title("Distribuicao das obras por ano")
         
    plt.show()


def Grafico3(obras): #ponto12
    dici3=distCompositores(obras)
    
    compositor = dici3.keys()
    obras = dici3.values()

    plt.bar(compositor, obras)
         
    plt.xlabel('compositor')

    plt.ylabel('obras')
     
    plt.title("Distribuicao das obras por compositor")
         
    plt.show()

def inversãoEst (obras): #ponto 13
    dici = {}
    lista1=[]
  
    for nome, _, _,_,compositor, *_ in obras:
        if compositor in dici.keys():
            dici[compositor].append(nome)
        else:
            dici[compositor] = [nome]
    for keys,values in dici.items():
        lista1.append([keys] + [values])
    
   
    return lista1


