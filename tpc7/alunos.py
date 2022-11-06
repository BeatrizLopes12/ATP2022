#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 09:25:32 2022

@author: beatrizlopes
"""

import matplotlib.pyplot as plt
import csv

filename = "/Users/beatrizlopes/Desktop/tpc7/alunos.csv"

def leAlunos(filename):  #ponto1
    file = open(filename, encoding="UTF8")
    file.readline()
    csv_file = csv.reader(file,delimiter=",")

    lista = []
    for aluno in csv_file:
        lista.append(tuple(aluno))
    return lista

def distCurso(alunos): #ponto 2
    dici = {}
    for _, _, curso, *_ in alunos:
        if curso in dici.keys():
            dici[curso] = dici[curso] + 1
        else:
            dici[curso] = 1
    return dici

def media(alunos): #ponto 3
    
    
    lista= []
    soma=0

    for aluno in alunos:
        
        soma= int(aluno[3]) + int(aluno[4]) + int(aluno[5]) + int(aluno[6])
        media = (soma/4)
        m=str(media)
        a= (*aluno,m)
    
            
        
        lista.append(a)
   
    alunos= lista
  
     
    return alunos

    
def escaloes(al):
    
    alunos= media(al)
    lista=[]
    
        
    for aluno in alunos:
      
            
        if (float(aluno[7]) >= 1 and float(aluno[7]) <=4.99):
            Esc= "E" 
        elif (float(aluno[7]) >= 5 and float(aluno[7]) <=8.99):
            Esc="D"
                
        elif (float(aluno[7]) >= 9 and float(aluno[7]) <=12.99):
            Esc= "C"
                
        elif (float(aluno[7]) >= 13 and float(aluno[7]) <=16.99):
            Esc="B"
                
        elif (float(aluno[7]) >= 17 and float(aluno[7]) <=20):
            Esc="A"
            
        a=(*aluno,Esc)
        lista.append(a)
    
    alunos=lista
    return(alunos)


def dist_escalao(al):
    
    alunos= escaloes(al)
    dici = {}
   
    for _, _, _, _, _, _, _, _, Esc in alunos:
        
        if Esc in dici.keys():
            dici[Esc] = dici[Esc] + 1
        else:
            dici[Esc] = 1
    
    return dici
            

def Grafico1(alunos): #ponto 6 

#distribuição de alunos por curso
    
    dici=distCurso(alunos)
    
    curso = dici.keys()
    alunos = dici.values()

    plt.plot(curso, alunos)
         
    plt.xlabel('curso')

    plt.ylabel('alunos')
     
    plt.title("Distribuicao de alunos por curso")
         
    plt.show()
    

def tabela(alunos):
    
    #tabela da distribuição de alunos por curso
    dici=distCurso(alunos)
    print("curso alunos")
    
    for i in dici:
        print("{}\t{}".format(i,dici[i]))
        

    
