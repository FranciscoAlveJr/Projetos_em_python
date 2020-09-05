from datetime import date
ano = int(input('Qual o ano de seu nascimento? '))
anoatual = date.today().year
idade = anoatual - ano
if idade < 18:
    if (18-idade) == 1:
        print(f'Falta {18 - idade} ano para você se alistar!')
    else:
        print(f'Faltam {18 - idade} anos para você se alistar!')
elif idade == 18:
    print('Esse ano você completa ou completou 18 anos. Aliste-se já!')
elif idade > 18:
    if (idade-18) == 1:
        print(f'Já se passou {idade - 18} ano do seu alistamento! Não perca mais tempo e aliste-se!')
    else:
        print(f'Já se passaram {idade - 18} anos do seu alistamento! Não perca mais tempo e aliste-se!')