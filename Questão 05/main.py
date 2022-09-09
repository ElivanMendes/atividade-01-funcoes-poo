heigth = float(input('Informe a Altura do Cilindro: '))
radius = float(input('Informe o Raio do Cilindro: '))


def cylinder_volume(height, radius):
    return 3.14 * radius ** 2 * height


print(f'Volume do Cilindro: {cylinder_volume(heigth, radius):.2f}')
