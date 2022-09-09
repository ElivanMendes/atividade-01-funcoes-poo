number = int(input('Informe um Numero Inteiro: '))


def check_number(number):
    if number > 0:
        return  1
    elif number < 0:
        return -1
    else:
        return 0


if check_number(number) == 1:
    print('Numero positivo!')
elif check_number(number) == -1:
    print('Numero Negativo!')
else:
    print('Numero igual a 0!')
