#EXERCICIO 1
def maximo(*valor:int):
    n1 = valor[0]
    n2 = valor[1]

    valor = n2
    if(n1 > n2):
       valor = n1   

    return valor

n1 = input("Digite o primeiro numero: ")
n2 = input("Digite o segundo numero: ")

print("O numero maior é: "+maximo(n1, n2))


#EXERCICIO 2
def mult(*valor:int):
    n1 = valor[0]
    n2 = valor[1]

    n3 = False
    if  n1 % n2 == 0:
        n3 = True  

    return n3

print(mult(35,7))

#EXERCICIO 3

def quad(n1:int):
    area = n1*n1
    return area

print(f'{quad(3.25):.2f}')

