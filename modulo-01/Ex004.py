from math import sqrt


def bhaskara(a, b, c):
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


bhaskara(1, 1, 6)
