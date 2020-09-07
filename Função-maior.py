def maior(*par):
    print('=+=' * 10)
    print('Analisando os valores passados...')
    if len(par) == 1:
        for n in par:
            print(n, end=' ')
        print(f'foi informado {len(par)} valor.')
    elif len(par) == 0:
        print(f'Nenhum valor foi informado.')
    else:
        for n in par:
            print(n, end=' ')
        print(f'foram informados {len(par)} valores ao todo.')
    mai = 1
    for m in par:
        if m > mai:
            mai = m
    if len(par) > 0:
        print(f'O maior valor informado foi {mai}.')


maior(1, 6, 3, 34, 2, 9, 6)
maior()
maior(6)
maior(9, 4)
