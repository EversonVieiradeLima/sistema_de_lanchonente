# Identificador Pessoal
identificador_pessoal = 'Éverson Vieira de Lima'
print('Bem Vindo a Lanchonete do {}'.format(identificador_pessoal))

print('*****************Cardápio*****************')
print('| Código |       Descrição       | Valor |')
print('|   100  |    Cachorro Quente    |  9,00 |')
print('|   101  | Cachorro Quente Duplo | 11,00 |')
print('|   102  |         X-Egg         | 12,00 |')
print('|   103  |       X-Salada        | 12,00 |')
print('|   104  |        X-Bacon        | 14,00 |')
print('|   105  |        X-Tudo         | 17,00 |')
print('|   200  |   Refrigerante Lata   |  5,00 |')
print('|   201  |      Chá Gelado       |  4,00 |')

total = 0 # Valor a ser acumulado a partir das compras
while True:
    codigo_produto = int(input('Digite o código do produto desejado: '))

    if codigo_produto == 100:
        print('Você pediu um Cachorro Quente no valor de R$9,00')
        total = total + 9 # Pega o valor acumulado e soma com 9

    elif codigo_produto == 101:
        print('Você pediu um Cachorro Quente Duplo no valor de R$11,00')
        total = total + 11 # Pega o valor acumulado e soma com 11

    elif codigo_produto == 102:
        print('Você pediu um X-Egg no valor de R$12,00')
        total = total + 12 # Pega o valor acumulado e soma com 12

    elif codigo_produto == 103:
        print('Você pediu um X-Salada no valor de R$12,00')
        total = total + 12 # Pega o valor acumulado e soma com 12

    elif codigo_produto == 104:
        print('Você pediu um X-Bacon no valor de R$14,00')
        total = total + 14 # Pega o valor acumulado e soma com 14

    elif codigo_produto == 105:
        print('Você pediu um X-Tudo no valor de R$17,00')
        total = total + 17 # Pega o valor acumulado e soma com 17

    elif codigo_produto == 200:
        print('Você pediu um Refrigerante Lata no valor de R$5,00')
        total = total + 5 # Pega o valor acumulado e soma com 5

    elif codigo_produto == 201:
        print('Você pediu um Chá Gelado no valor de R$4,00')
        total = total + 4 # Pega o valor acumulado e soma com 4

    else:
        print('Opção inválida')
        continue # Se digitar uma opção diferente da tabela informa "Opção inválida" e volta para o início do while

    print('Deseja pedir mais alguma coisa (1 - Sim | 2 - Não)?')
    pedir_mais = int(input('>> '))

    if pedir_mais == 1:
        continue # Se digitar a opção 1 volta para o início do while
    else:
        print('O total a ser pago é: R${:.2f}'.format(total))
        break # Se digitar outra opção mostra o resultado e encerra o programa