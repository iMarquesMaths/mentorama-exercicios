print('Equações do segundo grau em python')
print(" ax2+bx+c ")

a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))

d = (b**2) - (4 * a * c)

if d > 0:
    x1 = ((-b) + (d ** 0.5)) / (2 * a)
    x2 = ((-b) - (d ** 0.5)) / (2 * a)
    print("Existem duas possibilidades de resolução, sendo X': {} e X'': {}".format(x1, x2))
elif d == 0:
    x = (-b) / 2 * a
    print("Há uma possibilidade de resolução: ", x)
else:
    print('Não há possibilidade de resolução para raízes negativas')
