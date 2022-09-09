number_1 = float(input('Informe o Primeiro Numero: '))
number_2 = float(input('Informe o Segundo Numero: '))


def higher_number(number_1, number_2):
    return number_1 if number_1 > number_2 else number_2


print(f'Maior Numero: {higher_number(number_1, number_2):.2f}')
