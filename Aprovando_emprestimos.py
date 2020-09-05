casa = float(input('Qual o valor da casa para o empréstimo? '))
salario = float(input('Qual é o seu salario? '))
anos = float(input('Em quantos anos vai pagar? '))
meses = 12 * anos
parcelas = casa / meses
if parcelas <= (salario * 0.3):
    print(f'\033[34mParabéns!!! Seu empréstimo foi aprovado com parcelas de R${parcelas:.2f} por mês!\033[m')
elif parcelas > (salario * 0.3):
    print('\033[31mInfelizmente, seu empréstimo não foi aprovado devido ao valor excedido de 30%\033[m')
