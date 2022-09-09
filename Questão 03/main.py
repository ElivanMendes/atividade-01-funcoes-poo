radius = float(input('Informe o Raio da Esfera: '))


def sphere_volume(radius):
    return (4 * 3.14 * radius ** 3) / 3


print(f'O Volume da Esfera e: {sphere_volume(radius):.2f}')
