#tpc2

#1)O utilizador tenta divnhar o numero sorteado pelo computador

import random
from random import randrange

tentativa=0

numeroPensado= random.randrange(1,100)
n=0

while n is not numeroPensado:
    tentativa=tentativa + 1
    n=int(input("Adivinhe o número: "))
    if numeroPensado > n:
        print("O número está acima de", n)
    elif numeroPensado < n:
        print("O número é menor do que", n)
    else:
        print("Acertou!!")
        print("Conseguiu acertar o número em", tentativa,"tentativas")
    n=n+1
    



#2) Computador a adivinhar o numero escolhido pelo utilizador
        
numeroPensado = input("introduzir numero pensado entre 0 a 100:")


n = 50
tentativa = 0



while n is not numeroPensado :
    
    print("o numero advinhado foi:", n)
    
         
        
    maior_ou_menor = input("Escreve '1' se o numero adivinhado for maior do que o pensado.  '-1' se o numero advinhado for menor do que  o pensado. Ou '0' se o numero adivinhado for o numero pensado: ")
    
    tentativa = tentativa + 1
    
    
    if maior_ou_menor == "1" :
        
        n = n + n//2
        
        
    
    
    elif maior_ou_menor =="-1":
        
          n= n- n//2
         
    
    else: 
        print("Acertou")
        print("O computador demorou" , tentativa , "tentativas")   

        break
