#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 14:35:58 2022

@author: beatrizlopes
"""

import obras

myObras = obras.leObras("/Users/beatrizlopes/Desktop/tpc/obras.csv")
def menu(): 

        
        
    
    opcao = input ('''
        Introduza o que que pretende ver: 
                          1 - para ver quantas obras existem catalogadas 
                          2 - para imprimir no monitor uma tabela com o título da obra, a sua descrição, o seu compositor e ano de criação
                          3 - para ordenar alfabeticamente as obras
                          4 - para ordenar as obras por ano
                          5 - para produzir um dicionário em que cada ano tem a ele associado a lista de títulos a ele associado;
                          6 - mostrar uma lista ordenada dos compositores
                          7 - mostrar a distribuição das obras por periodo
                          8 - mostrar a distribuição das obras por ano
                          9 - mostrar a distribuição das obras por compositor
                          10 - grafico da distribuição das obras por periodo
                          11 - grafico da distribuição das obras por ano
                          12 - grafico da distribuição das obras por compositor
                          13 - lista dos compositores em que cada compositor tem a ele associado uma lista dos títulos das obras que compôs;
                        
                         ''')
         
    return str(opcao)   



def opcoes():
   
    opcao="25"
    
    
    while opcao != "0" :
        opcao= menu()
        
        if opcao=="1":
          resultado=obras.tamanhoObras(myObras)
          print(resultado)
            
            
        elif opcao=="2":
            resultado= obras.imprime(myObras)
            print(resultado)
            
        elif opcao=="3":
            lista = obras.titAno(myObras)
            print(lista)
        
        elif opcao=="4":
            titulosPorAno = obras.titAno_2(myObras)
            print (titulosPorAno)
         
        elif opcao=="5":
            
            dist = obras.titporAno(myObras)
            print(dist)
        
        elif opcao=="6":
            lista= obras.ordenaCompositores(myObras)
            print(lista)
                
            
        elif opcao =="7":
            dist_periodo = obras.distPeriodo(myObras)
            print(dist_periodo)
        
        
        elif opcao =="8":  
            dist_ano = obras.distAno(myObras)
            print(dist_ano)
        
        elif opcao =="9": 
            dist_compositor = obras.distCompositores(myObras)
            print(dist_compositor)
        
        elif opcao =="10":
            grafico= obras.Grafico1(myObras)
            print(grafico)
        
        elif opcao =="11":
            grafico= obras.Grafico2(myObras)
            print(grafico)
        
        elif opcao =="12":
            grafico= obras.Grafico3(myObras)
            print(grafico)
        
        elif opcao =="13":
            resultado= obras.inversãoEst(myObras)
            print(resultado)
            
        
        
opcoes()    
        
        
        
        
        
        
        
        
            
        