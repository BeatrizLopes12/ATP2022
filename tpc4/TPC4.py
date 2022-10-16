#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 22:11:13 2022

@author: beatrizlopes
"""




def listarfilmes(salas):
    for i in salas:
        nlugares, ocupados, nomef = i
        print("Para ver o filme", nomef, "temos:")
        print("A sala tem ",nlugares, "cadeiras")
        ocupados.sort()
        print("Existem ", nlugares-len(ocupados), " lugares disponiveis. Lista de lugares ocupados: ", ocupados )
        print("")



def disponivel(salas,nomefilme,lugar):
    var1= True
    var2 = True
    for i in salas:
       nlugares, ocupados, nomef = i
       if nomef == nomefilme:
           if lugar > nlugares:
               print("o lugar", lugar,"da sala com o filme ", nomef,"nao existe")
               var2 = False
           else:
               if lugar in ocupados:
                   var1 = False
    if var1 == True:
           print("o lugar", lugar,"da sala com o filme ", nomef,"encontra-se disponivel")
    else:
    	   print("o lugar", lugar,"da sala com o filme" , nomef,"encontra-se indisponivel escolha outro")
    	   var2 = False
    return var2


   
def vendebilhete(salas,nomefilme,lugar):
    dis = disponivel(salas,nomefilme,lugar)
    if dis == True:
        for i in salas:
            nlugares, ocupados, nomef = i
            if nomef == nomefilme:
                ocupados.append(lugar)
                ocupados.sort()
                print("Os lugares ocupados sao:", ocupados)
        print("")
    else:
        for i in salas:
            nlugares, ocupados, nomef = i
            if nomef == nomefilme:
                print("Os lugares ocupados sao:", ocupados)
    return ocupados
 

def listardisponibilidades(salas):
	for i in salas:
		nlugares, ocupados, nomef = i
		print("\n A sala do filme ",nomef, " tem ", nlugares-len(ocupados)," lugares disponiveis")
	return salas

def inserirsala(salas,nomefilme,lugar):
	sala = (lugar, [], nomefilme)
	salas.append(sala)
    #return salas
    #print("OOO:", salas)

lugaresocupados1 = [1,5,6,4,2]
lugaresocupados2 = [1,3,4,5,10,7]
lugaresocupados3 = [3,5]
lugaresocupados4 = [15, 16, 17, 21, 8, 5, 7]
sala1 = (8, lugaresocupados1, "Harry Potter e a pedra filosofal")
sala2 = (10, lugaresocupados2, "Mary poppins")
sala3 = (5, lugaresocupados3, "101 Dalmatas")
sala4 = (20, lugaresocupados4, "Bela Adromecida")
salas = [sala1, sala2, sala3, sala4]

#f1
listarfilmes(salas)
#f2
vendebilhete(salas,"101 Dalmatas",1)
vendebilhete(salas,"Bela Adromecida",15)
#f3
listardisponibilidades(salas)

#f4
inserirsala(salas, "Duna",70)





def menu ():
    print ("""
    (1) Listar filmes
    (2) Lugares disponiveis
    (3) Salas disponiveis
    (4) Criar sala
    (0) sair
    """)


opcao = 10
while opcao != "0":
    menu ()
    opcao = input (" introduza uma opcao: ")
    if opcao == "1":
        print("Filmes Disponiveis:\n")
        listarfilmes(salas)
    elif opcao == "2":
        op1 = input ("Filme que pretende ver: ")
        op2 = input ("Lugar que pretende ficar: ")
        disponivel(salas,op1,op2)

    elif opcao == "3":
       listardisponibilidades(salas)
       
    elif opcao == "4":
        op1 = input ("Filme que quer adicionar: ")
        op2 = input ("Numero de lugares da sala: ")
        inserirsala(salas, op1,op2)
