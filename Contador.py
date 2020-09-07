from time import sleep


def contador(inicio, fim, passo):
    print('-+-' * 10)
    if inicio > fim:
        if passo < 0:
            print(f'Contagem de {inicio} até {fim} de {-passo} em {-passo}.')
            for c in range(inicio, (fim - 1), passo):
                sleep(0.3)
                print(c, end=' ')
            print('FIM!')
        elif passo > 0:
            print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
            for c in range(inicio, (fim - 1), (-passo)):
                sleep(0.3)
                print(c, end=' ')
            print('FIM!')
        elif passo == 0:
            passo = 1
            print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
            for c in range(inicio, (fim - 1), (-passo)):
                sleep(0.3)
                print(c, end=' ')
            print('FIM!')
    else:
        if passo > 0:
            print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
            for c in range(inicio, (fim + 1), passo):
                sleep(0.3)
                print(c, end=' ')
            sleep(0.3)
            print('FIM!')
        elif passo < 0:
            print(f'Contagem de {inicio} até {fim} de {(-passo)} em {(-passo)}')
            for c in range(inicio, (fim + 1), (-passo)):
                sleep(0.3)
                print(c, end=' ')
            sleep(0.3)
            print('FIM!')
        elif passo == 0:
            passo = 1
            print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
            for c in range(inicio, (fim + 1), passo):
                sleep(0.3)
                print(c, end=' ')
            sleep(0.3)
            print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-' * 30)
print('Agora é sua de personalizar a contagem:')
ini = int(input('Início: '))
fi = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fi, pas)
