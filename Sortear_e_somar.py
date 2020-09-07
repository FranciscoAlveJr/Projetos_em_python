from random import randint
from time import sleep


def sorteia(lista):
    for n in range(5):
        lista.append(randint(1, 10))
    print('Sorteando 5 valores da lista: ', end='')
    for l in lista:
        sleep(0.3)
        print(l, end=' ')
    sleep(0.3)
    print('PRONTO!')


def somapar(num):
    soma = 0
    for n in num:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {num}, temos {soma}')


numeros = []
sorteia(numeros)
somapar(numeros)