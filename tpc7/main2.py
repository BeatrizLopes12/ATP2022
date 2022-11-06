#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 09:56:59 2022

@author: beatrizlopes
"""

import alunos

myAlunos = alunos.leAlunos("/Users/beatrizlopes/Desktop/tpc7/alunos.csv")
def menu(): 

        
        
    
    opcao = input ('''
        Introduza o que que pretende ver: 
                          
                          2 - Ver a distribuição de alunos por curso
                          3 - calcular a média das notas de cada aluno e acrescentar essa nova coluna no dataset em memória
                          4 - Ver a divisao por escaloes
                          5 - Ver a distribuição dos alunos por escaloes
                          6 - Ver o grafico de uma distribuição
                          7 - Ver a tabela de uma distribuição
                          
                        
                         ''')
         
    return str(opcao)   



def opcoes():
   
    opcao="25"
    
    
    while opcao != "0" :
        opcao= menu()
        
            
        if opcao=="2":
            dist_curso= alunos.distCurso(myAlunos)
            print(dist_curso)
            
        elif opcao=="3":
            lista = alunos.media(myAlunos)
            
            print(lista)
        
        elif opcao=="4":
            
           esc = alunos.escaloes(myAlunos)
           print(esc)
            
         
        elif opcao=="5":
            esca =alunos.dist_escalao(myAlunos)
            print(esca)
            
           
        
        elif opcao=="6":
            grafico= alunos.Grafico1(myAlunos)
            print(grafico)
        
            
        elif opcao =="7":
            tabela= alunos.tabela(myAlunos)
            print(tabela)
      
            
        
        
opcoes()    
        
        
        
        
        
        
        
        
            
        