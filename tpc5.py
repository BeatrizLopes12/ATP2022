#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 09:53:40 2022

@author: beatrizlopes
"""
import matplotlib.pyplot as plt
def Guardarficheiro():
   #converti o ficheiro de csv para txt
   ficheiro = open("myheart.txt", "r")
   lista = []
   lista2=[]
   for palavras in ficheiro.read().split("\n"):
       lista.append (palavras)
   lista.pop(0)
   
      
   ficheiro.close()
   
   for caso in lista:
       valor= caso.split(",")
       lista2.append(valor)
   print (lista2)
   return lista2    
       
       
   # print (lista)


def sexo (lista):
    distribuicao = {}
    #contadortotal=0
    contadorM=0
    contadorF=0
    #contadortotalM=0
    #contadortotalF=0
    for caso in lista:
     
        if caso[1] == 'M' :
    
            if caso[5]== '1':
                contadorM= contadorM + 1
                
        
        elif caso[1] == 'F' :

              if caso[5]== '1':
                  contadorF= contadorF + 1
  
    
                
    distribuicao['M']=contadorM  
    distribuicao['F']=contadorF 
   
   
    
   
    sexo = distribuicao.keys()
    valores = distribuicao.values()

    plt.bar(sexo, valores)
     
    plt.xlabel('sexo')

    plt.ylabel('Número de doentes')
 
    plt.title('distribuicao da doença por sexo')
     
    plt.show()
    
    return distribuicao
    
lista= Guardarficheiro()
sexo(lista)   
distribuicao=sexo(lista)


def idade (lista):
    distribuicao2 = {}
   
    contador1=0
    contador2=0
    contador3=0
    contador4=0
    contador5=0

    for caso in lista:
        c = int(caso[0])
        
        if c >= 30 and c <= 40 :
            contador1= contador1 + 1
        
        elif c >= 41 and c <= 50 :
            contador2= contador2 + 1
            
        elif c >= 51 and c <= 60 :
            contador3= contador3 + 1
            
        elif c >= 61 and c <= 70 :
            contador4= contador4 + 1
            
        elif c >= 71 and c <=80 :
            contador5= contador5 + 1
                 
    distribuicao2['30-40']=contador1  
    distribuicao2['41-50']=contador2
    distribuicao2['51-60']=contador3
    distribuicao2['61-70']=contador4
    distribuicao2['71-80']=contador5
    
    #print ("A percentagem de distribuicao masculina é ",distribuiçaoM, "‰")
    #print ("A percentagem de distribuicao feminina é ",distribuiçaoF, "‰" )
   
   
    sexo = distribuicao2.keys()
    valores = distribuicao2.values()

    plt.bar(sexo, valores)
     
    plt.xlabel('Escaloes')

    plt.ylabel('Número de doentes')
 
    plt.title('Distribuicao da doença por escaloes')
     
    plt.show()
    
    return distribuicao2
    
    
distribuicao2= idade(lista)    
def colesterol(lista):
    distribuicao3 = {}
       
    contador1=0
    contador2=0
    contador3=0
    contador4=0
    contador5=0
    contador6=0
    contador7=0
    contador8=0
    contador9=0
    

    for caso in lista:
           c = int(caso[3])
            
           if c >= 100 and c <= 199 :
               contador1= contador1 + 1
            
           elif c >= 200 and c <= 299 :
                 contador2= contador2 + 1
                
           elif c >= 300 and c <= 399 :
                 contador3= contador3 + 1
                
           elif c >= 400 and c <= 499 :
                 contador4= contador4 + 1
                
           elif c >= 500 and c <=599 :
                 contador5= contador5 + 1
                
           elif c >= 600 and c <=699 :
                 contador6= contador6 + 1  
                
           elif c >= 700 and c <=799 :
                 contador7= contador7 + 1
            
           elif c >= 800 and c <=899 :
                 contador8= contador8 + 1
            
           elif c >= 900 and c <=999 :
                 contador8= contador8 + 1
            
           elif c >= 1000 and c <=1999 :
                 contador9= contador9 + 1
    #nivel = N           
    distribuicao3['N1 ']=contador1  
    distribuicao3['N2 ']=contador2
    distribuicao3['N3 ']=contador3
    distribuicao3['N4 ']=contador4
    distribuicao3['N5 ']=contador5
    distribuicao3['N6 ']=contador5
    distribuicao3['N7 ']=contador5
    distribuicao3['N8 ']=contador5
    distribuicao3['N9 ']=contador5
    distribuicao3['N10 ']=contador5
        
    sexo = distribuicao3.keys()
    valores = distribuicao3.values()

    plt.bar(sexo, valores)
         
    plt.xlabel('Escaloes')

    plt.ylabel('Número de doentes')
     
    plt.title('Distribuicao do colesterol por escaloes')
         
    plt.show()
    
    return distribuicao3     
    
distribuicao3= colesterol(lista)

def tabela(distribuicao):
    
    print("sexo valor")
    
    for i in distribuicao:
        print("{}\t{}".format(i,distribuicao[i]))
    
tabela(distribuicao)

def menu(): 

        
        
    
    operacao = input ('''
        Introduza a tabela que pretende ver: 
                          1 para ver tabela da distribuição da doeça por sexo
                          2 para ver tabela da distribuição da doeça por idade
                          3 para ver tabela da distribuição da doeça por niveis de colesterol
                        
                         ''')
         
    return str(operacao)   


def tabela(distribuicao):
    
    print("sexo valor")
    
    for i in distribuicao:
        print("{}\t{}".format(i,distribuicao[i]))
    

                     

def tabelas():
   
    operacao="10"
    
    
    while operacao != "0" :
        operacao= menu()
        
        if operacao=="1":
            tabela(distribuicao)
        elif operacao=="2":
            
            tabela(distribuicao2)
        elif operacao=="3":
            tabela(distribuicao3)
       
        
   
tabelas()    

