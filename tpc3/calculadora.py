#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 19:03:39 2022

@author: beatrizlopes
"""
import random

lista=[]

    
def menu(): 
    print ("Bem-vindo à calculadora.")
        
        
    
    operacao = input ('''
        Introduza o tipo de operação que pretende efetuar: 
                          1 para criar lista
                          2 para ler lista
                          3 para fazer soma
                          4 para fazer a média
                          5 para ver o maior elemento da lista 
                          6 para ver o menor elemento da lista
                          7 para ver se a lista esta por ordem crescente
                          8 para ver se a lista esta por ordem decrescente
                          9 encontrar um elemento na lista
                          0 para sair
                         
                         ''')
         
    return str(operacao)                        
      
def op1():
       
        global lista
        N= int(input("Introduza o numero de elementos que quer na lista: "))
        
        i= 0
        while i < N:
            numero=random.randint (1,101)
            lista.append(numero)
            i=i+1
        print("\n")
        print ("A lista é a seguinte: ", lista)
        print("\n")
     
def op2():
    
    
    global lista
    lista=[]
    N= int(input("Introduza quantos numeros quer colocar na lista: "))
    for i in range (0,N):
        numeros= int(input("introduza um numero: "))
        lista.append(numeros)
    print ("\n")
    print ("A lista é a seguinte:", lista)     
    print ("\n")

def op3():
    
    global lista 
    if lista==[]:
        print("primeiro crie uma lista de numeros. Selecione operacao 1 ou 2 antes da soma.")
    
    else:
        
        soma = 0
        for numero in lista:
            soma += numero
        print ("A soma é ", soma)
    print ("\n")

def op4():
   
    
    global lista
    if lista==[]:
        print("primeiro crie uma lista de numeros. Selecione operacao 1 ou 2 antes da media.")
    else:
        soma = 0
        for numero in lista:
            soma += numero
            media= soma/len(lista)
        print ("a media é", media)
    print ("\n")

def op5():
    global lista
    if lista==[]:
        print("primeiro crie uma lista de numeros. Selecione operacao 1 ou 2 antes do maximo.")
        
    else:
        maximo = lista[0] 
          
        for x in lista: 
                           
            if x > maximo: 
                               
                maximo = x 
        print ("o maximo é" , maximo)
    print ("\n")

def op6():
    global lista
    if lista==[]:
        print("primeiro crie uma lista de numeros. Selecione operacao 1 ou 2 antes do minimo.")
    
    else:
    
        minimo = lista[0] 
          
        for x in lista: 
                           
            if x < minimo: 
                               
                minimo = x 
        print( "O minimo é", minimo)
    print ("\n")

def op7():
    global lista
    x= True
    if lista==[]:
        print("primeiro crie uma lista de numeros. Selecione operacao 1 ou 2.")
    else:
        maximo= lista[0]
        for i in lista:
            if i < maximo:
                x = False
            maximo=i
        if x == True:
            print("Sim")
        else:
            print("Não")
    print( "\n")

def op8():
    global lista
    x= True
    if lista==[]:
        print("primeiro crie uma lista de numeros. Selecione operacao 1 ou 2.")
    else:
        minimo= lista[0]
        for i in lista:
            if i > minimo:
                x = False
            minimo=i
        if x == True:
            print("Sim")
        else:
            print("Não")
        print( "\n")

def op9():
    
    global lista
    if lista==[]:
        print("primeiro crie uma lista de numeros. Selecione operacao 1 ou 2.")
    
        
    
    else:
        print ("A lista no momento é ", lista)
        
        h=int(input("Qual o número a procurar:"))
        print ("\n")
        if h not in lista:
            print (" O numero não está na lista.")
        else:
            for i in lista:
                          
               
                posicao=-1
                for t in range(len(lista)):
                    if lista[t]==h: 
                      posicao=t
        print("O numero", h ,"esta na posição numero ", posicao)
    print("\n")
   
                                                        
    
     
def calculadora():
   
    operacao="10"
    
    
    while operacao != "0" :
        operacao= menu()
        
        if operacao=="1":
            op1()
        elif operacao=="2":
            
            op2()
        elif operacao=="3":
            op3()
        elif operacao=="4":
            op4()
        elif operacao=="5":
            op5()
        elif operacao=="6":
            op6()
        elif operacao=="7":
            op7()
        elif operacao=="8":
            op8()
        elif operacao=="9":   
            op9()
    print("A lista guardada é", lista) 
    print ("Adeus!")    
    
   
calculadora()    

    
      
                 
            
           

     

            
       
          
           

             
                
