from math import sqrt

print('Equações do segundo grau em python')
print(" ax²+bx+c ")
resp = ''

while True:
    a = float(input('Digite o valor de A: '))
    b = float(input('Digite o valor de B: '))
    c = float(input('Digite o valor de C: '))

    d = (b ** 2) - (4 * a * c)

    if d > 0:
        x1 = ((-b) + sqrt(d)) / (2 * a)
        x2 = ((-b) - sqrt(d)) / (2 * a)
        print("Existem duas possibilidades de resolução, sendo X': {} e X'': {}".format(x1, x2))
    elif d == 0:
        x = (-b) / 2 * a
        print("Há uma possibilidade de resolução: ", x)
    elif d < 0:
        print('Não há possibilidade de resolução para raízes negativas')

    resp = str(input('Deseja testar novos valores? [S/N]')).strip().upper()[0]
    if resp == 'N':
        print('Programa encerrado!')
        break
