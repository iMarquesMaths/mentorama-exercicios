par = []
impar = []
for count in range(1, 11):
    if count % 2 == 0:
        par.append(count)
    else:
        impar.append(count)
print('Entre os números 1 e 10 existem {} numeros pares e {} numeros ímpares'.format(len(par), len(impar)))
print('As somas dos valores pares resulta em {} e dos valores ímpares em {}'.format(sum(par), sum(impar)))
